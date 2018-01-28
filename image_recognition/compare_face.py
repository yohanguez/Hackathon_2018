import face_recognition


def compare_face(image1, image2):
    known_image = face_recognition.load_image_file(image1)
    unknown_image = face_recognition.load_image_file(image2)

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding],
                                             unknown_encoding)
    print(results)
    return results
