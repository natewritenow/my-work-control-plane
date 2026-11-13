# My work control plane

A clickable prototype of My work in Aha! software, reimagined as the place a product manager steers AI agents across the product development lifecycle. All names and data are invented.

### Open it

Open `index.html` in a browser. It is one self-contained page with no build step and no server.

To serve it locally instead:

```bash
python3 -m http.server 8000
```

Then go to `http://localhost:8000`.

### What to try

1. **Decisions.** Click any row to open it in the drawer, then act on it. Every action says what happens first and can be undone.
2. **Stages.** Click a stage card, such as Plan, to filter the decisions and the agent actions to that stage.
3. **Mine and My team.** Switch to see what the team is waiting on.
4. **Meetings.** Pick a meeting to see its agenda, Elle's suggestions, notes with owners, and previous meetings.
5. **Agents.** Click an agent in the left navigation to chat with it, or open Settings to change how much it does on its own.

### Files

| File | What it is |
|---|---|
| `index.html` | The prototype. Built from `src.html`. |
| `src.html` | The source. Edit this, then run `python3 build.py`. |
| `aha.css` | The Aha! design system styles. |
| `icons.svg` | The Aha! icon set, inlined into `index.html` by the build. |

Profile photos load from randomuser.me. Without a connection, people show as initials.
