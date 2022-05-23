FROM ubuntu:18.04

# Fix for asking for timezone (https://askubuntu.com/a/1098881/458247)
ENV TZ=US/Denver
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
# Official distros are so light they don't even include the sudo command
RUN apt-get install sudo wget git postgresql postgresql-contrib -y

ENTRYPOINT service postgresql start && /bin/bash
