"""
Interactive Audit Runner — Single-Keypress Workflow (Windows)
==============================================================
Designed to avoid the multi-line paste problem in terminals.
Uses msvcrt.getch() for single keypress — NO input() for responses.

Flow:
  1. Prompt auto-copied to clipboard
  2. You paste into AI web UI, get the response
  3. You SELECT ALL + COPY the AI response (Ctrl+A, Ctrl+C in ChatGPT)
  4. Come back to terminal, press SPACE — script reads clipboard, saves
  5. Auto-advances to next prompt

Usage:
  python scripts/run_audit.py                  # Start interactive mode
  python scripts/run_audit.py --agent chatgpt  # Start with specific agent
  python scripts/run_audit.py --status         # Show progress report
"""

import json
import os
import sys
import subprocess
import time
import datetime
import msvcrt

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PROMPTS_FILE = os.path.join(BASE_DIR, "prompts_parsed.json")
RESPONSES_DIR = os.path.join(BASE_DIR, "responses")
PROGRESS_FILE = os.path.join(BASE_DIR, "audit_progress.json")
DROP_FILE = os.path.join(BASE_DIR, "_PASTE_RESPONSE_HERE.md")

AGENTS = ["chatgpt", "gemini", "perplexity"]


# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
class C:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    END = "\033[0m"


# ---------------------------------------------------------------------------
# Input helper — flush stdin then read one keypress
# ---------------------------------------------------------------------------
def flush_stdin():
    """Drain any buffered input (from accidental paste) before reading."""
    while msvcrt.kbhit():
        msvcrt.getch()


def wait_key(prompt_text=""):
    """Print prompt, flush any buffered paste garbage, then wait for ONE keypress."""
    if prompt_text:
        print(prompt_text, end="", flush=True)
    flush_stdin()
    ch = msvcrt.getch()
    # Handle special keys (arrows etc) — ignore them
    if ch in (b'\x00', b'\xe0'):
        msvcrt.getch()  # consume second byte
        return None
    try:
        return ch.decode("utf-8", errors="ignore")
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Clipboard helpers
# ---------------------------------------------------------------------------
def copy_to_clipboard(text):
    """Copy text to Windows clipboard via PowerShell."""
    try:
        import pyperclip
        pyperclip.copy(text)
        return
    except Exception:
        pass
    try:
        process = subprocess.Popen(
            ["powershell", "-NoProfile", "-Command", "$input | Set-Clipboard"],
            stdin=subprocess.PIPE,
        )
        process.communicate(text.encode("utf-8"))
    except Exception as e:
        print(f"  {C.RED}Clipboard copy failed: {e}{C.END}")


def get_from_clipboard():
    """Read text from Windows clipboard via PowerShell."""
    try:
        import pyperclip
        return pyperclip.paste()
    except Exception:
        pass
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", "Get-Clipboard -Raw"],
            capture_output=True, text=True, encoding="utf-8",
        )
        return result.stdout
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# Drop-file helpers
# ---------------------------------------------------------------------------
DROPFILE_MARKER = "<!-- PASTE AI RESPONSE BELOW THIS LINE -->"


def prepare_drop_file(prompt_obj, agent):
    header = f"""# PASTE RESPONSE HERE
# Agent: {agent.upper()} | Site: {prompt_obj['site_name']} | Prompt {prompt_obj['prompt_num']}
#
# Paste the AI response below the marker, save (Ctrl+S), go back and press SPACE.

{DROPFILE_MARKER}

"""
    with open(DROP_FILE, "w", encoding="utf-8") as f:
        f.write(header)


def read_drop_file():
    if not os.path.exists(DROP_FILE):
        return ""
    with open(DROP_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    if DROPFILE_MARKER in content:
        return content.split(DROPFILE_MARKER, 1)[1].strip()
    return content.strip()


def open_file_in_editor(path):
    try:
        subprocess.Popen(["code", path], shell=True)
    except Exception:
        try:
            subprocess.Popen(["notepad", path])
        except Exception:
            print(f"  {C.YELLOW}Open manually: {path}{C.END}")


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------
def load_prompts():
    with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": {}, "skipped": {}, "started_at": datetime.datetime.now().isoformat()}


def save_progress(progress):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)


def get_response_path(agent, file_key):
    return os.path.join(RESPONSES_DIR, agent, f"{file_key}.md")


def is_done(agent, file_key, progress):
    key = f"{agent}:{file_key}"
    if key in progress.get("completed", {}):
        return True
    path = get_response_path(agent, file_key)
    return os.path.exists(path) and os.path.getsize(path) > 100


