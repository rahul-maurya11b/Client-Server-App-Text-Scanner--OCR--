# Client-Server-App-Text-Scanner-OCR-
# USAGE:
## 1.
python .\server.py .\result.jpeg.

first run the server and then on argv[1] enter the name of file  which will be output of input image provided by client.

## 2. 

python .\client.py .\img3.jpeg.

then clien will connect with the server and on argv[1] enter the image file name of which text is to be recognized.

# Output

## (i) Server side
PS D:\socket programming> python .\server.py .\result.jpeg
Server is running
Server is ready to accept data ...
connected with client having ('192.168.1.101', 59346)
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
PS D:\socket programming>


## (ii) Client side 
PS D:\socket programming> python .\client.py .\img3.png  
client conected
****************************************************************
Result of text Recognition is:

****************************************************************
Do not resolve addresses to hostnames Maximum number 0f hops to search for target Loose source route along host-list (IPv4-only) Wait timeout milliseconds for each reply _ Trace round-trip path (IPv6-only) Source address to use (IPv6-only). Force using IPv4 . Force using IPv6 _ 
****************************************************************
Result in Table form

|     Text     | Accuracy |
| ------------ | --------:|
|      Do      |  99.99   |
|     not      |  90.46   |
|   resolve    |  99.99   |
|  addresses   |  98.68   |
|      to      |  99.96   |
|  hostnames   |  99.91   |
|   Maximum    |  26.89   |
|    number    |  100.00  |
|      0f      |  99.99   |
|     hops     |  99.71   |
|      to      |  90.46   |
|    search    |  100.00  |
|     for      |  99.97   |
|    target    |  97.36   |
|    Loose     |  73.13   |
|    source    |  100.00  |
|    route     |  99.77   |
|    along     |  99.91   |
|  host-list   |  70.38   |
| (IPv4-only)  |  92.15   |
|     Wait     |  99.99   |
|   timeout    |  99.99   |
| milliseconds |  99.98   |
|     for      |  99.99   |
|     each     |  60.04   |
|    reply     |  67.17   |
|      _       |  99.34   |
|    Trace     |  79.04   |


PS D:\socket programming>

## Output Image

![alt text](https://github.com/rahul-maurya11b/Client-Server-App-Text-Scanner-OCR-/blob/master/result.jpeg)

## Conclusion.
Text recognition is greatly dependent the condition of
handwriting the contrast, Brightness ratios in image and
many more factors.
To detect the text very accurately our model should be more
robust, and fault tolerant in any condition at the same time
our model should be fast.
So, with the fast and accurate model, server can send data to
client very fast and accurate. So, communication will be
faster.
With this conclusion summing-up my project.




 

