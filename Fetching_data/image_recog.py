import face_recognition
from PIL import Image, ImageDraw

class Image_recog:
    """Checks similarity between two images"""
    def __init__(self, im1, im_smiling, im_not_smiling):
        self.im_known = im1
        self.im_smiling = im_smiling
        self.im_not_smiling = im_not_smiling
    '''
    Return true if self.im_known and im_not_smiling are the same person (or 
    false if they are not)
    '''
    def check_similarity(self):
        known_image = face_recognition.load_image_file(self.im_known)
        unknown_image = face_recognition.load_image_file(self.im_not_smiling)

        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)
        return results[0]

    '''
    
    '''
    def dis(self, a, b):
        return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** .5

    def lineDis(self,m, y, point):
        """slope in decimal, y intercept, (x,y)"""
        a = m
        b = -1
        c = y
        m = point[0]
        n = point[1]
        return abs(a * m + b * n + c) / ((a) ** 2 + (b) ** 2) ** .5

    def findMY(self, a, b):
        """return slope(m), y intercept(y)"""
        x1, y1, x2, y2 = a[0], a[1], b[0], b[1]
        x1 = float(x1)
        y1 = float(y1)
        slope = (x2 - x1) / (y2 - y1)
        x, y = a[0], a[1]
        while x != 0:
            if x < 0:
                x += 1
                y += slope
            if x > 0:
                x -= 1
                y -= slope
        yint = y
        return slope, yint

    def triArea(self,a, b, c):
        h = self.dis(a, b)
        m, y = self.findMY(a, b)
        b = self.lineDis(m, y, c)
        return .5 * h * b


    def check_is_smiling(self):
        image1 = face_recognition.load_image_file(self.im_smiling)
        image2 = face_recognition.load_image_file(self.im_not_smiling)
        distance_smile = []
        i = 0
        images = [image1, image2]
        for image in images:

            face_landmarks_list = face_recognition.face_landmarks(image)

            #print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

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

                # for facial_feature in facial_features:
                # print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

                x_1 = [z[0] for z in face_landmarks["bottom_lip"]]
                x_2 = [z[0] for z in face_landmarks["top_lip"]]
                y_1 = [z[1] for z in face_landmarks["bottom_lip"]]
                y_2 = [z[1] for z in face_landmarks["top_lip"]]


                left = (x_2[0], y_2[0])
                right = (x_1[0], y_1[0])
                top = (x_1[3], y_1[3])
                distance_smile.append(self.triArea(left, right, top))

                #print(distance_smile[i])

                # Let's trace out each facial feature in the image with a line!
                pil_image = Image.fromarray(image)
                d = ImageDraw.Draw(pil_image)

                for facial_feature in facial_features:
                    d.line(face_landmarks[facial_feature], width=5)

                #pil_image.show()
                i += 1

        if ((distance_smile[0] / distance_smile[1]) > 1):
            return True
        else:
            return False



test_reco = Image_recog("/Users/carlalasry/Downloads/carla1.png", "/Users/carlalasry/Downloads/arthur.jpg", "/Users/carlalasry/Desktop/carla_smile.jpg", "/Users/carlalasry/Desktop/carla_not_smile.jpg")
print(test_reco.check_similarity())
#print(test_reco.similarity)
print(test_reco.check_is_smiling())
#print(test_reco.is_smiling)

