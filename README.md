# 🛠️ Zelscript

> Small, single-purpose CLI helpers that plug into the wider Zel suite.

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🚀 Quick Start

### Install the Zel Ecosystem

```bash
curl -sSL https://raw.githubusercontent.com/Zeldean/zelutil/main/bootstrap-zel.py | python3
```

This sets up ZelUtil and makes all Zel tools available. See the [ZelUtil repository](https://github.com/Zeldean/zelutil) for details.

### Install Zelscript

**Via pip:**
```bash
pip install zelscript
```

**From source:**
```bash
git clone https://github.com/Zeldean/zelscript.git
cd zelscript
pip install -e .
```

---

## 📋 Available Commands

All commands run through the `zelscript` entry point. Use `zelscript --help` or `zelscript <command> --help` for detailed usage.

### 🎲 Random Choice Picker
```bash
zelscript choose OPTION [OPTION...]
```
Pick a random option from the provided list. Runs 11 selection rounds and announces a winner.

**Example:**
```bash
zelscript choose pizza ramen curry sushi
```

### ⏱️ Pomodoro Timer
```bash
zelscript timer [WORK] [REST] [CYCLES]
```
Terminal-based Pomodoro timer with live countdown display.
- **WORK**: Work duration in minutes (default: 25)
- **REST**: Rest duration in minutes (default: 5)
- **CYCLES**: Number of work/rest cycles (default: 4)

**Examples:**
```bash
zelscript timer              # Default: 25min work, 5min rest, 4 cycles
zelscript timer 40 10 3      # Custom: 40min work, 10min rest, 3 cycles
```

### 🔢 Sequential File Renamer
```bash
zelscript rename /path/to/folder
```
Rename all files in a directory to sequential format: `001.ext`, `002.ext`, `003.ext`, etc.

**Example:**
```bash
zelscript rename ~/Downloads/photos
```

### 🖼️ Image Format Converter
```bash
zelscript convert-png /path/to/folder
```
Convert all non-PNG images in a directory to PNG format. Original files are removed after conversion.

**Example:**
```bash
zelscript convert-png ~/Pictures/screenshots
```

### 👋 Welcome Banner
```bash
zelscript welcome
```
Display the ASCII art welcome banner with available commands.

---

## 📚 Command Reference

| Command | Description | Arguments |
|---------|-------------|----------|
| `choose` | Random option picker (11 rounds + winner) | `OPTION [OPTION...]` |
| `timer` | Pomodoro productivity timer | `[work] [rest] [cycles]` |
| `rename` | Sequential file renamer (001, 002, 003...) | `FOLDER` |
| `convert-png` | Convert images to PNG format | `FOLDER` |
| `welcome` | Display welcome banner | None |

---

## 🔧 Development

### Adding New Commands

1. Create a new module in `src/zelscript/commands/`
2. Implement your function with a clear docstring
3. Register the command in `src/zelscript/cli.py`
4. Keep dependencies minimal—`click` is the only mandatory requirement

### Project Structure

```
zelscript/
├── src/zelscript/
│   ├── commands/          # Command implementations
│   │   ├── choice.py
│   │   ├── timer.py
│   │   ├── rename_sequential.py
│   │   ├── convert_to_png.py
│   │   └── welcome.py
│   └── cli.py            # CLI entry point
├── pyproject.toml
└── README.md
```

---

## 📦 Dependencies

- **click** - CLI framework
- **Pillow** - Image processing (for `convert-png` command)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🔗 Related Projects

- [ZelUtil](https://github.com/Zeldean/zelutil) - Core Zel ecosystem utilities

---

**Made with ⚡ by Zeldean**
