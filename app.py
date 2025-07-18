from flask import Flask, render_template, redirect, url_for, request, Response
import mysql.connector
import os
from dotenv import load_dotenv
import pandas as pd 

load_dotenv()

app = Flask(__name__)

conn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)

@app.route("/", methods=["GET","POST"])

def index():
    cursor = conn.cursor()

    if request.method=="POST":
        date= request.form["date"]
        category = request.form["category"]
        amount = float(request.form["amount"])
        note = request.form["note"]

        cursor.execute(
            "INSERT INTO expenses (date,category,amount,note) VALUES (%s,%s,%s,%s)",(date,category,amount,note)
        )

        conn.commit()

        return redirect("/")
    
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")

    expenses = cursor.fetchall()

    from datetime import datetime
    current_month = datetime.now().month
    current_year = datetime.now().year

    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE MONTH(date)= %s AND YEAR(date)=%s",(current_month,current_year)
    )
    total_this_month = cursor.fetchone()[0] or 0.00

    cursor.close()

    return render_template("index.html", expenses=expenses, total_this_month=total_this_month)

@app.route("/report")
def report():
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) as total FROM expenses GROUP BY category ORDER BY total DESC")

    category_totals = cursor.fetchall()

    cursor.close()

    return render_template("report.html", category_totals=category_totals)


@app.route("/download")
def download_csv():
    cursor = conn.cursor()

    cursor.execute("SELECT date, category, amount, note FROM expenses ORDER BY date DESC")

    rows = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(rows, columns=['date','category','amount','note'])

    csv_data = df.to_csv(index=False)

    return Response(
        csv_data,
        mimetype='text/csv',
        headers={"Content-deposition":"attachment ; filename= expenses.csv"}
    )


    

if __name__ == '__main__':
    app.run(debug=True)
