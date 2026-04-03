from flask import Flask, request, render_template, session
import sqlite3
from encryption_utils import encrypt_data # Ensure this matches your file name!

app = Flask(__name__)
app.secret_key = "super_secret_session_key"

# --- ADD THIS NEW SECTION TO FIX THE 404 ---
@app.route('/')
def home():
    # This looks for 'login.html' inside your 'templates' folder
    return render_template('login.html') 
# -------------------------------------------

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    # LAYER 1: Encrypted sensitive info (AES-256)
    email_input = request.form['email']
    encrypted_email = encrypt_data(email_input)
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # LAYER 2: Parameterized Query
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                       (username, encrypted_email, password))
        conn.commit()
        return "User registered securely! Check your 'users.db' to see the AES-256 encryption."
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
    # Create the table if it doesn't exist
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, email TEXT, password TEXT)')
    conn.close()
    app.run(debug=True)