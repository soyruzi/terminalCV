FROM nginx

ADD www /usr/share/nginx/html
COPY nginx/cv.conf /etc/nginx/conf.d/cv.conf
RUN find /usr/share/nginx/html -type d -exec chmod 755 {} \;
RUN find /usr/share/nginx/html -type f -exec chmod 644 {} \;

