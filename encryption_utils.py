from cryptography.fernet import Fernet
import os

# In a real cloud app, you'd store this in AWS Secrets Manager or a .env file
# For now, we generate one. Keep this key safe!
SECRET_KEY = Fernet.generate_key() 
cipher = Fernet(SECRET_KEY)

def encrypt_data(plain_text):
    return cipher.encrypt(plain_text.encode()).decode()

def decrypt_data(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()
