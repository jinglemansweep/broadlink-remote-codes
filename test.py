#!/usr/bin/env python

import time
import broadlink

BROADLINK_RM_HOST="10.0.2.80"
LOOP_DELAY = 0.05

ur = broadlink.hello(BROADLINK_RM_HOST)
ur.auth()

while True:
    ur.enter_learning()
    try:
        packet = ur.check_data()
        if packet:
            print(packet)
    except: 
        pass
    time.sleep(LOOP_DELAY)
    