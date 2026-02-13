import sqlite3

def init_database():
    """Initialize the database with required tables"""
    db = sqlite3.connect("database.db")
    cur = db.cursor()
    
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            employee_id TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            reward_type TEXT NOT NULL,
            amount INTEGER DEFAULT 0,
            status TEXT NOT NULL,
            date_allocated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    
    try:
        
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("rajesh_kumar", "password123", "EMP001", "employee"))
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("priya_sharma", "password123", "EMP002", "employee"))
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("amit_patel", "password123", "EMP003", "employee"))
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("neha_gupta", "password123", "EMP004", "employee"))
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("vikram_singh", "password123", "EMP005", "employee"))
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("deepa_nair", "password123", "EMP006", "employee"))
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("akshay_desai", "password123", "EMP007", "employee"))
        
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("sandhya_hr", "password123", "HR001", "hr"))
        cur.execute("INSERT INTO users (username, password, employee_id, role) VALUES (?, ?, ?, ?)", 
                   ("admin_user", "admin123", "ADMIN001", "admin"))
        db.commit()
        print("✓ Sample users created")
    except sqlite3.IntegrityError:
        print("✓ Users already exist")
    
    
    try:
        
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP001", "Performance Bonus", 8000, "Approved"))
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP002", "Excellence Award", 6000, "Approved"))
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP003", "Innovation Prize", 7500, "Approved"))
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP004", "Team Player Badge", 5000, "Approved"))
        
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP005", "Project Completion Bonus", 9000, "Approved"))
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP006", "Customer Satisfaction Award", 6500, "Approved"))
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP001", "Leadership Prize", 7000, "Approved"))
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP002", "Attendance Bonus", 3000, "Approved"))
        
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP007", "Performance Bonus", 8500, "Approved"))
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP003", "Mentorship Award", 5500, "Approved"))
        cur.execute("INSERT INTO rewards (employee_id, reward_type, amount, status) VALUES (?, ?, ?, ?)", 
                   ("EMP004", "Quality Excellence", 7000, "Approved"))
        db.commit()
        print("✓ Sample rewards data created")
    except sqlite3.IntegrityError:
        print("✓ Rewards data already exists")
    
    db.close()
    print("✓ Database initialized successfully!")

if __name__ == "__main__":
    init_database()
