# Sample Docker container with Eagle installed
FROM debian:buster

RUN apt-get clean && apt-get update && apt-get install -y wget libgomp1

# Install Eagle
RUN wget "https://data.broadinstitute.org/alkesgroup/Eagle/downloads/dev/eagle_v2.4.1" -O /usr/bin/eagle
RUN chmod a+x /usr/bin/eagle
