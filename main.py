from PIL import Image,ImageOps
import cv2
import time
 
nFrames=100 # Max number of frame (you can also render all frames looping in a while true)
inverted=False # invert colors
 
vidcap=cv2.VideoCapture('test.mp4') # Filename
vidcap.set(cv2.CAP_PROP_FPS,1)
success,image = vidcap.read()
count = 0
 
def imageToAsciiG(imgG,w,h):
    pixG = imgG.load()
    with open('text.txt','a',encoding='UTF-8') as f:
        for y in range(h):
            for x in range(w):
                if(pixG[x,y]>75):
                    f.write('▓') # 100
                elif(pixG[x,y]>50):
                    f.write('▒') # 75
                elif(pixG[x,y]>25):
                    f.write('░') # 50
                else:
                    f.write(' ') # 25
            f.write('\n')
            #print()
 
for i in range(nFrames):
    f=open('text.txt','r+')
    #f.truncate(0) Uncomment for delete last frames
    cv2.imwrite("frames/{}.jpg".format(count+1), image) # Save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    imgRGB = Image.open("frames/{}.jpg".format(count+1))
    imgG = ImageOps.grayscale(imgRGB)
    if inverted:
        imgG = ImageOps.invert(imgG)
    w,h=imgG.size
    imageToAsciiG(imgG,w,h)
    count += 1
    #time.sleep(0.5) Uncomment for delay
