from PIL import Image, ImageDraw
import face_recognition
import matplotlib.pyplot as plt

# Load the jpg file into a numpy array
image1 = face_recognition.load_image_file("/Users/carlalasry/Desktop/carla_smile.jpg")
image2 = face_recognition.load_image_file("/Users/carlalasry/Desktop/carla_not_smile.jpg")
# Find all facial features in all the faces in the image
images = [image1,image2]
i=0
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

        x_1 = [z[0] for z in face_landmarks["bottom_lip"]]
        x_2 = [z[0] for z in face_landmarks["top_lip"]]
        y_1 = [z[1] for z in face_landmarks["bottom_lip"]]
        y_2 = [z[1] for z in face_landmarks["top_lip"]]


        plt.plot(x_1 + x_2,y_1 + y_2)
        plt.savefig('/Users/carlalasry/Desktop/' + str(i))

        # Let's trace out each facial feature in the image with a line!
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)

        for facial_feature in facial_features:
            d.line(face_landmarks[facial_feature], width=5)

        pil_image.show()
        i+=1

#print(face_landmarks["bottom_lip"],face_landmarks["top_lip"])