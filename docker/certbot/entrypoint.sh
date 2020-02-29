#!/bin/sh
set -eu
trap exit TERM
echo "dns_cloudflare_api_token = $CERTBOT_API_KEY" > /cloudflare.key

if [ ! -f "/etc/letsencrypt/live/$CERTBOT_SERVER_NAME" ]; then
    certbot certonly --non-interactive  --rsa-key-size 4096 --no-self-upgrade --dns-cloudflare --dns-cloudflare-propagation-seconds 60 --dns-cloudflare-credentials /cloudflare.key --email certs@trenton.io --agree-tos --server https://acme-staging-v02.api.letsencrypt.org/directory -d "$CERTBOT_DOMAIN_LIST" # https://acme-v02.api.letsencrypt.org/directory
fi
while :; do
    certbot renew --non-interactive --no-self-upgrade --dns-cloudflare --dns-cloudflare-propagation-seconds 60 --dns-cloudflare-credentials /cloudflare.key --email certs@trenton.io --agree-tos --server https://acme-staging-v02.api.letsencrypt.org/directory -d "$CERTBOT_DOMAIN_LIST # https://acme-v02.api.letsencrypt.org/directory
    sleep 12h & wait $${!}
done
git gc --prune=now