def is_skipped(agent, file_key, progress):
    return f"{agent}:{file_key}" in progress.get("skipped", {})


def save_response(agent, file_key, prompt_obj, response_text):
    path = get_response_path(agent, file_key)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    header = f"""# {prompt_obj['site_name']} - Prompt {prompt_obj['prompt_num']}: {prompt_obj['prompt_label']}
**Agent:** {agent.upper()}
**Site:** {prompt_obj['site_url']}
**Captured:** {datetime.datetime.now().isoformat()}

---

"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(header + response_text)


# ---------------------------------------------------------------------------
# Progress report
# ---------------------------------------------------------------------------
def show_progress_report(prompts, progress):
    print(f"\n{C.BOLD}{'='*70}{C.END}")
    print(f"{C.BOLD}  AUDIT PROGRESS REPORT{C.END}")
    print(f"{'='*70}\n")

    for agent in AGENTS:
        done = sum(1 for p in prompts if is_done(agent, p["file_key"], progress))
        skipped = sum(1 for p in prompts if is_skipped(agent, p["file_key"], progress))
        total = len(prompts)
        pct = (done / total) * 100 if total > 0 else 0

        bar_len = 30
        filled = int(bar_len * done / total)
        bar = f"{'#' * filled}{'-' * (bar_len - filled)}"

        color = C.GREEN if pct == 100 else C.YELLOW if pct > 50 else C.RED
        print(f"  {C.BOLD}{agent.upper():12s}{C.END} {color}[{bar}]{C.END} {done:3d}/{total} ({pct:5.1f}%)  "
              f"{C.DIM}skip:{skipped}{C.END}")

        sites = sorted(set(p["site_id"] for p in prompts))
        for sid in sites:
            sp = [p for p in prompts if p["site_id"] == sid]
            sd = sum(1 for p in sp if is_done(agent, p["file_key"], progress))
            nm = sp[0]["site_name"]
            st = f"{C.GREEN}DONE{C.END}" if sd == 6 else (f"{C.YELLOW}{sd}/6{C.END}" if sd > 0 else f"{C.DIM}0/6{C.END}")
            print(f"    Site {sid:2d}: {nm:20s} {st}")
        print()

    total_all = len(prompts) * len(AGENTS)
    done_all = sum(1 for a in AGENTS for p in prompts if is_done(a, p["file_key"], progress))
    print(f"  {C.BOLD}OVERALL: {done_all}/{total_all} ({done_all/total_all*100:.1f}%){C.END}\n")


# ---------------------------------------------------------------------------
# Core: capture response from clipboard or drop file
# ---------------------------------------------------------------------------
def capture_response(prompt_obj, agent, copied_prompt_snippet):
    """
    Try to capture the AI response. Returns (response_text, source) or (None, None).
    """
    time.sleep(0.3)  # let clipboard settle

    # Priority 1: drop file
    response = read_drop_file()
    source = "drop file"

    # Priority 2: clipboard
    if not response or len(response) < 50:
        response = get_from_clipboard()
        source = "clipboard"

    if not response or len(response.strip()) < 50:
        return None, "too_short"

    if response.strip()[:150] == copied_prompt_snippet[:150]:
        return None, "is_prompt"

    return response.strip(), source


# ---------------------------------------------------------------------------
# Core session runner
# ---------------------------------------------------------------------------
def run_agent_session(agent, prompts, progress):
    remaining = [
        p for p in prompts
        if not is_done(agent, p["file_key"], progress)
        and not is_skipped(agent, p["file_key"], progress)
    ]

    if not remaining:
        print(f"\n{C.GREEN}All prompts for {agent.upper()} are already complete!{C.END}")
        return

    total = len(prompts)
    done_before = total - len(remaining)

    print(f"\n{C.BOLD}{'='*70}{C.END}")
    print(f"{C.BOLD}  SESSION: {agent.upper()}  ({done_before}/{total} done, {len(remaining)} left){C.END}")
    print(f"{'='*70}")
    print(f"""
{C.CYAN}WORKFLOW:{C.END}
  1. Prompt is auto-copied to your clipboard
  2. Paste into {agent.upper()}, wait for full response
  3. SELECT ALL the AI response text, then COPY it (Ctrl+C)
  4. Come back here, press {C.GREEN}SPACE{C.END} to save

