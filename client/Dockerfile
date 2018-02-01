FROM frolvlad/alpine-python3
RUN mkdir /data
COPY . /data
ENV DATADIR /data
ENV PORT 443
EXPOSE ${PORT}
WORKDIR ${DATADIR}
CMD python server.py