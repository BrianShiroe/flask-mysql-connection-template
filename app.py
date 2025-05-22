from flask import Flask, jsonify, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# Database configuration (kept as you requested)
db_config = {
    'host': 'localhost',
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NAME'),
}

# Function to connect to MySQL
def get_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    # Redirect root URL to /getTable
    return redirect(url_for('get_tables'))

@app.route('/getTable', methods=['GET'])
def get_tables():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        table_names = [table[0] for table in tables]
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals() and con.is_connected():
            con.close()
    return jsonify({"tables": table_names}), 200

if __name__ == "__main__":
    print("Connecting to DB...")
    app.run(debug=True)
