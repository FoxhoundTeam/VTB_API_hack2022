FROM openresty/openresty:latest

COPY ./compose/nginx/nginx.conf /etc/openresty/nginx.conf
COPY ./compose/nginx/foxhound.conf /etc/nginx/conf.d/foxhound.conf

ENV TZ=Europe/Moscow
