# This is a _very simple_ example of a web service that recognizes faces in uploaded images.
# Upload an image file and it will check if the image contains a picture of Barack Obama.
# The result is returned as json. For example:
#
# $ curl -F "file=@obama2.jpg" http://127.0.0.1:5001
#
# Returns:
#
# {
#  "face_found_in_image": true,
#  "is_picture_of_obama": true
# }
#
# This example is based on the Flask file upload example: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

# NOTE: This example requires flask to be installed! You can install it with pip:
from image_recognition.image_recog import Image_recog
from flask import Flask, jsonify, request, redirect

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


'''
/register_account
```
{
   "first_name": "Or Rez",     
   "last_name": "Rez",    
   "email": "or.rez@gmail.com",  
   "uploaded_image": base64encodedimage,
   "webcam_image_simple": base64encodedimage2,
   "webcam_image_smiling": base64encodedimage3,
}
```
JSON result:
```
{
   "same_image": True,   
   "same_image_and_smiling_image": True, 
}
```
'''


@app.route('/register_account', methods=['POST'])
def upload_images():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'original_pic' not in request.files and 'webcam_pic' not in \
                request.files and 'webcam_pic_smiling' not in \
                request.files:
            return redirect(request.url)

        original_pic = request.files['original_pic']
        webcam_pic = request.files['webcam_pic']
        webcam_pic_smiling = request.files['webcam_pic_smiling']

        if original_pic.filename == '' or webcam_pic.filename == '' or webcam_pic_smiling.filename == '':
            return redirect(request.url)

        # The image file seems valid! Detect faces and return the result.
        return verify_identity(original_pic, webcam_pic, webcam_pic_smiling)


def verify_identity(original_pic, webcam_pic, webcam_pic_smiling):
    # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)
    my_imagerecog = Image_recog(original_pic, webcam_pic_smiling, webcam_pic)

    # Load the uploaded image file

    # Return the result as json
    result = {
        "is_similar": my_imagerecog.is_similar(),
        "is_smiling_ratio": my_imagerecog.is_smiling_ratio(),
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
