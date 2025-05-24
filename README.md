# 🔌 Flask MySQL Connection Template

A simple Flask + MySQL connection template designed for local development. Just follow the steps below to get started quickly.

## SETUP:
```bash
#1. Clone the repository
git clone https://github.com/BrianShiroe/flask-mysql-connection-template.git

#2. Access the project directory
cd flask-mysql-connection-template

#3. Check if python is installed
python --version

#4. If python is installed, proceed to #5. If python is not installed, install on this link.
https://www.python.org/downloads/

#5. Install required packages
pip install flask mysql-connector-python python-dotenv

#6. Create a .env file with MySQL configuration, and put these files
export DB_HOST=localhost        # Hostname of your MySQL server (usually 'localhost' for local development)
export DB_USER=root             # MySQL username (default is often 'root' unless changed)
export DB_PASS=password123      # MySQL password (set this to your actual MySQL password)
export DB_NAME=mydatabase       # Name of the database you want to connect to

#7. Run the Flask application
python app.py

#8. Open your browser and run the given server link in the terminal.
http://localhost:5000/getTable
```

### DONE!