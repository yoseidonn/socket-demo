# SERVER
import socket

# Set SERVER to you local IP with provided methods by socket lib,
# and choose a port to run on.  

# You can first run only the line 8 to learn your local IP and print it.
# So you can share it will your friend.
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9995

# Imagine ADDR as 192.168.1.20:9995 but in a tuple form,
# just because the socket functions takes tuple.
ADDR = (SERVER, PORT)

try:
    # Create a socket object that uses IPv4 (AF_INET family) and uses TCP (SOCK_STREAM)
    # Don't think about that family and type parameters, just memorize or check the documentation
    # if you want to learn more. I've choosed them as our needs.
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # Set your server socket to your ADDR
    sock.bind(ADDR)

    # If you're able to bind that ADDR succesfully, you will start listening for new connections.
    # sock.connect(ADDR) on the client side !
    sock.listen()
    
    # If there is a connection, program will proceed to next lines,
    # then listening message will occure.
    print(f"Server listening on {SERVER}:{PORT}")
    
    # Now there is a connection so you need to accept it.
    # accept methods gives you a socket object of your friend (conn stand for connection),
    # So you can use all the socket methods on conn variable. 
    
    # addr will be a tuple like (IP, NUMBER)
    # IP is a string which is your friends local IP,
    # NUMBER is a random unique number that socket lib gives your friends connection like an ID.
    conn, addr = sock.accept()
    print(f"Connection accepted: {addr[0]}:{addr[1]}")
    
    # Now read his message and decode.
    # recv method will wait until your friend will send a message.
    # When there is something to read, recv will proceed.
    msg = conn.recv(1024).decode()
    print(f"Message recieved from client: {msg}")

    # Take an input to send back if you want and encode it
    send_msg = input("Enter a response message: ").encode()
    
    # As I said, conn is a representation of your friends socket, so you can use send method
    # just like your friend used on client-side. <server_socket>.send()
    conn.send(send_msg)
    
finally:
    # Wheter a error occurs or the code above runs perfectly, this block will run. 
    # So you will always close the socket properly either you got an error neither perform perfectly.
    sock.close()