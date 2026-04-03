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


