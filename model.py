import easyocr
import matplotlib.pyplot as plt
import cv2
import easyocr

def texts(file):
   
    # actual model working
    reader = easyocr.Reader(['en'])
    # results =tuple containing x and y coordinates ,text and accuracy of the recognition
    results = reader.readtext(file)

    # now for marking the text and showing the image with marks
    # cord = results[-1][0]
    image = cv2.imread(file)
    for (cord,text,accuracy) in results:
        # cooridinates of the text
        (x1, x2, y1, y2) = cord
        x1 = (int(x1[0]), int(x1[1]))
        y1 = (int(y1[0]), int(y1[1]))
    
    # for putting mark on text
        cv2.rectangle(image, x1, y1, (25, 25, 255), 5)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # showing image with recognized text
    plt.savefig(file)

    # returning text and accuracy
    content = ''
    prob=''
    for item in results:
        content += item[1]+' '
        num=item[2]*100
        prob +=str('%.2f' % num)+' '
    
    return content,prob
    

