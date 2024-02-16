import socket
import threading

# Define a function to mimic a service
def fake_service(port, message):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port and listen for connections
        s.bind(('', port))
        s.listen(5)
        print(f"Listening on port {port}...")
        
        while True:
            conn, addr = s.accept()
            print(f"Received connection from {addr} on port {port}")
            # Send a fake banner or message
            conn.send(message.encode())
            # Close the connection
            conn.close()
    except Exception as e:
        print(f"Error on port {port}: {e}")

# List of ports and fake messages to use
ports_messages = [
    (1000, "SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2"),
    (2000, "220 FTP Server ready."),
    (3000, "220 ProFTPD 1.3.5 Server (Debian)"),
    (4000, "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>Fake Web Server</body></html>\r\n"),
    (5000, "220 ESMTP Postfix"),
    (6000, "MySQL server version 5.7.27-0ubuntu0.18.04.1"),
    (7000, "220 Microsoft ESMTP MAIL Service"),
    (8000, "Nmap"),
    (9000, "SMB Service"),
    (10000, "220 IMAP server ready"),
]

threads = []

# Start a thread for each port
for port, message in ports_messages:
    thread = threading.Thread(target=fake_service, args=(port, message))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
