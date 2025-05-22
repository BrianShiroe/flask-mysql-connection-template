# 🔌 Flask MySQL Connection Template

A simple Flask + MySQL connection template designed for local development. Just follow the steps below to get started quickly.

## SETUP:
1. clone the repository.
```bash
#Input this in your terminal
git clone https://github.com/BrianShiroe/flask-mysql-connection-template.git

# access the folder path
cd flask-mysql-connection-template
```

2. Install required packages:
```bash
# library and framework used for the project
pip install flask mysql-connector-python
```

3. Create a .env file

4. In your .env, rewrite this with your mysql information.
```bash
export DB_HOST=localhost        # Hostname of your MySQL server (usually 'localhost' for local development)
export DB_USER=root             # MySQL username (default is often 'root' unless changed)
export DB_PASS=password123      # MySQL password (set this to your actual MySQL password)
export DB_NAME=mydatabase       # Name of the database you want to connect to
```

5. Run your Flask app:
```bash
python app.py
```

6. Open your browser and run the given server link in the terminal.
```bash
http://localhost:5000/getTable
```

### DONE!