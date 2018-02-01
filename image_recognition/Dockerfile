FROM aaftio/face_recognition
RUN mkdir /server && pip install flask
COPY . /server
WORKDIR /server
CMD python server.py