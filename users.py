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

# import sqlite3
# import ssl
# import socket

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
#     # Create SSL context
#     ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

#     # Load SSL certificate and private key
#     ssl_context.load_cert_chain(certfile='D:\Programming files\MinGW\Sem-4\Email-Systems\cert.pem', keyfile='D:\Programming files\MinGW\Sem-4\Email-Systems\key.pem')

#     # Connect to server with SSL
#     with socket.create_connection(('10.1.19.255', 5000)) as sock:
#         with ssl_context.wrap_socket(sock, server_hostname='10.1.19.255') as ssock:
#             cursor = ssock.makefile('rwb')
#             cursor = sqlite3.connect('users.db').cursor()

#             create_users_table(cursor)
#             display_users(cursor)

#             # Example: Register a new user
#             email = input("Enter email address: ")
#             password = input("Enter password: ")

#             # Attempt to insert the new user
#             insert_user(cursor, email, password)

#             # Commit changes and close connection
#             cursor.connection.commit()
#             cursor.connection.close()

# if __name__ == "__main__":
#     main()


# import sqlite3
# import ssl
# import socket

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
#     # Create SSL context
#     ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

#     # Load SSL certificate and private key
#     ssl_context.load_cert_chain(certfile='D:\Programming files\MinGW\Sem-4\Email-Systems\cert.pem', keyfile='D:\Programming files\MinGW\Sem-4\Email-Systems\key.pem')

#     # Connect to server with SSL
#     with socket.create_connection(('10.1.19.255', 5000)) as sock:
#         with ssl_context.wrap_socket(sock, server_hostname='10.1.19.255') as ssock:
#             cursor = ssock.makefile('rwb')
#             cursor = sqlite3.connect('users.db').cursor()

#             create_users_table(cursor)
#             display_users(cursor)

#             # Example: Register a new user
#             email = input("Enter email address: ")
#             password = input("Enter password: ")

#             # Attempt to insert the new user
#             insert_user(cursor, email, password)

#             # Commit changes and close connection
#             cursor.connection.commit()
#             cursor.connection.close()

# if __name__ == "__main__":
#     main()


import sqlite3
import ssl
import socket

def create_tables(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS emails
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, recipient TEXT, subject TEXT, body TEXT)''')

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
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

    # Disable certificate verification
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Connect to server with SSL
    server_ip = '192.168.143.8'  # Replace this with the actual IP address of the server
    server_port = 5000  # Replace this with the actual port of the server

    with socket.create_connection((server_ip, server_port)) as sock:
        with ssl_context.wrap_socket(sock, server_hostname=server_ip) as ssock:
            cursor = ssock.makefile('rwb')
            cursor = sqlite3.connect('users.db').cursor()

            create_users_table(cursor)
            display_users(cursor)

            # Example: Register a new user
            email = input("Enter email address: ")
            password = input("Enter password: ")

            # Attempt to insert the new user
            insert_user(cursor, email, password)

            # Commit changes and close connection
            cursor.connection.commit()
            cursor.connection.close()

if __name__ == "__main__":
    main()
