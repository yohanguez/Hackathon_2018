from PIL import Image, ImageDraw
import face_recognition
import matplotlib.pyplot as plt
import numpy as np

# Load the jpg file into a numpy array
image1 = face_recognition.load_image_file("data/half_closed.jpg")
image2 = face_recognition.load_image_file("data/smile1.jpg")
# Find all facial features in all the faces in the image
images = [image1]


def dis(a,b):
    return (  (b[0]-a[0])**2 + (b[1]-a[1])**2   )**.5

def lineDis(m,y,point):
    """slope in decimal, y intercept, (x,y)"""
    a = m
    b = -1
    c = y
    m = point[0]
    n = point[1]
    return abs(a*m+b*n+c)/((a)**2+(b)**2)**.5

def findMY(a,b):
    """return slope(m), y intercept(y)"""
    x1,y1,x2,y2 = a[0],a[1],b[0],b[1]
    x1 = float(x1)
    y1 = float(y1)
    slope = (x2-x1)/(y2-y1)
    x,y=a[0],a[1]
    while x != 0:
        if x < 0:
            x+=1
            y += slope
        if x > 0:
            x-=1
            y-=slope
    yint = y
    return slope, yint

def triArea(a,b,c):
    h=dis(a,b)
    m,y = findMY(a,b)
    b=lineDis(m,y,c)
    return .5*h*b

distance_smile = []

def check_smiling(images):
    distance_smile = []

    i = 0

    for image in images:

        face_landmarks_list = face_recognition.face_landmarks(image)

        print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

        for face_landmarks in face_landmarks_list:

            # Print the location of each facial feature in this image
            facial_features = [
                'chin',
                'left_eyebrow',
                'right_eyebrow',
                'nose_bridge',
                'nose_tip',
                'left_eye',
                'right_eye',
                'top_lip',
                'bottom_lip'
            ]

            for facial_feature in facial_features:
                print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

            x_1 = [z[0] for z in face_landmarks["left_eye"]]
            x_2 = [z[0] for z in face_landmarks["right_eye"]]
            y_1 = [z[1] for z in face_landmarks["right_eye"]]
            y_2 = [z[1] for z in face_landmarks["left_eye"]]


            #plt.plot(x_1 , y_1 ,"*")
            #plt.plot( x_2, y_2, "*", c="r")

            #plt.show()

            #plt.plot(x_1[3], y_1[3], "*", c='r')
            #plt.plot(x_2[3], y_2[3], "*", c='b')
            #plt.plot(x_1[9], y_1[9], "*",c='g')
            #plt.plot(x_2[9], y_2[9], "*", c='k')
            #plt.savefig('data/' + "tal")

            lowest = y_1[3]
            low = y_1[9]
            uppest = y_2[3]
            up = y_2[9]
            #distance_smile.append(triArea(left, right, top))
            ratio = np.abs((low - up) / (lowest -uppest))


            #print(distance_smile[i])

            # Let's trace out each facial feature in the image with a line!
            pil_image = Image.fromarray(image)
            d = ImageDraw.Draw(pil_image)

            for facial_feature in facial_features:
                d.line(face_landmarks[facial_feature], width=5)

            pil_image.show()
            i += 1
    #print(ratio)
    #if ratio > 0.30 :
        #return True
    #else:
        #return False
    #if((distance_smile[0]/distance_smile[1]) > 1) :
        #return True
#print(face_landmarks["bottom_lip"],face_landmarks["top_lip"])

print(check_smiling(images))