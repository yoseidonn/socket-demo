# CLIENT
import socket

# Set the SERVER to your host friend's local IP which he tells you.
# and set the PORT to whatever you decide.

# Attention! You need to avoid using ports that are already in use.
# For example 80 port is used for internet (by your browser) so if you try to use 80,
# you'll get en error says "This port is already in use."
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

    # Connect to the server socket
    sock.connect(ADDR)
    
    # Print a message if you've connected succesfully,
    # It will stop the program until either it connects or fails.

    # If it fails, the try block will be skipped just like a break called,
    # and the finally block will work, the close() is to close the socket properly.
    # Otherwise you may get an error says "The port is on use" if you don't close the socket properly.
    
    # Now if it connects as the other case, the program will continue and print the message.
    print(f"Conneted to {ADDR[0]}:{ADDR[1]}")
    
    # Get an input (input() returns a str object by default) and decode it to bytes (01010001011)
    # If you don't specify a parameter to encode or decode functions, they will perform according to ASCII.
    
    # Just to know, you can decode a bytestring which is encoded using UTF-8 into string according to ASCII.
    # Because are compatible each other.
    
    send_msg = input("Enter a message to send: ").encode()

    # Send the bytes
    sock.send(send_msg)
    
    # Read from the line for 1024 bytes. Then decode it so you get a str.
    # This means your friend can't you send longer than 1024 bytes at first.
    # If you want to send something longer or don't wanna send empty string like "hello        ..." which has thousand empty bytes after hello.
    # You can first send the lenght of your message to the otherside then they can recieve the amount of bytes you said first.
    # But even in this method, you need to set a HEADER LENGHT which will by your custom protocol.
    # You can set it whatever you want. It's up to you.
    msg = sock.recv(1024).decode()

    # Print the message
    print(f"Server responded with: {msg}")
    
finally:
    # Wheter a error occurs or the code above runs perfectly, this block will run. 
    # So you will always close the socket properly either you got an error neither perform perfectly.
    sock.close()