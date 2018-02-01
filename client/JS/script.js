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

        var request = createCORSRequest("POST", "http://localhost:5001/register_account");
        request.responseType = 'json';
        request.onload = function () {
            var jsonResponse = request.response;
            console.log(jsonResponse);
            var is_similar = jsonResponse.is_similar;
            var is_smiling_ratio = jsonResponse.is_smiling_ratio;

            const GLYPHICON_OK_CLASSES = "glyphicon\n" +
                "                              glyphicon-ok";
            const GLYPHICON_REMOVE_CLASSES = "glyphicon\n" +
                "                              glyphicon-remove";

            $('#compareSpan').removeClass();
            $('#smilingSpan').removeClass();

            if (is_similar) {
                $('#compareSpan').addClass(GLYPHICON_OK_CLASSES);
            }
            else {
                $('#compareSpan').addClass(GLYPHICON_REMOVE_CLASSES);

            }

            if (is_smiling_ratio) {
                $('#smilingSpan').addClass(GLYPHICON_OK_CLASSES);
            }
            else {
                $('#smilingSpan').addClass(GLYPHICON_REMOVE_CLASSES);
            }

            if (is_similar && is_smiling_ratio) {
                $('#successSpan').text("succeeded. Welcome !!");
            }
            else {
                $('#successSpan').text("failed. Please retry.");
            }
            $("body").removeClass("loading");
            // $('#myTab a:last').tab('show');
        };
        request.send(fd);
        $("body").addClass("loading");
    });
    // Show please wait
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

// Create the XHR object.
function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
        // XHR for Chrome/Firefox/Opera/Safari.
        xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
        // XDomainRequest for IE.
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        // CORS not supported.
        xhr = null;
    }
    return xhr;
}