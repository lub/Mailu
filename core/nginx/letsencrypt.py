#!/usr/bin/python3

import os
import time
import subprocess


command = [
    "certbot",
    "-n", "--agree-tos", # non-interactive
    "-d", os.environ["HOSTNAMES"],
    "-m", "{}@{}".format(os.environ["POSTMASTER"], os.environ["DOMAIN"]),
    "certonly", "--standalone",
    "--cert-name", "mailu",
    "--preferred-challenges", "http", "--http-01-port", "8008",
    "--keep-until-expiring",
    "--rsa-key-size", "4096",
    "--config-dir", "/certs/letsencrypt",
    "--post-hook", "/config.py"
]

# if dane is used we recommend pinning to the key, so it should not change
# ('true','yes') to be consistent with the logic in configuration.py
if os.environ.get("TLS_REUSE_KEY", "false").lower() in ('true','yes'):
    command.append("--reuse-key")

# Wait for nginx to start
time.sleep(5)

# Run certbot every hour
while True:
    subprocess.call(command)
    time.sleep(3600)

