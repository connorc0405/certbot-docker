FROM certbot/dns-route53

RUN apk add bash python3

COPY entry.py /
COPY script.py /

ENTRYPOINT ["python3", "/entry.py"]

