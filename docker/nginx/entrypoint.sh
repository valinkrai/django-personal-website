#!/usr/bin/env sh
set -eu

echo 'Running substitutions for nginx'
envsubst '${NGINX_SERVER_NAME}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

exec "$@"