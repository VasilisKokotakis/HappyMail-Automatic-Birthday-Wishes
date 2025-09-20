---

# 🎉 HappyMail – Your Automated Birthday Buddy 🎂💌

Never miss a birthday again! **HappyMail** sends personalized birthday emails automatically—so you can be the hero of birthdays without even trying. 🦸‍♂️✨

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python) ![License](https://img.shields.io/badge/License-MIT-green)

---

## 🛠 Features

* 🎈 **Automatic Birthday Emails** – Sends wishes on the right day.
* ✨ **Personalized Templates** – `[NAME]` is replaced automatically.
* 🎁 **Randomized Letters** – Keep it fresh with multiple templates.
* 👯 **Multiple Birthdays Supported** – Celebrate everyone!
* ⚡ **Easy Setup** – Just CSV + templates + run.

---

## 📂 Setup

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/happymail.git
cd happymail
```

2. **Install dependencies**

```bash
pip install pandas
```

3. **Add birthdays** in `birthdays.csv` with columns: `name`, `email`, `month`, `day`.

4. **Add letter templates** in `letter_templates/` (e.g., `letter_1.txt`, `letter_2.txt`).

5. **Configure email** in the script (or use environment variables for safety 🔒).

6. **Run it**

```bash
python send_birthday_email.py
```

---

## 📝 Example

**birthdays.csv**

| name  | email                                     | month | day |
| ----- | ----------------------------------------- | ----- | --- |
| Alice | [alice@email.com](mailto:alice@email.com) | 9     | 20  |
| Bob   | [bob@email.com](mailto:bob@email.com)     | 12    | 5   |

**letter\_1.txt**

```
Happy Birthday, [NAME]!
Wishing you a magical day full of joy and surprises! 🎉🎂
```

---

## ⏰ Bonus: Automate Daily

* **Linux/macOS:** Use `cron` to run daily
* **Windows:** Use Task Scheduler

---

## 💡 Tips

* Use a **Gmail App Password** if you have 2FA enabled.
* Add **more templates** to surprise your friends every year.
* Keep your email credentials **secure**!

---

## 🤝 Contributing

Add templates, suggest features, or fix bugs! Pull requests welcome. Let’s make birthdays unforgettable. 🎊

---

## 📬 License

MIT License – celebrate freely! 🎈

