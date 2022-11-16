
import socket,sys,model,io
from PIL import Image

# creating socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print("Server is running")
server.bind((ip,8899))
server.listen(4)

# accepting the client request
client,address=server.accept()
print("Server is ready to accept data ...")
print("connected with client having",address)

# for binary data and io for input output operation 
# data is kept as bytes in an in memory buffer
file_stream=io.BytesIO()

image_data=client.recv(2048)
# writing the image data
while image_data:
    file_stream.write(image_data)
    image_data=client.recv(2048)
    if image_data==b'%DONE%' :
        break
# image converted
image=Image.open(file_stream)
filename=str(sys.argv[1])
# saving image
image.save(filename,format='png')

msg,accuracy=model.texts(filename)
# print(accuracy)
check=True
while check==True:
    # sending reply
    client.send(msg.encode('utf-8'))
    client.send(accuracy.encode('utf-8'))
    check=False
# closing the socket
client.close()


        
