# 🎓 Class Directory Creation Tool

The **Class Directory Creation Tool** is a Python-based automation utility that I designed for my personal use to create and personalize organized directory templates for college courses.  
It helps streamline my academic workflow at the beginning of each term by automatically generating subfolders, APA-formatted Word files, and course-specific names for my archives.

---

## 🚀 Features

✅ Automatically creates a pre-structured class directory  
✅ Builds nested folders for Units, Discussions, Assignments, and more  
✅ Generates preformatted Word documents with custom styles  
✅ Renames folders and updates text with specified course name  
✅ Supports interactive prompts (wizard) and command-line options
✅ Displays clear visual feedback in the wizard:
   - 💬 for prompts  
   - ✅ for success  
   - ❌ for errors  
   - ℹ️ for informational messages
   - 💡 for tool tips
✅ Can be packaged into a single `.exe` for Windows (using PyInstaller)
✅ The `.exe` launches a GUI for non-technical users and general ease of use 

---

## 🧠 How It Works

### 🟢 Interactive Mode

Run the interactive wizard that guides you step-by-step:

```bash
python cli_control.py
```

or after packaging:

```bash
ClassDirectoryTool.exe
```

You’ll be prompted to create the directory structure, rename it with your course name, and automatically update text within Word files.

---

### ⚙️ CLI Flags

By default, `cli_control.py` launches the interactive wizard. You can also control behavior with flags:

**Interactive**
```bash
python cli_control.py --interactive
```

**Non-Interactive (in progress)**
```bash
python cli_control.py --noninteractive
```

**Version Information**
```bash
python cli_control.py --version
```

**Help**
```bash
python cli_control.py --help
```

---

## 🧩 Project Structure

```
ClassDirectoryTool/
│
├── venv                       # Project virtual environment (not committed to Git)
|
├── cli_control.py             # CLI entry point (argparse-based)
|── ui_control.py              # GUI entry point (Tkinter-based)
├── create_template.py         # Creates directory and file structure
├── personalize_docs.py        # Renames folders and modifies Word content
├── version.py                 # Version tracking and semantic versioning notes
│
├── requirements.txt           # Project dependencies for recreating the venv
├── README.md                  # Project documentation
|
├── .gitignore                 # Excludes venv, cache, build artifacts, etc.
|
└── foldericon.ico             # Used for both Tkinter window icon and PyInstaller executable icon

```

### 📦 Build Artifacts (Generated Later)

These folders and files are created when running PyInstaller:

```
ClassDirectoryTool/
│
├── build/                    # PyInstaller build artifacts (auto-generated)
├── dist/                     # Packaged executable output
└── ClassDirectoryTool.spec   # PyInstaller spec file for executable configuration

```

---

## 🧰 Requirements

**Python 3.10+**

Required libraries:
```bash
pip install python-docx colorama
```
*(Note: `argparse`, `os`, `re`, `sys`,`shutil`, and `tkinter` are built into Python, but are listed here for clarity.)*

Optional (for packaging):
```bash
pip install pyinstaller
```

---

## 🏗️ Building the Executable

To package the project into a standalone `.exe` (for Windows):

```bash
pyinstaller --onefile --clean --noconsole --add-data "foldericon.ico;." --icon=foldericon.ico --name ClassDirectoryTool ui_control.py
```

The executable will appear in the `dist/` folder as:
```
ClassDirectoryTool.exe
```

You can then run:
```bash
ClassDirectoryTool.exe
```

---

## 🧭 Versioning

Version information is stored in `version.py` and follows the **Semantic Versioning (SemVer)** standard:

```
MAJOR.MINOR.PATCH
```

| Segment | Meaning |
|----------|----------|
| **MAJOR** | Incompatible or breaking changes |
| **MINOR** | New features or major enhancements |
| **PATCH** | Bug fixes or small improvements |

Current version:
```
v0.8.0 — Pre-release build (interactive mode and GUI functional; CLI parameters in development)
```

---

## 💡 Future Plans

- [ ] Add CLI flags: `--create`, `--rename`, `--modify`
- [ ] Add logging for automation and error reporting

---

## 🧠 Learning Outcomes

This project demonstrates:

- Practical use of Python automation
- File and directory manipulation with `os` and `shutil`
- Word document creation and editing using `python-docx`
- CLI design and argument parsing with `argparse`
- Use of regular expressions with `re` for pattern-based sorting
- Software modularity across multiple Python files
- Cross-module imports and function reuse
- Command-line interaction with visual feedback
- Design and implementation of a graphical user interface (GUI) using `tkinter`
- Event-driven programming through GUI callbacks and user input handling
- Packaging Python scripts into a standalone Windows executable with `PyInstaller`
- Implementation of semantic versioning (SemVer) for release tracking
- Clear project documentation using Markdown (README.md)
- Safe experimentation in a virtualized sandbox environment (Oracle VirtualBox)

---

## 👤 Author

**Emmanuel Mot**  
Information Technology Major — Web and Software Development  
Purdue University Global  

---

## 📝 License

This project is intended for **educational and personal use**.  
You are free to modify or expand it for your own learning purposes.

---

### ⭐ Acknowledgements

Special thanks to open-source developers and documentation writers whose tools make learning and experimentation possible.

---