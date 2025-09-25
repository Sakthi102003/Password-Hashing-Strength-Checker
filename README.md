# Password Hashing & Strength Checker

A simple desktop GUI tool built with Tkinter that lets you:
- **Hash passwords** using SHA-256
- **Evaluate password strength** (WEAK, MEDIUM, STRONG) with color-coded feedback and a reason
- **Show/Hide password** while typing

File: `passwordhash.py`

---

## Features
- **SHA-256 hashing**: Displays the hexadecimal hash of the entered password
- **Strength categories**: WEAK, MEDIUM, STRONG based on length and character variety
- **Reasoned feedback**: Explains why the password falls into a category
- **Common password check**: Flags extremely common passwords
- **Privacy**: All operations are local; nothing is sent over the network

## Requirements
- **Python**: 3.8+ recommended
- **Tkinter**: Included with most Python distributions
  - Ubuntu/Debian: `sudo apt-get install python3-tk`
  - Fedora: `sudo dnf install python3-tkinter`
  - Windows/macOS (python.org installers): Tkinter included by default

## Run
1. Open a terminal in the project directory.
2. Run the script:
   - Windows (cmd/PowerShell):
     ```powershell
     python passwordhash.py
     ```
   - Linux/macOS:
     ```bash
     python3 passwordhash.py
     ```

## How to Use
1. Type a password in the input field (masked by default).
2. Click **Check** or press **Enter**.
3. Toggle **Show Password** to reveal/hide the input.
4. View:
   - **Password Strength** (color-coded)
   - **Reason** for the classification
   - **SHA-256 hash** of the input

## Strength Rules (Summary)
The script applies the following checks (see `check_strength` in the code):
- **Common password** (e.g., `123456`, `password`, etc.) → WEAK
- **Too short** (length < 6) → WEAK
- **Character types detected**: uppercase, lowercase, digit, symbol
  - **STRONG**: length ≥ 8 and at least 3 of the 4 character types
  - **MEDIUM**: length ≥ 6 and at least 2 of the 4 character types
  - **WEAK**: otherwise

## Customization
- **Common password list**: Edit `common_passwords` in `passwordhash.py` to add/remove entries.
- **Rules/Thresholds**: Adjust logic in `check_strength()` (regexes or scoring).
- **UI tweaks**: Change window size, fonts, and labels in the Tkinter setup section.

## Security Notes
- This tool is for **education and demonstration**. It provides a simple heuristic, not a formal security audit.
- SHA-256 hashing here is **one-way display only** (no salts, iterations, or storage). For real applications, use vetted password hashing libraries (e.g., `argon2`, `bcrypt`, `scrypt`).

## Project Structure
```
.
├── passwordhash.py   # Tkinter app: hashing + strength checker
└── README.md         # This documentation
```

## License
You may use and modify this code for learning and personal projects. For production use, review and harden the logic to meet your security requirements.