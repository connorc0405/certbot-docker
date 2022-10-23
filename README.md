This image bulk-fetches certificates from LetsEncrypt from a domain list.  See this example compose config:

```
certbot:
    image: certbot:latest
    build: ./certbot
    volumes:
      - /path/to/domains.txt:/domains.txt
      - /path/to/config:/config
      - /path/to/work:/work
      - /path/to/logs:/logs
      - /path/to/aws_credentials:/root/.aws/config
    environment:
      - EMAIL=<your_email>
      - REPEATING=y  # 'y' or anything else for No
    restart: always
```
