# import sqlite3

# def create_users_table(cursor):
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                     (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')

# def insert_user(cursor, email, password):
#     try:
#         cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
#         print(f"User with email '{email}' registered successfully.")
#         return True
#     except sqlite3.IntegrityError:
#         print(f"User with email '{email}' already exists.")
#         return False

# def display_users(cursor):
#     cursor.execute("SELECT email, logged_in FROM users")
#     users = cursor.fetchall()
#     print("Users:")
#     for user in users:
#         login_status = "Logged in" if user[1] == 1 else "Logged out"
#         print(f"Email: {user[0]}, Status: {login_status}")

# def main():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()

#     create_users_table(cursor)
#     display_users(cursor)

#     # Example: Register a new user
#     email = input("Enter email address: ")
#     password = input("Enter password: ")

#     # Attempt to insert the new user
#     insert_user(cursor, email, password)

#     # Commit changes and close connection
#     conn.commit()
#     conn.close()

# if __name__ == "__main__":
#     main()


import sqlite3
import ssl
import socket

def create_users_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')

def insert_user(cursor, email, password):
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        print(f"User with email '{email}' registered successfully.")
        return True
    except sqlite3.IntegrityError:
        print(f"User with email '{email}' already exists.")
        return False

def display_users(cursor):
    cursor.execute("SELECT email, logged_in FROM users")
    users = cursor.fetchall()
    print("Users:")
    for user in users:
        login_status = "Logged in" if user[1] == 1 else "Logged out"
        print(f"Email: {user[0]}, Status: {login_status}")

def main():
    # Create SSL context
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

    # Load SSL certificate and private key
    ssl_context.load_cert_chain(certfile='D:\Programming files\MinGW\Sem-4\Email-Systems\cert.pem', keyfile='D:\Programming files\MinGW\Sem-4\Email-Systems\key.pem')

    # Connect to SQLite database with SSL
    conn = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), ssl_version=ssl.PROTOCOL_TLS, cert_reqs=ssl.CERT_NONE)
    conn.connect(('127.0.0.1', 5000))

    cursor = conn.cursor()

    create_users_table(cursor)
    display_users(cursor)

    # Example: Register a new user
    email = input("Enter email address: ")
    password = input("Enter password: ")

    # Attempt to insert the new user
    insert_user(cursor, email, password)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
