FROM ubuntu:xenial

MAINTAINER kadenlnelson@gmail.com

# Install nginx
RUN apt-get update && apt-get install -y \
    nginx

# Stop the service for safety
RUN service nginx stop

# Copy the operating static content over
COPY ./static /opt/web/static

# Install our reverse_proxy configuration
RUN rm /etc/nginx/sites-enabled/default && rm /etc/nginx/sites-available/default
COPY ./default.conf /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default

# Expose ports
EXPOSE 80

# Rezzurect the nginx service
CMD service nginx start && tail -f /var/log/nginx/access.log