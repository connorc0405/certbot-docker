#! /usr/bin/env/python3

import subprocess
import os

def run():
    email = os.environ['EMAIL']

    with open('/domains.txt', 'r') as domains_file:
        domains_list = domains_file.readlines()

    for domain in domains_list:
        final_domain = domain.rstrip()
        subprocess.check_output(['certbot', 'certonly', '--dns-route53', '-d', final_domain, '--email', email, '--non-interactive', '--agree-tos', '--config-dir', '/config', '--work-dir', '/work', '--logs-dir', '/logs'])

