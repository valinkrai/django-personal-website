#!/bin/sh
set -eu
trap exit TERM

if [ ! -f "$FILE" ]; then
    certbot certonly --non-interactive  --rsa-key-size 4096 --no-self-upgrade --dns-cloudflare --dns-cloudflare-propagation-seconds 30 --dns-cloudflare-credentials /cloudflare.key --email certs@trenton.io --agree-tos --server https://acme-staging-v02.api.letsencrypt.org/directory # https://acme-v02.api.letsencrypt.org/directory
fi
while :; do
    certbot renew --non-interactive --no-self-upgrade --dns-cloudflare --dns-cloudflare-propagation-seconds 30 --dns-cloudflare-credentials /cloudflare.key --email certs@trenton.io --agree-tos --server https://acme-staging-v02.api.letsencrypt.org/directory # https://acme-v02.api.letsencrypt.org/directory
    sleep 12h & wait $${!}
done