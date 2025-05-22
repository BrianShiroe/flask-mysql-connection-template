## simple Flask with mysql connection template

## SETUP:
1. Install required packages:
```bash
pip install flask mysql-connector-python
```

2. Create a .env file

3. In your .env, rewrite this with your mysql information.
```bash
export DB_HOST=localhost        # Hostname of your MySQL server (usually 'localhost' for local development)
export DB_USER=root             # MySQL username (default is often 'root' unless changed)
export DB_PASS=password123      # MySQL password (set this to your actual MySQL password)
export DB_NAME=mydatabase       # Name of the database you want to connect to
```

4. Run your Flask app:
```bash
python app.py
```

5. Open your browser and run the given link in the terminal. ex.
```bash
http://localhost:5000/getTable
```