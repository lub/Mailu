ARG DISTRO=alpine:3.12
FROM $DISTRO
# python3 shared with most images
RUN apk add --no-cache \
    python3 py3-pip git bash py3-multidict \
  && pip3 install --upgrade pip

# Shared layer between nginx, dovecot, postfix, postgresql, rspamd, unbound, rainloop, roundcube
RUN pip3 install socrate==0.2.0

# Image specific layers under this line
RUN apk add --no-cache rspamd rspamd-controller rspamd-proxy rspamd-fuzzy ca-certificates curl

RUN mkdir /run/rspamd

COPY conf/ /conf
COPY start.py /start.py

EXPOSE 11332/tcp 11334/tcp 11335/tcp

VOLUME ["/var/lib/rspamd"]

CMD /start.py

ENV HOST_FRONT="front" \
    HOST_REDIS="redis" \
    HOST_ANTIVIRUS="antivirus:3310"

HEALTHCHECK --start-period=350s CMD curl -f -L http://localhost:11334/ || exit 1
