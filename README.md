# 🎓 Class Directory Creation Tool

The **Class Directory Creation Tool** is a Python-based automation utility that I designed for my personal use to create and personalize organized directory templates for college courses.  
It helps streamline my academic workflow at the beginning of each term by automatically generating subfolders, APA-formatted Word files, and course-specific names.

---

## 🚀 Features

✅ Automatically creates a pre-structured class directory  
✅ Builds nested folders for Units, Discussions, Assignments, and more  
✅ Generates preformatted Word documents with custom styles  
✅ Dynamically renames folders and updates text with specified course name  
✅ Supports **interactive prompts** (wizard) and **command-line options**  
✅ Displays clear visual feedback:  
   - 💬 for prompts  
   - ✅ for success  
   - ❌ for errors  
   - ℹ️ for informational messages
   - 💡 for tool tips
✅ Can be packaged into a single `.exe` for Windows (using PyInstaller)

---

## 🧠 How It Works

### 🟢 Interactive Mode

Run the interactive wizard that guides you step-by-step:

```bash
python central_control.py
```

or after packaging:

```bash
ClassDirectoryTool.exe
```

You’ll be prompted to create the directory structure, rename it with your course name, and automatically update text within Word files.

---

### ⚙️ CLI Flags

By default, the program launches the **interactive wizard**. You can also control behavior with flags:

**Interactive (explicit)**
```bash
python central_control.py --interactive
```

**Non-Interactive (in progress)**
```bash
python central_control.py --noninteractive
```

**Version Information**
```bash
python central_control.py --version
```

**Help**
```bash
python central_control.py --help
```

---

## 🧩 Project Structure

```
ClassDirectoryTool/
│
├── __pycache__/               # Compiled Python cache (auto-generated)
├── build/                     # PyInstaller build artifacts
├── dist/                      # Packaged executable and supporting files
│
├── central_control.py                     # Main command-line interface (entry point)
├── create_template.py         # Creates directory and file structure
├── personalize_docs.py             # Renames folders and modifies Word content
├── version.py                 # Version tracking and semantic versioning notes
│
├── README.md                  # Project documentation
│
├── ClassDirectoryTool.spec # PyInstaller spec file for current executable
```

---

## 🧰 Requirements

**Python 3.10+**

Required libraries:
```bash
pip install python-docx colorama
```
*(Note: `argparse`, `os`, `re`, `sys`, and `shutil` are built into Python, but are listed here for clarity.)*

Optional (for packaging):
```bash
pip install pyinstaller
```

---

## 🏗️ Building the Executable

To package the project into a standalone `.exe` (for Windows):

```bash
pyinstaller --onefile --clean --name ClassDirectoryTool central_control.py
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
v0.8.0 — Pre-release build (interactive mode functional; CLI parameters in development)
```

---

## 💡 Future Plans

- [ ] Add CLI flags: `--create`, `--rename`, `--modify`
- [ ] Add logging for automation and error reporting
- [ ] Optional GUI interface for non-technical users

---

## 🧠 Learning Outcomes

This project demonstrates:

- Practical use of **Python automation**
- File and directory manipulation with `os` and `shutil`
- Word document creation and editing using `python-docx`
- CLI design and argument parsing with `argparse`
- Use of regular expressions with `re` for pattern-based sorting
- Software modularity across multiple Python files
- Cross-module imports and function reuse
- Command-line interaction with visual feedback
- Packaging Python scripts into a standalone Windows executable with `PyInstaller`
- Implementation of semantic versioning (SemVer) for release tracking
- Clear project documentation using Markdown (README.md)
- Safe experimentation in a **virtualized sandbox environment (Oracle VirtualBox)**

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

Special thanks to open-source developers and documentation writers whose tools make learning and experimentation possible — including the maintainers of **python-docx**, **colorama**, and **PyInstaller**.

---

Test change made from VM (Developer A)

Test change made from local machine (Developer B) (New edit on VM)