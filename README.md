# Zelscript

Small, single-purpose CLI helpers that plug into the wider Zel suite.

## Getting Started

**First, install the Zel ecosystem:**
```bash
curl -sSL https://raw.githubusercontent.com/Zeldean/zelutil/main/bootstrap-zel.py | python3
```

This sets up ZelUtil and makes all Zel tools available. See the [ZelUtil repository](https://github.com/Zeldean/zelutil) for details.

---

## Installation

```bash
pip install zelscript
```

From source:

```bash
git clone https://github.com/Zeldean/zelscript.git
cd zelscript
pip install -e .
```

---

## Commands

Run everything through the `zelscript` entry point:

| Command | Description |
| ------- | ----------- |
| `zelscript choose OPTION…` | Pick a random option 11 times, then announce a winner. |
| `zelscript welcome` | Print the ASCII-art welcome banner. |
| `zelscript timer [work rest cycles]` | Quick terminal Pomodoro (default `25 5 4`). |
| `zelscript rename-phineas /path/to/folder` | Rename files to `Phineas_and_Ferb_SxxEyy.*` based on SxxEyy matches. |

All commands are built with Click, so `--help` is available on each subcommand.

---

## Examples

```bash
# Random lunch picker
zelscript choose pizza ramen curry

# 3x 40/10 Pomodoro block
zelscript timer 40 10 3

# Normalise episode filenames
zelscript rename-phineas ~/Shows/Phineas
```

---

## Developing new utilities

- Add a module in `src/zelscript/commands/` or `src/zelscript/tools/`.
- Register the Click command in `src/zelscript/cli.py`.
- Keep dependencies minimal—`click` is the only mandatory runtime requirement.
