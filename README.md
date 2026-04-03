🛡️ Data Leak Prevention System using SQL Injection Detection
A secure, cloud-accessible web application designed to prevent data leaks through a Double-Layer Security Protocol. Built as part of an Internship Project focusing on Cloud Computing and Cybersecurity.

🚀 Features
Layer 1: Parameterized Queries – Blocks SQL Injection (SQLi) by separating code from user-provided data.

Layer 2: AES-256 Encryption – Uses symmetric-key encryption to scramble sensitive information (emails/credentials) before storing them in the database.

Cloud Tunneling – Accessible over the internet via a secure reverse proxy (Serveo/Localtunnel).

Lightweight Architecture – Designed for high performance without heavy system requirements.

🛠️ Tech Stack
Language: Python 3.x

Framework: Flask

Security: Cryptography (Fernet/AES-256)

Database: SQLite3 (Local) / Cloud-ready

Deployment: Serveo (SSH Tunneling)

📂 Project Structure
Plaintext
/data-leak-detection-project
│── app.py              # Backend logic & SQLi prevention
│── encryption_utils.py # AES-256 encryption/decryption logic
│── users.db            # Secure encrypted database
│── templates/          # Frontend UI
│   └── login.html      # Secure data entry form
└── README.md           # Project documentation

⚙️ How to Run Locally
Clone the repository:

Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install dependencies:

Bash
pip install flask cryptography
Start the Flask server:

Bash
python app.py
Expose to the Cloud (Internet):
Open a second terminal and run:

Bash
ssh -R 80:localhost:5000 serveo.net
🔒 Security Verification
To verify the AES-256 encryption, you can query the database directly. Notice that the sensitive fields are unreadable:

SQL
SELECT username, email FROM users;
-- Result: Arun, gAAAAABmB7... (Encrypted)