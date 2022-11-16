# Pseudocode


# for model.py
Make a function which returns the recognized texts from image and takes an argument as image file:
    Define the lang to be recognized .
    Read the file to obtain the tuple containing the coordinates, text and accuracy using easyocr.
    Set the coordinates.
    Read the file using cv2 as image.
    To mark the text iterate through the coordinates. 
    Make rectangle on the recognized text passing arguments image ,x and y coordinates ,color of border and width of border
    Now iterate the tuple and add only the text in empty string and return that string.
    Use matplotlib to show the recognized text from image by marking them.
    *import all library that are needed*

# for server.py
Create socket for TCP Connection (SOCK_STREAM)
Get ip
Bind socket to a specific port and IP where clients can contact server
Listen for client connection 
Accept the client connection 
open the file in binary write mode (for recognizing the text)
Loop and receive the image_data in binary form from client 
Write the image data in opened file 
Close the file
Now got the image so use model.py to recognize the text from the image
Send the return (Which is text and accuracy) value of model.py to client 
*import all needed libraries*
Close Socket

# for client.py
Create Socket for TCP Connection (SOCK_STREAM)
Get Ip
Connect to Server's address 
Open file in binary read mode
Read file 
Loop and send all the binary data to server 
close the file
Now Receive recognized text from server using loop.
Decode the message 
Print the message in form of Table with Text and Accuracy as Heading
*import all needed libraries*
Close Socket
