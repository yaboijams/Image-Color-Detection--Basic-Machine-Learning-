import os
import argparse
import cv2
import pandas as pd

###List out current images inside of image directory
Folder_Path = r'C:\Users\JKM\Documents\GitHub\Image-Color-Detection--Basic-Machine-Learning-'
Images_Dir = r'C:\Users\JKM\Documents\GitHub\Image-Color-Detection--Basic-Machine-Learning-\Images'

def listDir(dir):
    print("This is the list of images that you currently have stored\n")
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print(fileName)

if __name__ =='__main__':
    listDir(Images_Dir)

def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

#Reading image with 
os.chdir(Images_Dir)
imageInput = input('\n What image would you like to run recognition on: \n')
img = cv2.imread(imageInput)
window_name = 'Image Color Recognition'
os.chdir(Folder_Path)

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name,draw_function)




while(1):
    cv2.imshow(window_name,img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display ( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)
        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
  #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    #Break the loop when user hits 'esc' key 
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()