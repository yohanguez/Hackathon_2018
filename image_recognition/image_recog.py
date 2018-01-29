"""
Hold the functionality of Image Recognition and Verification
"""

import face_recognition
import numpy as np
from PIL import Image, ImageDraw


class Image_recog:
    """ Holds the functionality of testing similarity between two images """

    def __init__(self, im1, im_smiling, im_not_smiling):
        self.im_known = im1
        self.im_smiling = im_smiling
        self.im_not_smiling = im_not_smiling

    def is_similar(self):
        """
        Checks if two images are similar - the same person

        Returns:
             bool. True for the same person False otherwise
        """
        known_image = face_recognition.load_image_file(self.im_known)
        unknown_image = face_recognition.load_image_file(self.im_not_smiling)

        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)
        return results[0]

    def calc_distance(self, a, b):
        """
        Calculates the distance between two points

        Args:
            a(tuple): first point (x,y)
            b(tuple): second point (x,y)

        Returns:
            (float): The distance between two points
        """
        return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** .5

    def calc_distance_from_line(self, m, y, point):
        """
        Calculate the distance of a point from a line

        Args:
            m(float): the slop of the line
            y(float): the intercept of the line
            point(tuple): the given point (x,y)

        Returns:

        slope in decimal, y intercept, (x,y)
        """
        a = m
        b = -1
        c = y
        m = point[0]
        n = point[1]
        return abs(a * m + b * n + c) / ((a) ** 2 + (b) ** 2) ** .5

    def calc_slop_intercept(self, a, b):
        """
        Calculates the slop and intercept between two points

        Args:
            a(tuple): 1st point (x,y)
            b(tuple): 2nd point (x,y)

        Return
            float. slope(m),
            float. y intercept(y)
        """
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

    def calc_triangle_area(self,a, b, c):
        """
        Calculate triangle area given 3 points

        Args:
            a(tuple): 1st point (x,y)
            b(tuple): 2nd point (x,y)
            c(tuple): 3rd point (x,y)

        Returns:
             float. triangle area
        """
        h = self.calc_distance(a, b)
        m, y = self.calc_slop_intercept(a, b)
        b = self.calc_distance_from_line(m, y, c)
        return .5 * h * b


    def is_smiling_ratio(self):
        image = face_recognition.load_image_file(self.im_smiling)
        face_landmarks_list = face_recognition.face_landmarks(image)

        #print("I found {} face(s) in this photograph.".format(
            #len(face_landmarks_list)))

        if not self.is_similar_smiling():
            return False

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
            # print("The {} in this face has the following points: {
            # }".format(facial_feature, face_landmarks[facial_feature]))

            x_1 = [z[0] for z in face_landmarks["bottom_lip"]]
            x_2 = [z[0] for z in face_landmarks["top_lip"]]
            y_1 = [z[1] for z in face_landmarks["bottom_lip"]]
            y_2 = [z[1] for z in face_landmarks["top_lip"]]

            """plt.plot(x_1 + x_2, y_1 + y_2)
            plt.plot(x_1[3], y_1[3], "*", c='r')
            plt.plot(x_2[3], y_2[3], "*", c='b')
            plt.plot(x_1[9], y_1[9], "*", c='g')
            plt.plot(x_2[9], y_2[9], "*", c='k')
            plt.savefig('data/' + "tal")"""

            lowest = y_1[3]
            low = y_1[9]
            uppest = y_2[3]
            up = y_2[9]
            # distance_smile.append(triArea(left, right, top))
            ratio = np.abs((low - up) / (lowest - uppest))

            # print(distance_smile[i])

            # Let's trace out each facial feature in the image with a line!
            pil_image = Image.fromarray(image)
            d = ImageDraw.Draw(pil_image)

            for facial_feature in facial_features:
                d.line(face_landmarks[facial_feature], width=5)

            #pil_image.show()

        if ratio > 0.30:
            return True
        else:
            return False


    def is_similar_smiling(self):
        """
        Checks if two images are similar - the same person

        Returns:
             bool. True for the same person False otherwise
        """
        known_image = face_recognition.load_image_file(self.im_known)
        unknown_image = face_recognition.load_image_file(self.im_smiling)

        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)
        return results[0]

    def is_smiling(self):
        """
        Compares two picture and check if a person is smiling or not

        Returns:
            bool. : True if smiling, False otherwise
        """
        # Retrive images:
        image1 = face_recognition.load_image_file(self.im_smiling)
        image2 = face_recognition.load_image_file(self.im_not_smiling)
        distance_smile = []

        print(self.is_similar_smiling())
        if not self.is_similar_smiling():
            return False

        i = 0
        images = [image1, image2]
        for image in images:

            face_landmarks_list = face_recognition.face_landmarks(image)

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

                x_1 = [z[0] for z in face_landmarks["bottom_lip"]]
                x_2 = [z[0] for z in face_landmarks["top_lip"]]
                y_1 = [z[1] for z in face_landmarks["bottom_lip"]]
                y_2 = [z[1] for z in face_landmarks["top_lip"]]

                left = (x_2[0], y_2[0])
                right = (x_1[0], y_1[0])
                top = (x_1[3], y_1[3])
                distance_smile.append(self.calc_triangle_area(left, right, top))

                # Let's trace out each facial feature in the image with a line!
                pil_image = Image.fromarray(image)
                d = ImageDraw.Draw(pil_image)

                for facial_feature in facial_features:
                    d.line(face_landmarks[facial_feature], width=5)

                i += 1

        # Smiling if the ration of lips triangle is larger than 1:
        if (distance_smile[0] / distance_smile[1]) > 1:
            return (True and self.is_similar_smiling())
        else:
            return (False and self.is_similar_smiling())


#test_reco = Image_recog("/Users/carlalasry/Downloads/carla1.png",
 #"/Users/carlalasry/Desktop/carla_smile.jpg",
        # "/Users/carlalasry/Desktop/carla_not_smile.jpg")


