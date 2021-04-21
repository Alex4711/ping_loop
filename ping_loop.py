#!/usr/local/bin python3.8

import subprocess
import os
import random

def cool_function_bro():


        with open(os.devnull, "wb") as limbo:
                add = ["127.0.0.1","10.1.1.254","1.1.1.1","1.0.0.1","192.168.178.1"]
                for n in range(len(add)):
                        ip = (add[n])
                        result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                stdout = limbo, stderr=limbo).wait()
                        if result:
                                print ('\x1b[1;31;47m' + ' inactive! -> ' + '\x1b[0m',ip)
                        else:
                                print ('\x1b[6;30;42m' + ' active! -> ' + '\x1b[0m',ip)


for i in range(100):
  cool_function_bro()


# Ping Test with List
#
# farben in CLI https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
#
# Farbecode von stack siehe link in Zeile 4
# print zeigt value und text in Farbe
#print ('\x1b[6;30;42m' +ip+ '\x1b[0m', '\x1b[6;30;42m' + 'active!' + '\x1b[0m')
# grün auf schwarz
# '\x1b[6;30;42m' + 'active!' + '\x1b[0m'
# rot auf schwarz
# '\x1b[0;30;41m' + 'inactive!' + '\x1b[0m'
