#import ssl
from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope,
   # (#open the socket , connect)

   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   # Fill in start2
   #servername = "smtp.gmail.com"
   #port= 465
   servername = "127.0.0.1"
   port = 1025
   # Fill in end5
   clientSocket = socket(AF_INET, SOCK_STREAM)
   #clientSocket = ssl.wrap_socket(clientSocket)
   clientSocket.connect((servername, port))
   # Fill in end5
   print("after opening socket ")
   recv = clientSocket.recv(1024).decode()
   print(recv)
   #print(" after receving connecion " + recv)


   if recv[:3] != '220':
       print('220 reply not received from server.')

   #end HELO command and print server response.
   heloCommand = 'HELO Najlaa \r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   # Fill in start
   mailFrom = "MAIL FROM:<nb3261@nyu.edu>\r\n"
   clientSocket.send(mailFrom.encode())
   # Fill in end
   recv2 = clientSocket.recv(1024)
   recv2 = recv2.decode()
   print("After MAIL FROM command: " + recv2)

   # Send RCPT TO command and print server response.
   # Fill in start
   rcptTo = "RCPT TO:<nb3216@nyu.edu>\r\n"
   clientSocket.send(rcptTo.encode())
   recv3 = clientSocket.recv(1024)
   recv3 = recv3.decode()
   # Fill in end


   # Fill in start
   print("After RCPT TO command: " + recv3)
   data = "DATA : I am Najlaa, sending a message \r\n"
   clientSocket.send(data.encode())
   recv4 = clientSocket.recv(1024)
   recv4 = recv4.decode()
   print("After DATA command: " + recv4)
   #Send DATA command and print server response.
   # Fill in end

   # Send message data.
   # Fill in start
   message = "how are you?"
   clientSocket.send(message.encode())
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   end_msg = "\r\n.\r\n"
   clientSocket.send(end_msg.encode())
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   quit = "QUIT\r\n"
   clientSocket.send(quit.encode())
   recv5 = clientSocket.recv(1024)
   print(recv5.decode())
   clientSocket.close()
   # Fill in end


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
