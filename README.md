
# Random Book Picker

A modern, interactive desktop application built in Python using CustomTkinter. It helps you keep track of your reading list and solves the "what should I read next?" dilemma by randomly selecting your next book!

## Features

- **Modern Dark UI:** A beautiful, responsive user interface utilizing the CustomTkinter toolkit.
- **Dynamic Book Library:** A scrollable container displaying your books with metadata (Title, Author, Genre).
- **Interactive Management:** Add new books instantly or remove them on the fly with single-click remove buttons.
- **Local Persistence:** Data is stored locally in a `library.json` file, ensuring your collection persists every time you reopen the app.
- **Random Selection:** Let the app randomly choose a book from your custom library!

---

## Operating System Setup Guides

Follow the specific steps below for your operating system to set up your environment and run the application.

### 🪟 Windows Setup

1. **Install Python:**
   - Download and install Python 3.x from the official website or the Microsoft Store.
   - **Important:** Make sure to check the box that says **"Add Python to PATH"** during installation.

2. **Install Dependencies:**
   Open Command Prompt or PowerShell and install the GUI framework:
   ```cmd
   pip install customtkinter
   ```

3. **Run the App:**
   Navigate to your project directory and execute:
   ```cmd
   python book_picker.py
   ```

---

### 🐧 Linux Setup (Ubuntu/Debian)

1. **Install Python and Tkinter:**
   Most Linux distributions have Python 3 pre-installed, but they often exclude the underlying GUI library (`tkinter`). Install both Python, Pip, and Tkinter using your package manager:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk -y
   ```

2. **Install Dependencies:**
   Use pip3 to install the CustomTkinter package:
   ```bash
   pip3 install customtkinter
   ```

3. **Run the App:**
   Navigate to your project directory and execute:
   ```bash
   python3 book_picker.py
   ```

---

### 🍏 macOS Setup

1. **Install Python:**
   - Mac comes with a default Python stub, but it is highly recommended to install the official latest Python 3 release using [Homebrew](https://brew.sh) or from the Python.org website.
   - To install via Homebrew:
     ```bash
     brew install python
     ```

2. **Install Dependencies:**
   Install the CustomTkinter library. If your Python environment requires active Tkinter bindings on macOS, Homebrew Python handles this automatically.
   ```bash
   pip3 install customtkinter
   ```

3. **Run the App:**
   Navigate to your project directory and execute:
   ```bash
   python3 book_picker.py
   ```

---

## Project Structure

- `book_picker.py` - The main Python script containing the GUI window layout, data loading/saving logic, and action controllers.
- `library.json` - Your local JSON database storing the book list in a structured format.

## Customizing Your Library

You can pre-populate your library directly inside `library.json`. The structure should look like this:

```json
[
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Sci-Fi"
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy"
    }
]
```
