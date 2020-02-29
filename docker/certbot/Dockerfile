FROM certbot/cloudflare-dns

COPY cloudflare.key /cloudflare.key
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]