# 💰 Expense Tracker Web App

A clean and simple web application for tracking personal expenses.  
Built using **Python**, **Flask**, **MySQL**, **Pandas**, and styled with **HTML/CSS**.

---

## 🚀 Features

- ➕ Add expenses (date, category, amount, note)
- 📋 View all expenses in a table
- 📤 Export data to CSV
- 📈 Generate monthly expense reports
- 💅 Styled with plain CSS (no Bootstrap)
- 🧠 Powered by Flask and MySQL

---

## 🧰 Technologies Used

| Tool         | Purpose                      |
|--------------|------------------------------|
| Python       | Core programming language    |
| Flask        | Web framework (backend)      |
| MySQL        | Database (stores expenses)   |
| Pandas       | Data analysis & CSV export   |
| HTML/CSS     | Frontend interface           |
| Jinja2       | Template engine for Flask    |

---

## 📂 Project Folder Structure

expense-tracker/
├── app.py # Main Flask app
├── templates/
│ ├── index.html # Homepage (add/view expenses)
│ └── report.html # Report page
├── static/
│ └── style.css # Custom styles
├── README.md # This file
└── requirements.txt # Python dependencies

---

## 🛠️ Setup Instructions (Run Locally)

### 🔧 Requirements
- Python 3.x
- MySQL server installed
- pip (Python package manager)

### ⚙️ Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/RamGenAi22/expense-tracker.git
   cd expense-tracker


Install dependencies


pip install -r requirements.txt
Set up MySQL

Open MySQL Workbench or CLI

Create a database named: expenses_db

Then run this SQL:

sql
Copy
Edit
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    category VARCHAR(255),
    amount FLOAT,
    note TEXT
);
Update DB credentials in app.py

python
Copy
Edit
conn = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="expenses_db"
)
Run the Flask app
python app.py


Open your browser
http://localhost:5000/

🧠 Future Improvements
🔐 Add user authentication (login/signup)

📊 Add graphs with Chart.js or Plotly

📅 Filter by custom dates or range

☁️ Deploy the app online

👤 Author
  SaiRam 
🔗 GitHub: @RamGenAi22

📄 License
This project is licensed for learning and personal use.