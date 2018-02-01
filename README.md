# Hackathon_2018

Build:
- docker-compose build
- docker-compose push

Deployment:
- Launching a Ubuntu 16.04 server
- Installing Docker on the server: https://docs.docker.com/install/linux/docker-ce/ubuntu/
- Installing Docker compose on the server: https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04
- docker-compose up -d

Notes on architecture:
- Generated self-signed certificates for client-side with this blog:
http://pankajmalhotra.com/Simple-HTTPS-Server-In-Python-Using-Self-Signed-Certs
This was necessary to use webcam on secure domain.