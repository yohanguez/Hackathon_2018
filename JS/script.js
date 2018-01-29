var fd;

function previewFile() {
    var preview = document.querySelector('img');
    var file = document.querySelector('input[type=file]').files[0];
    var reader = new FileReader();

    reader.addEventListener("load", function () {
        preview.src = reader.result;
    }, false);

    if (file) {
        reader.readAsDataURL(file);
    }
}

//Configure a few settings and attach camera - need to set this up to only be called when on second page
function startCamera() {
    Webcam.set({
        width: 320,
        height: 240,
        image_format: 'jpeg',
        jpeg_quality: 90
    });
    Webcam.attach('#my_camera');
}

//Code to handle taking the snapshot and displaying it locally
function take_snapshot() {
    // take snapshot and get image data
    Webcam.snap(function (data_uri) {
        // Send data_uri to the backend.
        var blob = dataURItoBlob(data_uri);
        fd = new FormData(document.forms.namedItem('regForm'));
        fd.append("webcam_pic", blob,
            "webcam_pic.jpg");
    });
}

function take_smiling_snapshot() {
    // take snapshot and get image data
    Webcam.snap(function (data_uri) {
        // Send data_uri to the backend.
        var blob = dataURItoBlob(data_uri);
        fd.append("webcam_pic_smiling", blob,
            "webcam_pic_smiling.jpg");

        var request = new XMLHttpRequest();
        request.open("POST", "http://localhost:5001/register_account");
        request.send(fd);

    });
}

function dataURItoBlob(dataURI) {
    // convert base64/URLEncoded data component to raw binary data held in a string
    var byteString;
    if (dataURI.split(',')[0].indexOf('base64') >= 0)
        byteString = atob(dataURI.split(',')[1]);
    else
        byteString = decodeURI(dataURI.split(',')[1]);

    // separate out the mime component
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

    // write the bytes of the string to a typed array
    var ia = new Uint8Array(byteString.length);
    for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }

    return new Blob([ia], {type: mimeString});
}

$(function () {
    $('a[title]').tooltip();
});