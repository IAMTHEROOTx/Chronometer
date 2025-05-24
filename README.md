# Chronometer

**Chronometer** is a simple countdown timer written in Python. It allows the user to define a duration in seconds and an interval between each countdown tick. The timer then counts down and displays the remaining time in the terminal.

---

## 🎯 Purpose

This script was created as a lightweight tool to practice Python basics such as loops, user input, and the `time.sleep()` function. It can be used as a minimal terminal-based timer for personal tasks or exercises.

---

## 👤 Author

Made by **IAMTHEROOTx**

---

## 🧩 Features

- Set a countdown duration (in seconds).
- Set a custom interval between countdown messages.
- Clear, interactive terminal output.
- Graceful start and finish messages.

---

## 🛠️ How to Run

Make sure Python is installed on your system.

1. Save the code in a file, for example: `chronometer.py`
2. Open your terminal or command prompt.
3. Run the program with:

```bash
python chronometer.py
```

---

## 📝 Example Usage

```text
WELCOME IN MINUTOR
IAMTHEROOTx made this script
You ready to start the minutor: yes
Enter a time in seconds: 5
Enter an interval of seconds between each secondes: 1
MINUTOR ON
Il vous manque 5 secondes.
Il vous manque 4 secondes.
Il vous manque 3 secondes.
Il vous manque 2 secondes.
Il vous manque 1 secondes.
The time is done!!!
```

---

## ⚠️ Code Note

There is a small logic issue in the input condition:

```python
if start == "Yes" or "yes" or "YES":
```

This condition will **always be true**. To fix it, use:

```python
if start.lower() == "yes":
```

This ensures that any case variation of "yes" will trigger the countdown properly.

---

## 📜 License

This project is open-source and may be used freely for learning and personal use. Redistribution or malicious use is discouraged.
