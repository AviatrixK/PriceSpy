# 🛒 Price Spy — Minor Project (2024-25)

**Price Spy** is a lightweight web app designed to simplify online shopping by allowing users to compare real-time product prices across multiple e-commerce platforms. No more switching tabs, no more forgotten passwords — just quick, smart price comparison in one place.

---

## 🚀 Features

- 🔍 **Real-Time Price Comparison** from platforms like Snapdeal and Shopclues.
- 🧾 **No Sign-Ups or Passwords** — just email-based OTP login.
- ⚡ **Lightweight & Fast** — No database; fetches live data on demand.
- 📱 **Responsive UI** — Works on mobile, tablet, and desktop.
- 🔐 **Secure OTP Login** via SMTP.
- 🔧 **Scalable Architecture** — Easy to add more websites later.

---

## 🛠️ Tech Stack

| Frontend       | Backend        | Web Scraping     | Authentication  |
|----------------|----------------|------------------|------------------|
| HTML, CSS, JS  | Python, Flask  | BeautifulSoup    | SMTP (Email OTP) |

---

## 📂 Project Architecture

- **Frontend:** HTML + CSS for layout and styling, JavaScript for dynamic interactions.
- **Backend:** Flask routes handle user requests, scrape data, and return structured JSON.
- **Live Scraping:** No stored data; prices fetched in real-time using BeautifulSoup.
- **User Auth:** Email-based OTP login system using SMTP — no password storage.

---

## 📽️ Demo Video
> 🎥[ https://drive.google.com/drive/folders/1JwEqkGxQm5CkOEdQ9inxUYPwgiKjR47r
](https://drive.google.com/drive/folders/1JwEqkGxQm5CkOEdQ9inxUYPwgiKjR47r?usp=drive_link)
---

## 📊 Presentation Slides
> 📁 [https://docs.google.com/presentation/d/1xDb5y1HQ1-rmPK78P4ss4puxSxguR82LbiIeg8p1g3k/edit?usp=sharing](https://docs.google.com/presentation/d/1xDb5y1HQ1-rmPK78P4ss4puxSxguR82LbiIeg8p1g3k/edit?usp=sharing)

---

## 📌 Future Enhancements
- 🧠 Search history tracking and price trend analysis.
- 🔔 Stock alert notifications for out-of-stock items.

---

## 🙌 Made With

💻 Python • 🌐 Flask • 🧹 BeautifulSoup • 💌 SMTP • 🎨 HTML/CSS/JS

---

## 📞 Contact

**Developed by:** Kiruthika, Mayank Rawat  
🧑‍🎓 BSc (Hons.) Cybersecurity — Semester 2  
📫 Email: kiruthika.s0405@gmail.com  
📫 Email: mayank.r2409@gmail.com

---
**Steps to Run PriceSpy**
- Clone the repository using the command:
 git clone https://github.com/AviatrixK/PriceSpy.git
- Then navigate into the project directory:
 cd PriceSpy

- Create a virtual environment by running:
 python -m venv venv

- Activate the virtual environment:
 On Windows, use: venv\Scripts\activate
 On Linux/macOS, use: source venv/bin/activate

- Install the required dependencies using:
 pip install -r requirement.txt

- Set the Flask environment variables:
 On Windows (Command Prompt):
  set FLASK_APP=app.py
  set FLASK_ENV=development
 On Linux/macOS:
  export FLASK_APP=app.py
  export FLASK_ENV=development

- Finally, run the Flask application with:
 flask run

**Once the server starts, you can access the application by navigating to http://127.0.0.1:5000 in your web browser.**




