FROM python:3.6

# Update the system, install Python, make, pip, acl and create user
#RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && \
    apt-get install -q -y default-jre && \
    #rm -rf /var/lib/apt/lists/* && \
    adduser swagger-user && \
    chown -R swagger-user: /usr/local/ && \
    pip install tweepy

# Switch user to swagger user 
USER swagger-user
# Download Swagger-Codegen jar
RUN mkdir ~/swagger && \
    mkdir ~/files && \
    wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -P ~/swagger

# Copy required files
COPY ["Makefile", "swagger-stream-twitter.yaml", "credentials.yaml", \
      "__main__.py", "movies_controller.py", "music_controller.py", \
      "tv_shows_controller.py", "/home/swagger-user/files/"]

WORKDIR /home/swagger-user/files

RUN make service
EXPOSE 9550

CMD ["make", "start"]
