
# covid19 vizualizare date - moldova

# Docker 
inspired from: https://hub.docker.com/r/waleedka/modern-deep-learning/

## Build image
sudo docker build -t covid19md:1 -f Dockerfile .

## Run container 
* sudo docker run -it -d -p 8881:8881  -p 6001:6001 -v "$(pwd)":/app --name covid19mdbox covid19md:1
* sudo docker exec -ti covid19md bash
* python main.py