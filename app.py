from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

# Database configuration
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NAME'),
}

def get_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def all_tables():
    table_data = []
    error = None
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        for table in tables:
            name = table[0]
            cursor.execute(f"SELECT * FROM `{name}`")
            rows = cursor.fetchall()
            cols = [desc[0] for desc in cursor.description]
            table_data.append({
                "name": name,
                "columns": cols,
                "rows": rows
            })
    except mysql.connector.Error as err:
        error = str(err)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals() and con.is_connected():
            con.close()

    return render_template("index.html", tables=table_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
