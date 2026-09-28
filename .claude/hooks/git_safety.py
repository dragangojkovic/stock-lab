"""
PreToolUse hook (matcher: Bash) — blokira git komande koje CLAUDE.md izricito
zabranjuje: amendovanje starih komita, force push, i hard reset (nepovratno
gube ili prepravljaju istoriju, sto krsi "bez retroaktivnih izmena" pravilo).

Cita hook event JSON sa stdin, exit code 2 blokira poziv alata i vraca stderr
Claude-u kao razlog.
"""
import json
import re
import sys

BLOCKED = [
    (r"\bgit\s+commit\b[^|;&\n]*(--amend|-{1,2}amend\b)",
     "git commit --amend je zabranjen (CLAUDE.md SS11: 'Ne amenduj-ujem stare git "
     "komite'). Napravi NOV commit umesto izmene starog."),
    (r"\bgit\s+push\b[^|;&\n]*(--force(-with-lease)?\b|(?:^|\s)-f(?:\s|$))",
     "git push --force je zabranjen (prepisuje udaljenu istoriju). Ako je zaista "
     "potrebno, to je Draganova odluka - pitaj eksplicitno, ne izvrsavaj sam."),
    (r"\bgit\s+reset\b[^|;&\n]*--hard\b",
     "git reset --hard je destruktivan (brise lokalne izmene bez povratka) i "
     "blokiran je ovim hook-om. Koristi git stash ili nov commit."),
]


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    if payload.get("tool_name") != "Bash":
        sys.exit(0)

    command = (payload.get("tool_input") or {}).get("command", "") or ""

    for pattern, message in BLOCKED:
        if re.search(pattern, command, re.IGNORECASE):
            sys.stderr.write(message + "\n")
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
