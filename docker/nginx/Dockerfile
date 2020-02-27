FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx-default.conf.template /etc/nginx/conf.d/default.conf.template
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]