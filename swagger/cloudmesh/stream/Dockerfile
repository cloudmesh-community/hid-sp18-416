FROM python:3.6

# Update the system, install Python, make, pip, acl and create user
RUN apt-get update && \
    apt-get install -q -y default-jre && \
    adduser swagger-user && \
    chown -R swagger-user: /usr/local/

# Switch user to swagger user 
USER swagger-user
# Create folder for files
RUN mkdir ~/files

# Copy required files
COPY ["Makefile", "swagger-stream-twitter.yaml", "credentials.yaml", \
      "__main__.py", "movies_controller.py", "music_controller.py", \
      "tv_shows_controller.py", "stream-requirements.txt", "swagger-codegen-cli-2.3.1.jar", "download-swagger-codegen.sh", "/home/swagger-user/files/"]

WORKDIR /home/swagger-user/files

RUN make service
EXPOSE 9550

CMD ["make", "start"]
