"""
Hold the functionality of getting images urls, download images and compare if they contain the same personality
"""

import requests

from flask import json


def download_image(url):
    """
    Download image by url

    Args:
        url(str): the image url
    """

    response = requests.get(url)
    if response.status_code == 200:
        with open("sample.jpg", 'wb') as f:
            f.write(response.content)


def request_handler():
    pass


@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
                f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

url = "https://www.petakids.com/wp-content/uploads/2015/11/Cute-Red-Bunny.jpg"
download_image(url)




