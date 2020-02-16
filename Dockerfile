FROM nginx

ADD www /usr/share/nginx/html
COPY nginx/cv.conf /etc/nginx/conf.d/cv.conf
