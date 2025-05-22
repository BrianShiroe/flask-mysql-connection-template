from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NAME', 'mydatabase')
}

# Function to connect to MySQL
def get_connection():
    return mysql.connector.connect(**db_config)

@app.route('/getTable', methods=['GET'])
def get_tables():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    con.close()
    table_names = [table[0] for table in tables]
    return jsonify({"tables": table_names}), 200

if __name__ == "__main__":
    print("Connecting to DB...")
    app.run(debug=True)
