# i3 obs controller


### Requirements
* the [obs-websocket](https://obsproject.com/forum/resources/obs-websocket-remote-control-obs-studio-from-websockets.466/) plugin
* the `obs-websocket-py` python library `pip install obs-websocket-py`

### Usage
1. after installing the [obs-websocket](https://obsproject.com/forum/resources/obs-websocket-remote-control-obs-studio-from-websockets.466/) plugin, open obs and setup the plugin to add a password and chose a port
2. clone the code `git clone https://github.com/thesusian/i3-obs-controller.git` or simply download and extract the zip
3. edit the `main.py` file and change the following variables
  * **port**: the obs websocket port
  * **password**: the obs websocket password
  * **LegalWorkspaces**: the workspaces to be assigned to the first scene
  * **LegalScene**: the scene that will be active when you are on a **LegalWorkspace**
  * **IllegalScene**: the scene that will be a ctive when you are **not** on a **LegalWorkspace**
