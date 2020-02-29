FROM certbot/dns-cloudflare

COPY cloudflare.key /cloudflare.key
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]