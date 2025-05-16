from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# Создание БД
def init_db():
    conn = sqlite3.connect('vuln.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, name TEXT, comment TEXT)')
    conn.commit()
    conn.close()

init_db()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Vulnerable App</title>
</head>
<body>
    <h1>Leave a comment</h1>
    <form method="POST" action="/">
        Name: <input type="text" name="name"><br>
        Comment: <input type="text" name="comment"><br>
        <button type="submit">Submit</button>
    </form>

    <h2>Messages:</h2>
    {% for row in rows %}
        <b>{{ row[1] }}</b>: {{ row[2] | safe }}<br>
    {% endfor %}

    <hr>
    <h2>Run a system command (danger!)</h2>
    <form method="POST" action="/cmd">
        Command: <input type="text" name="cmd"><br>
        <button type="submit">Run</button>
    </form>
    {% if output %}
        <pre>{{ output }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        comment = request.form["comment"]
        # SQL Injection уязвимость
        conn = sqlite3.connect('vuln.db')
        c = conn.cursor()
        query = f"INSERT INTO messages (name, comment) VALUES ('{name}', '{comment}')"
        c.execute(query)
        conn.commit()
        conn.close()

    conn = sqlite3.connect('vuln.db')
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    rows = c.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, rows=rows)

@app.route("/cmd", methods=["POST"])
def cmd():
    command = request.form["cmd"]
    # Command Injection уязвимость
    output = os.popen(command).read()
    conn = sqlite3.connect('vuln.db')
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    rows = c.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, rows=rows, output=output)

if __name__ == "__main__":
    app.run(debug=True)
