# roku_remote
Roku Remote written in Python
PySimpleGUI is used for the GUI.
The requests module is used to interact with the REST API on the Roku.

Currently you will have to manually type in an IP Address or hostname for the Roku you want to control. There is no automatic detection of Rokus on the network yet.
If an attempted connection fails (which the app attempts to do every time you press a button) the app will crash. I intend to put in some exception handling later to handle that more gracefully.
