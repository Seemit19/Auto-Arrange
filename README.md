# AutoArrange 🧹

**AutoArrange** is a Python tool that organizes cluttered folders by automatically sorting files into categorized folders based on their extensions.

> "A clean folder is a happy folder."

---

## 📂 What It Does

AutoArrange helps you:
- Categorize files like Images, Documents, Videos, etc.
- Automatically create folders for each category
- Move files into their respective folders
- Preview the organization (dry run)
- Undo the organization if needed

---

## 🔧 Features

- 📦 **Auto-Sorting**: Organizes files into folders like `Images`, `Videos`, `Documents`, etc.
- 🧪 **Dry Run Mode**: See where your files will go before moving them.
- ↩️ **Undo Option**: Reverts the organization and restores your files.
- 💻 **Simple CLI**: Just run and follow prompts — no coding knowledge needed.

---

## 📸 Screenshot / Example
Imagine this mess:

Downloads/

├── report.pdf

├── selfie.jpg

├── song.mp3 

├── script.py 

**Becomes this:**

Organized_Files/

├── Documents/ report.pdf

├── Images/ selfie.jpg

├── Audio/ song.mp3

├── Program/ script.py

---

## Running the Script

Save the script as autoarrange.py, then run it:

|  python autoarrange.py   |

You’ll be guided through these steps:

 - Enter the folder with unorganized files.
 - Enter the folder where files should be sorted.
 - Optionally preview the changes (dry run).
 - Confirm to proceed.
 - Optionally undo the operation.

## 🔮 Future Plans

 - Add GUI version
 - Add logging for move history
 - Allow user-defined custom categories
 - Support automatic folder monitoring

## 💬 Contributions

 - If you'd like to suggest a feature, report a bug, or contribute to development, feel free to open an issue or fork the repo and make a pull request.

## 🙌 Acknowledgments

 - Built with Python, love, and the desire to never sort folders manually again.
   
## License

 - This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
