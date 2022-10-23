#! /usr/bin/env/python3

import os
import script
import time

is_repeating = os.environ['REPEATING']


if is_repeating == 'y':
    while True:
        script.run()
        time.sleep(43200)  # 30 days
else:
    script.run()

