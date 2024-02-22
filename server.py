# import socket
# import sqlite3
# import signal
# import sys
# import ssl

# # Define server address and port
# SERVER_HOST = '127.0.0.1'
# SERVER_PORT = 5000
# CERTFILE = 'Email-Systems\cert.pem'
# KEYFILE = 'Email-Systems\key.pem'

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Allow socket reuse and bind to the server address and port
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.bind((SERVER_HOST, SERVER_PORT))

# # Listen for incoming connections
# server_socket.listen(5)
# print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# # Connect to SQLite database
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()

# # Create a table to store users (if not exists)
# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                 (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')

# # Create a table to store emails (if not exists)
# cursor.execute('''CREATE TABLE IF NOT EXISTS emails
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, recipient TEXT, subject TEXT, body TEXT)''')

# def signal_handler(sig, frame):
#     print('\nGracefully shutting down the server...')
#     server_socket.close()
#     sys.exit(0)

# # Register the signal handler for graceful termination
# signal.signal(signal.SIGINT, signal_handler)

# # Function to authenticate users
# def authenticate(email, password):
#     cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#     user = cursor.fetchone()
#     if user:
#         cursor.execute("UPDATE users SET logged_in = 1 WHERE email=?", (email,))
#         conn.commit()
#     return user is not None

# # Function to retrieve emails for a user
# def get_emails(recipient):
#     cursor.execute("SELECT * FROM emails WHERE recipient=?", (recipient,))
#     emails = cursor.fetchall()
#     return emails

# # Main server loop
# while True:
#     try:
#         # Accept incoming connections
#         client_socket, client_address = server_socket.accept()
#         print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

#         # Receive data from client (authentication)
#         auth_data = client_socket.recv(1024).decode()

#         # Check if the received data contains both email and password
#         if "|" not in auth_data:
#             client_socket.sendall(b"Invalid authentication data.")
#             client_socket.close()
#             continue

#         email, password = auth_data.split("|")

#         # Authenticate user
#         if authenticate(email, password):
#             # Send authentication response
#             client_socket.sendall(b"Authentication successful. You are logged in.")

#             # Receive data from client (operation)
#             operation = client_socket.recv(1024).decode()

#             if operation == "SEND_EMAIL":
#                 # Receive data from client (email)
#                 email_data = client_socket.recv(1024).decode()
#                 sender, recipient, subject, body = email_data.split("|")
               
#                 # Process received data (assuming it's an email)
#                 # Store the email in the database or send to recipient's inbox (in a real system)
#                 print(f"Received email from {sender} to {recipient}")
#                 client_socket.sendall(b"Email received by the server. Thank you!")
#                 # Store email in a database table (if needed)
#                 cursor.execute("INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)",
#                                (sender, recipient, subject, body))
#                 conn.commit()
#             elif operation == "READ_EMAILS":
#                 # Read emails for the logged-in user
#                 emails = get_emails(email)
#                 if emails:
#                     email_list = "\n".join([f"From: {email[1]}\nSubject: {email[3]}\n{email[4]}\n" for email in emails])
#                     client_socket.sendall(email_list.encode())
#                 else:
#                     client_socket.sendall(b"No emails found.")
#         else:
#             client_socket.sendall(b"Authentication failed. Please check your email and password.")
       
#         # Close the connection
#         client_socket.close()
#     except Exception as e:
#         print("An error occurred:", e)


# import socket
# import ssl
# import sqlite3
# import signal
# import sys

# SERVER_HOST = '127.0.0.1'
# SERVER_PORT = 5000
# CERTFILE = 'Email-Systems\cert.pem'  # Path to your server certificate
# KEYFILE = 'Email-Systems\key.pem'    # Path to your server private key
# DATABASE = 'users.db'

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.bind((SERVER_HOST, SERVER_PORT))
# server_socket.listen(5)

# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

# print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# # Connect to SQLite database
# conn = sqlite3.connect(DATABASE)
# cursor = conn.cursor()

# # Create a table to store users (if not exists)
# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                 (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')

# # Create a table to store emails (if not exists)
# cursor.execute('''CREATE TABLE IF NOT EXISTS emails
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, recipient TEXT, subject TEXT, body TEXT)''')


# def signal_handler(sig, frame):
#     print('\nGracefully shutting down the server...')
#     server_socket.close()
#     sys.exit(0)


# signal.signal(signal.SIGINT, signal_handler)


# def authenticate(email, password):
#     cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#     user = cursor.fetchone()
#     if user:
#         cursor.execute("UPDATE users SET logged_in = 1 WHERE email=?", (email,))
#         conn.commit()
#     return user is not None


# def get_emails(recipient):
#     cursor.execute("SELECT * FROM emails WHERE recipient=?", (recipient,))
#     emails = cursor.fetchall()
#     return emails


# def handle_client_connection(client_socket):
#     with context.wrap_socket(client_socket, server_side=True) as ssl_socket:
#         print(f"[*] Accepted connection from {ssl_socket.getpeername()[0]}:{ssl_socket.getpeername()[1]}")

#         try:
#             auth_data = ssl_socket.recv(1024).decode()
#             if "|" not in auth_data:
#                 ssl_socket.sendall(b"Invalid authentication data.")
#                 ssl_socket.close()
#                 return

#             email, password = auth_data.split("|")

#             if authenticate(email, password):
#                 ssl_socket.sendall(b"Authentication successful. You are logged in.")

#                 operation = ssl_socket.recv(1024).decode()

#                 if operation == "SEND_EMAIL":
#                     email_data = ssl_socket.recv(1024).decode()
#                     sender, recipient, subject, body = email_data.split("|")

#                     print(f"Received email from {sender} to {recipient}")
#                     ssl_socket.sendall(b"Email received by the server. Thank you!")

#                     cursor.execute("INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)",
#                                    (sender, recipient, subject, body))
#                     conn.commit()

#                 elif operation == "READ_EMAILS":
#                     emails = get_emails(email)
#                     if emails:
#                         email_list = "\n".join(
#                             [f"From: {email[1]}\nSubject: {email[3]}\n{email[4]}\n" for email in emails])
#                         ssl_socket.sendall(email_list.encode())
#                     else:
#                         ssl_socket.sendall(b"No emails found.")
#             else:
#                 ssl_socket.sendall(b"Authentication failed. Please check your email and password.")

#         except Exception as e:
#             print("An error occurred:", e)
#         finally:
#             ssl_socket.close()


# while True:
#     client_socket, client_address = server_socket.accept()
#     handle_client_connection(client_socket)


# import socket
# import ssl
# import sqlite3
# import signal
# import sys

# SERVER_HOST = '127.0.0.1'
# SERVER_PORT = 5000
# CERTFILE = 'D:/Programming files/MinGW/Sem-4/Email-Systems/cert.pem'
# KEYFILE = 'D:/Programming files/MinGW/Sem-4/Email-Systems/key.pem'
# DATABASE = 'users.db'

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.bind((SERVER_HOST, SERVER_PORT))
# server_socket.listen(5)

# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

# print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# # Connect to SQLite database
# conn = sqlite3.connect(DATABASE)
# cursor = conn.cursor()

# # Create a table to store users (if not exists)
# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                 (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')

# # Create a table to store emails (if not exists)
# cursor.execute('''CREATE TABLE IF NOT EXISTS emails
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, recipient TEXT, subject TEXT, body TEXT)''')

# # Signal handler for graceful shutdown
# def signal_handler(sig, frame):
#     print('\nGracefully shutting down the server...')
#     server_socket.close()
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)

# def authenticate(email, password):
#     cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#     user = cursor.fetchone()
#     if user:
#         cursor.execute("UPDATE users SET logged_in = 1 WHERE email=?", (email,))
#         conn.commit()
#     return user is not None

# def get_emails(recipient):
#     cursor.execute("SELECT * FROM emails WHERE recipient=?", (recipient,))
#     emails = cursor.fetchall()
#     return emails
# def handle_client_connection(client_socket):
#     try:
#         with context.wrap_socket(client_socket, server_side=True) as ssl_socket:
#             print(f"[*] Accepted connection from {ssl_socket.getpeername()[0]}:{ssl_socket.getpeername()[1]}")

#             auth_data = ssl_socket.recv(1024).decode()
#             if "|" not in auth_data:
#                 ssl_socket.sendall(b"Invalid authentication data.")
#                 ssl_socket.close()
#                 return

#             email, password = auth_data.split("|")

#             if authenticate(email, password):
#                 ssl_socket.sendall(b"Authentication successful. You are logged in.")

#                 operation = ssl_socket.recv(1024).decode()

#                 if operation == "SEND_EMAIL":
#                     handle_send_email(ssl_socket)  # Call the new function to handle sending emails

#                 elif operation == "READ_EMAILS":
#                     # Read emails for the logged-in user
#                     emails = get_emails(email)
#                     if emails:
#                         email_list = "\n".join(
#                             [f"From: {email[1]}\nSubject: {email[3]}\n{email[4]}\n" for email in emails])
#                         ssl_socket.sendall(email_list.encode())
#                     else:
#                         ssl_socket.sendall(b"No emails found.")
#             else:
#                 ssl_socket.sendall(b"Authentication failed. Please check your email and password.")

#     except Exception as e:
#         print("An error occurred:", e)
#     finally:
#         client_socket.close()
# while True:
#     client_socket, client_address = server_socket.accept()
#     handle_client_connection(client_socket)

import socket
import ssl
import sqlite3
import signal
import sys

SERVER_HOST = '192.168.143.8'
SERVER_PORT = 5000
CERTFILE = 'D:/Programming files/MinGW/Sem-4/Email-Systems/cert.pem'
KEYFILE = 'D:/Programming files/MinGW/Sem-4/Email-Systems/key.pem'
DATABASE = 'users.db'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# Connect to SQLite database
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Create a table to store users (if not exists)
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')

# Create a table to store emails (if not exists)
cursor.execute('''CREATE TABLE IF NOT EXISTS emails
                (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, recipient TEXT, subject TEXT, body TEXT)''')

# Signal handler for graceful shutdown
def signal_handler(sig, frame):
    print('\nGracefully shutting down the server...')
    server_socket.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def authenticate(email, password):
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    if user:
        cursor.execute("UPDATE users SET logged_in = 1 WHERE email=?", (email,))
        conn.commit()
    return user is not None

def get_emails(recipient):
    cursor.execute("SELECT * FROM emails WHERE recipient=?", (recipient,))
    emails = cursor.fetchall()
    return emails

def handle_send_email(ssl_socket):
    email_data = ssl_socket.recv(1024).decode()
    sender, recipient, subject, body = email_data.split("|")

    print(f"Received email from {sender} to {recipient}")
    # print(f"Subject: {subject}")
    # print(f"Message: {body}")

    cursor.execute("INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)",
                   (sender, recipient, subject, body))
    conn.commit()

    ssl_socket.sendall(b"Email received by the server. Thank you!")

def handle_client_connection(client_socket):
    try:
        with context.wrap_socket(client_socket, server_side=True) as ssl_socket:
            print(f"[*] Accepted connection from {ssl_socket.getpeername()[0]}:{ssl_socket.getpeername()[1]}")

            auth_data = ssl_socket.recv(1024).decode()
            if "|" not in auth_data:
                ssl_socket.sendall(b"Invalid authentication data.")
                ssl_socket.close()
                return

            email, password = auth_data.split("|")

            if authenticate(email, password):
                ssl_socket.sendall(b"Authentication successful. You are logged in.")

                operation = ssl_socket.recv(1024).decode()

                if operation == "SEND_EMAIL":
                    handle_send_email(ssl_socket)

                elif operation == "READ_EMAILS":
                    emails = get_emails(email)
                    if emails:
                        email_list = "\n".join(
                            [f"From: {email[1]}\nSubject: {email[3]}\n{email[4]}\n" for email in emails])
                        ssl_socket.sendall(email_list.encode())
                    else:
                        ssl_socket.sendall(b"No emails found.")
            else:
                ssl_socket.sendall(b"Authentication failed. Please check your email and password.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    handle_client_connection(client_socket)
