# Frontend for nginx:mainline-alpine3.20-slim
FROM nginx@sha256:e9293c9bedb0db866e7d2b69e58131db4c2478e6cd216cdd99b134830703983a

COPY ./react/nginx.conf /etc/nginx/nginx.conf
COPY ./react/build /var/www/html

USER nginx

CMD ["nginx"]