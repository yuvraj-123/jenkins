#This is a sample Image 
FROM ubuntu 
MAINTAINER Yuvraj Singh

RUN apt-get update 
RUN apt-get install –y nginx 
CMD ["echo","Image created"]