FROM ubuntu:20.04

# MAINTANER Your Name "alexandra.penin@le-campus-numerique.fr


RUN apt-get update && apt-get install -y \
	python3-pip python3-dev git
RUN pip3 install --upgrade pip
RUN pip3 install Flask

WORKDIR /app
COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
