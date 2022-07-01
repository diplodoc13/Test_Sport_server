import telnetlib
import random

HOST = "localhost"
PORT = 9999

data = [["0001 C1 01:13:02.177 00[CR]"], ["0002 C1 01:16:02.677 01[CR]"], ["0003 C1 01:19:02.777 00[CR]"],
        ["0004 C1 01:14:02.277 00[CR]"], ["0005 C1 01:17:02.577 01[CR]"], ["0006 C1 01:20:02.877 00[CR]"],
        ["0007 C1 01:15:02.377 00[CR]"], ["0008 C1 01:18:02.477 01[CR]"], ["0009 C1 01:21:02.977 00[CR]"]]

tn = telnetlib.Telnet(HOST, PORT)

tn.write(f'{" ".join(random.choice(data))}'.encode())
