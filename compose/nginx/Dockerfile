FROM openresty/openresty:latest

COPY ./compose/nginx/nginx.conf /etc/openresty/nginx.conf
COPY ./compose/nginx/foxhound.conf /etc/nginx/conf.d/default.conf

ENV TZ=Europe/Moscow
