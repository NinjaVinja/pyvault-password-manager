# 🔐 PyVault - Password Manager

A simple desktop password manager built with Python's Tkinter GUI toolkit. Generate strong random passwords, save your website credentials locally, and manage them through a clean, minimal interface.

## Features

- **Random Password Generator** — Creates strong passwords combining random letters, numbers, and symbols
- **Save Credentials** — Store website, email/username, and password entries locally
- **Input Validation** — Prevents saving incomplete entries
- **Confirmation Dialog** — Reviews details before writing to file
- **Simple GUI** — Built entirely with Tkinter, no external UI dependencies

## Screenshot

*(Add a screenshot of the app here)*

## Tech Stack

- Python 3
- Tkinter (GUI)
- Random module (password generation)

## Getting Started

### Prerequisites

- Python 3.x installed
- A `logo.png` file in the project directory (used as the app's canvas image)

### Installation

```bash
git clone https://github.com/NinjaVinja/pyvault-password-manager.git
cd pyvault-password-manager
python main.py
```

### Usage

1. Enter the website name and your email/username
2. Click **Generate Password** to auto-create a strong password, or type your own
3. Click **Add** to save the entry
4. Confirm the details in the popup dialog
5. Your credentials are saved to `data.txt` in the format:
   ```
   website | email | password
   ```

## Project Structure

```
pyvault-password-manager/
│
├── main.py          # Main application file
├── logo.png          # App logo/image
├── data.txt           # Saved credentials (auto-generated)
└── README.md
```

## Future Improvements

- [ ] Encrypt saved passwords instead of storing in plain text
- [ ] Add a search/lookup feature for saved websites
- [ ] Migrate storage from `.txt` to JSON or a database
- [ ] Add a master password / login screen
- [ ] Add copy-to-clipboard functionality

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Muhammad Taha Ahmad** ([NinjaVinja](https://github.com/NinjaVinja))
