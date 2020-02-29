#!/bin/sh
set -eu
trap exit TERM
echo "dns_cloudflare_api_token = $CERTBOT_API_KEY" > /cloudflare.key

if [ ! -f "/etc/letsencrypt/live/$CERTBOT_SERVER_NAME" ]; then
    certbot certonly --non-interactive  --rsa-key-size 4096 --no-self-upgrade --dns-cloudflare --dns-cloudflare-propagation-seconds 60 --dns-cloudflare-credentials /cloudflare.key --email "$CERTBOT_EMAIL" --agree-tos --server "${CERTBOT_SERVER}" -d "$CERTBOT_DOMAIN_LIST"
fi
while :; do
    certbot renew --non-interactive --no-self-upgrade --dns-cloudflare --dns-cloudflare-propagation-seconds 60 --dns-cloudflare-credentials /cloudflare.key --email "$CERTBOT_EMAIL" --agree-tos --server "${CERTBOT_SERVER}"
    sleep 12h & wait $!
done
git gc --prune=now
