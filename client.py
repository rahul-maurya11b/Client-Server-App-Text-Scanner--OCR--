
import socket,sys
from prettytable import PrettyTable
# creating socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
# connecting the client
client.connect((ip,8899))
print("client conected")


# read binary data from image file
file=open(sys.argv[1],'rb')
image_data=file.read(2048)

# send image data to server
while image_data :
    client.send(image_data)
    image_data=file.read(2048)
# closing the file
file.close()
# condition for loop exit
client.send(b"%DONE%")
check=True
# receiving the data
while(check==True):
    msg=client.recv(1024)
    accuracy=client.recv(1024)
    check=False
# making the text in list form 
real_text=msg.decode('utf-8')
msg=(msg.decode('utf-8')).strip()
msg=msg.split(" ")
accuracy=(accuracy.decode('utf-8')).strip()
accuracy=accuracy.split(" ")


# for only text
print("****************************************************************")
print("Result of text Recognition is:\n")
print("****************************************************************")
print(real_text)
print("****************************************************************")
# for table form
print("Result in Table form")

# making table 
myTable = PrettyTable(["Text", "Accuracy"])
for i in range(len(msg)):
    try:
        myTable.add_row([msg[i], accuracy[i]])
    except:
        IndexError
print(myTable)

# closing the sockt 
client.close()

    