{C.CYAN}KEYS (single keypress, no Enter needed):{C.END}
  {C.GREEN}SPACE{C.END}  = Read clipboard and save response
  {C.YELLOW}O{C.END}      = Open drop file in editor (alternative paste method)
  {C.YELLOW}S{C.END}      = Skip this prompt
  {C.YELLOW}X{C.END}      = Skip entire site (all 6 prompts)
  {C.YELLOW}R{C.END}      = Re-copy prompt to clipboard
  {C.YELLOW}V{C.END}      = View current prompt
  {C.YELLOW}P{C.END}      = Show progress
  {C.RED}Q{C.END}      = Quit (saves progress)
""")

    idx = 0
    while idx < len(remaining):
        prompt_obj = remaining[idx]
        file_key = prompt_obj["file_key"]
        seq_num = idx + done_before + 1

        print(f"\n{C.BOLD}{'='*70}{C.END}")
        print(f"  {C.BOLD}[{seq_num}/{total}]{C.END}  "
              f"{C.CYAN}Site {prompt_obj['site_id']:2d}: {prompt_obj['site_name']}{C.END}  |  "
              f"Prompt {prompt_obj['prompt_num']}: {C.YELLOW}{prompt_obj['prompt_label']}{C.END}")
        print(f"  {C.DIM}URL: {prompt_obj['site_url']}{C.END}")
        print(f"  {C.DIM}File: responses/{agent}/{file_key}.md{C.END}")
        print(f"{'='*70}")

        # Copy prompt to clipboard
        copy_to_clipboard(prompt_obj["prompt_text"])
        print(f"\n  {C.GREEN}>>> PROMPT COPIED TO CLIPBOARD!{C.END}")
        print(f"  {C.DIM}Paste into {agent.upper()}, copy the response, press SPACE to save.{C.END}")

        # Reset drop file
        prepare_drop_file(prompt_obj, agent)
        copied_snippet = prompt_obj["prompt_text"][:200]

        while True:
            key = wait_key(f"\n  {C.BOLD}[SPACE=save O=dropfile S=skip X=skipsite R=recopy V=view P=progress Q=quit]: {C.END}")

            if key is None:
                continue

            key = key.lower()

            if key == "q":
                save_progress(progress)
                print(f"\n\n{C.GREEN}Saved! {seq_num - 1}/{total} done for {agent.upper()}.{C.END}")
                return

            elif key == "s":
                progress.setdefault("skipped", {})[f"{agent}:{file_key}"] = {
                    "at": datetime.datetime.now().isoformat(), "reason": "user_skip"
                }
                save_progress(progress)
                print(f"\n  {C.YELLOW}Skipped.{C.END}")
                idx += 1
                break

            elif key == "x":
                site_id = prompt_obj["site_id"]
                count = 0
                for j in range(idx, len(remaining)):
                    if remaining[j]["site_id"] == site_id:
                        fk = remaining[j]["file_key"]
                        progress.setdefault("skipped", {})[f"{agent}:{fk}"] = {
                            "at": datetime.datetime.now().isoformat(), "reason": "site_skip"
                        }
                        count += 1
                save_progress(progress)
                print(f"\n  {C.YELLOW}Skipped {count} prompts for {prompt_obj['site_name']}.{C.END}")
                while idx < len(remaining) and remaining[idx]["site_id"] == site_id:
                    idx += 1
                break

            elif key == "o":
                prepare_drop_file(prompt_obj, agent)
                open_file_in_editor(DROP_FILE)
                print(f"\n  {C.GREEN}Drop file opened.{C.END} Paste response, save (Ctrl+S), press SPACE.")
                continue

            elif key == "r":
                copy_to_clipboard(prompt_obj["prompt_text"])
                print(f"\n  {C.GREEN}>>> Prompt re-copied.{C.END}")
                continue

            elif key == "v":
                txt = prompt_obj["prompt_text"]
                print(f"\n{C.DIM}{'='*60}{C.END}")
                print(txt[:1000])
                if len(txt) > 1000:
                    print(f"  {C.DIM}... ({len(txt)} chars){C.END}")
                print(f"{C.DIM}{'='*60}{C.END}")
                continue

            elif key == "p":
                print()
                show_progress_report(prompts, progress)
                continue

            elif key == " ":
                # ---- CAPTURE RESPONSE ----
                response, source = capture_response(prompt_obj, agent, copied_snippet)

                if source == "too_short":
                    print(f"\n  {C.RED}Clipboard/drop file empty or <50 chars.{C.END}")
                    print(f"  {C.RED}Copy the AI response first, then press SPACE.{C.END}")
                    continue

                if source == "is_prompt":
                    print(f"\n  {C.RED}That's the PROMPT, not the response!{C.END}")
                    print(f"  {C.RED}Copy the AI's RESPONSE, then press SPACE.{C.END}")
                    continue

                lines = response.split("\n")

                # Show preview
                print(f"\n\n  {C.CYAN}--- PREVIEW ({source}: {len(response):,} chars, {len(lines)} lines) ---{C.END}")
                for ln in lines[:3]:
                    print(f"  {C.DIM}{ln[:100]}{C.END}")
                if len(lines) > 5:
                    print(f"  {C.DIM}  ... ({len(lines) - 5} more lines) ...{C.END}")
                for ln in lines[-2:]:
                    print(f"  {C.DIM}{ln[:100]}{C.END}")
                print(f"  {C.CYAN}--- END PREVIEW ---{C.END}")

                # Confirm with single keypress
                flush_stdin()
                print(f"\n  {C.BOLD}Save? [Y]=yes  [N]=discard  [O]=use drop file instead{C.END}", end="", flush=True)
                confirm = wait_key("")

                if confirm and confirm.lower() in ("y", " ", "\r", "\n"):
                    save_response(agent, file_key, prompt_obj, response)
                    progress.setdefault("completed", {})[f"{agent}:{file_key}"] = {
                        "at": datetime.datetime.now().isoformat(),
                        "chars": len(response),
                        "source": source,
                    }
                    save_progress(progress)
                    print(f"\n\n  {C.GREEN}SAVED! ({len(response):,} chars){C.END}")
                    print(f"  {C.DIM}-> responses/{agent}/{file_key}.md{C.END}")
                    idx += 1
                    break
                elif confirm and confirm.lower() == "o":
                    prepare_drop_file(prompt_obj, agent)
                    open_file_in_editor(DROP_FILE)
                    print(f"\n\n  {C.GREEN}Drop file opened.{C.END} Paste, save, press SPACE.")
                    continue
                else:
                    print(f"\n\n  {C.YELLOW}Discarded. Copy the response again and press SPACE.{C.END}")
                    continue

            else:
                # Any other key — show help briefly
                print(f"\n  {C.DIM}SPACE=save O=drop S=skip X=skipsite R=recopy V=view P=progress Q=quit{C.END}")


# ---------------------------------------------------------------------------
# Agent selection (uses input() — this is safe, single line only)
# ---------------------------------------------------------------------------
def select_agent():
    print(f"\n{C.BOLD}Select AI Agent:{C.END}\n")
    for i, a in enumerate(AGENTS, 1):
        print(f"  {i}. {a.upper()}")
    print(f"  4. Progress report")
    print(f"  5. Quit")

    while True:
        try:
            choice = input(f"\n  {C.BOLD}Choice (1-5): {C.END}").strip()
        except (EOFError, KeyboardInterrupt):
            return None
        if choice in ("1", "2", "3"):
            return AGENTS[int(choice) - 1]
        elif choice == "4":
            return "progress"
        elif choice == "5":
            return None
        print(f"  {C.DIM}Enter 1-5.{C.END}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    prompts = load_prompts()
    progress = load_progress()

    print(f"\n{C.BOLD}{'='*70}{C.END}")
    print(f"{C.BOLD}   WEBSITE AUDIT - AI RESPONSE COLLECTOR{C.END}")
    print(f"{C.BOLD}   {len(prompts)} prompts x {len(AGENTS)} agents = {len(prompts) * len(AGENTS)} total{C.END}")
    print(f"{'='*70}")

    if "--status" in sys.argv:
        show_progress_report(prompts, progress)
        return

    start_agent = None
    if "--agent" in sys.argv:
        i = sys.argv.index("--agent")
        if i + 1 < len(sys.argv) and sys.argv[i + 1] in AGENTS:
            start_agent = sys.argv[i + 1]

    if start_agent:
        run_agent_session(start_agent, prompts, progress)
    else:
        while True:
            show_progress_report(prompts, progress)
            choice = select_agent()
            if choice is None:
                print(f"\n{C.GREEN}Goodbye! Progress in audit_progress.json{C.END}")
                break
            elif choice == "progress":
                show_progress_report(prompts, progress)
            else:
                run_agent_session(choice, prompts, progress)

    if os.path.exists(DROP_FILE):
        try:
            os.remove(DROP_FILE)
        except Exception:
            pass


if __name__ == "__main__":
    main()
