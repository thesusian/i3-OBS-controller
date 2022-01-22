#!/usr/bin/env python

import subprocess
from obswebsocket import obsws, requests
import logging
logging.basicConfig(level=logging.INFO)

host = "localhost"
port = 4444
password = "123456"
ws = obsws(host, port, password)
ws.connect()

LegalWorkspaces = [2, 3]
LegalScene = "FullscreenView"
IllegalScene = "BeRightBack"

PrevWorkspace = 0

while True:
    CurrentWorkspace = (int(subprocess.getoutput("./GetCurrentWorkspace.sh")))
    
    if PrevWorkspace != CurrentWorkspace:
        if CurrentWorkspace in LegalWorkspaces:
            print("Legal Workspace")
            scene = ws.call(requests.SetCurrentScene(LegalScene))

        else:
            print("Illegal Workspace")
            scene = ws.call(requests.SetCurrentScene(IllegalScene))
    
    PrevWorkspace = CurrentWorkspace

ws.disconnect()
