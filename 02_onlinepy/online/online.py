#!/usr/bin/env python3
''' Check if you are online'''

import socket
import subprocess
from time import sleep

def run_online():
    '''
    Runs function to check internet availability and print status
    '''
    while True:
        try:
            if internet():
                print("online")
            else:
                print("offline")
        except KeyboardInterrupt:
            print('Stopped by keyboard interrupt')
            break
        except OSError as oserror:
            print(oserror)
        except RuntimeError as rerror:
            print(rerror)
        except SystemExit:
            print('Stopped by system interupt')
            break
        sleep(5.0)

def internet(timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        host = socket.gethostbyname("www.google.com")
        _ = socket.create_connection((host, 80))
        return True
    except socket.error as ex:
        print(ex)
        return False


if __name__ == "__main__":
    # execute only if run as a script
    run_online()
