# 🧾 Elden Ring Death Counter (Tkinter)

A simple **Python Tkinter** application that tracks the number of times you’ve died while playing *Elden Ring* (or any other game).  
This project was my **first time using Tkinter**, and it helped me learn how to create GUIs, handle file saving/loading, and manage persistent data between sessions.

---

## 📦 Features

- ✅ Simple and clean graphical interface  
- ➕ Increase your death count with a single click  
- 🔁 Reset your counter anytime  
- 💾 Manual **Save** button  
- 🧠 **Auto-save** on exit — automatically saves progress before closing the window  
- ⚙️ Config file system for storing the icon and save data  

---

## 🗂️ Project Structure
project_folder/
│
├── main.py # Main program (the code above)
│
└── config/ # Configuration folder (required)
  ├── icon.png # App window icon (replace with your own image)
  └── count.txt # Save file storing death count


> ⚠️ **Important:**  
> The app requires a `config` folder in the same directory as your main script.  
> Inside it, you must have:
> - `icon.png` – used for the app window icon  
> - `count.txt` – used to store your death count (created automatically if missing)

---

## ⚙️ How It Works

- When the app starts, it looks for `config/count.txt`.  
  - If found, it loads your last saved death count.  
  - If not found, it starts at **0** and prints a warning in the console.
- Every time you press **+1**, the death count increases.
- Press **RESET** to set it back to 0.
- You can press **SAVE** manually anytime.
- When you close the window, it **automatically saves** the current count and then exits safely.

---

## 🧠 Error Handling

- If saving fails (e.g., `config` folder is missing or read-only),  
  the app prints: `⚠️ Could not save the file.`
- If loading fails (e.g., no `count.txt` exists yet),  
  the app prints: `⚠️ No save file found.`

These messages don’t stop the app — they’re just friendly warnings in the console.

---

## 🧰 Requirements

- Python 3.8+  
- Tkinter (included with most Python installations)

