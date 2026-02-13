from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO, emit
import sqlite3

app = Flask(__name__)
app.secret_key = "secretkey"


socketio = SocketIO(app)

def get_db():
    return sqlite3.connect("database.db")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if not username or not password:
            return "Please enter both username and password"

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT role, employee_id FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        db.close()

        if user:
            session["role"] = user[0]
            session["employee_id"] = user[1]

            if user[0] == "employee":
                return redirect("/employee")
            elif user[0] == "admin":
                return redirect("/admin")
            else:
                return redirect("/hr")

        return "Invalid Login"

    return render_template("login.html")


@app.route("/admin")
def admin():
    if "employee_id" not in session or session.get("role") != "admin":
        return redirect("/")

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT role, COUNT(*) FROM users GROUP BY role")
    user_stats = cur.fetchall()

    cur.execute("SELECT reward_type, COUNT(*) FROM rewards GROUP BY reward_type")
    reward_stats = cur.fetchall()

    cur.execute("SELECT COUNT(*) FROM rewards")
    total_rewards = cur.fetchone()[0]

    db.close()

    return render_template("admin_dashboard.html",
                           user_stats=user_stats,
                           reward_stats=reward_stats,
                           total_rewards=total_rewards)


@app.route("/hr")
def hr():
    if "employee_id" not in session or session.get("role") != "hr":
        return redirect("/")

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT reward_type, COUNT(*) FROM rewards GROUP BY reward_type")
    chart = cur.fetchall()

    cur.execute("SELECT COUNT(*) FROM rewards")
    total_rewards = cur.fetchone()[0]

    db.close()

    return render_template("hr_dashboard.html",
                           chart=chart,
                           total_rewards=total_rewards)


@app.route("/allocate", methods=["GET", "POST"])
def allocate():
    if "employee_id" not in session or session.get("role") != "hr":
        return redirect("/")

    if request.method == "POST":
        emp = request.form["employee_id"]
        reward = request.form["reward"]
        amount = request.form.get("amount", 0)

        db = get_db()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO rewards(employee_id,reward_type,amount,status) VALUES (?,?,?,?)",
            (emp, reward, amount, "Approved")
        )
        db.commit()
        db.close()

        
        socketio.emit("reward_added", {
            "employee_id": emp,
            "reward_type": reward,
            "amount": amount
        }, broadcast=True)

        return redirect("/hr")

    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT employee_id, username FROM users WHERE role=? ORDER BY employee_id", ("employee",))
    employees = cur.fetchall()
    db.close()

    return render_template("reward_allocation.html", employees=employees)



@socketio.on("connect")
def handle_connect():
    print("User Connected to Real-Time Server")


# 🔥 IMPORTANT: Use socketio.run instead of app.run
if __name__ == "__main__":
    socketio.run(app, debug=True)
