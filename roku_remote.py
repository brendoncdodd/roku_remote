from enum import IntEnum
import socket
import requests
import PySimpleGUI as sg

ROKU_HOST = ""

"""Define some button flags that we can use to signal which button we're "pressing"."""
class Roku_Button_Code(IntEnum):
    HOME	= 0x0001
    SEL		= 0x0002
    BACK	= 0x0004
    LEFT	= 0x0008
    RIGHT	= 0x0010
    UP		= 0x0020
    DOWN	= 0x0040
    REV		= 0x0080
    FWD		= 0x0100
    PLAY	= 0x0200

def roku_post(ip_addr, button_code):
    response = {}
    match button_code:
        case Roku_Button_Code.HOME:
            response = requests.post("http://" + ip_addr +":8060/keypress/home", '')
        case Roku_Button_Code.SEL:
            response = requests.post("http://" + ip_addr +":8060/keypress/select", '')
        case Roku_Button_Code.BACK:
            response = requests.post("http://" + ip_addr +":8060/keypress/back", '')
        case Roku_Button_Code.LEFT:
            response = requests.post("http://" + ip_addr +":8060/keypress/left", '')
        case Roku_Button_Code.RIGHT:
            response = requests.post("http://" + ip_addr +":8060/keypress/right", '')
        case Roku_Button_Code.UP:
            response = requests.post("http://" + ip_addr +":8060/keypress/up", '')
        case Roku_Button_Code.DOWN:
            response = requests.post("http://" + ip_addr +":8060/keypress/down", '')
        case Roku_Button_Code.REV:
            response = requests.post("http://" + ip_addr +":8060/keypress/rev", '')
        case Roku_Button_Code.FWD:
            response = requests.post("http://" + ip_addr +":8060/keypress/fwd", '')
        case Roku_Button_Code.PLAY:
            response = requests.post("http://" + ip_addr +":8060/keypress/play", '')
    return response

# Define the window's contents
sg.theme('Dark Blue 5')
layout = [[sg.Text("Host:"), sg.Input(key='-IPADDR-')],
       	  [[sg.Text(size=(15,1))], [[sg.Button('Back'), sg.Text(size=(4,1)), sg.Button('Home')],
                                    [sg.Text(size=(5,1)), sg.Button('Up')],
                                    [sg.Button('Left'), sg.Button('Select'), sg.Button('Right')],
                                    [sg.Text(size=(4,1)), sg.Button('Down')],
                                    [sg.Text(size=(0,1)),sg.Button('<--'),sg.Button('Play'),sg.Button('-->')]
                                   ]
          ],
          [sg.Text(size=(40,1), key='-OUTPUT-'), sg.Button('Quit')]
         ]

# Create the window
window = sg.Window('Roku Remote', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Get the user input IP Address
    ROKU_HOST = values['-IPADDR-']
    # Check if one of the buttons was pressed
    match event:
        case 'Home':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.HOME)
        case 'Select':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.SEL)
        case 'Back':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.BACK)
        case 'Up':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.UP)
        case 'Left':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.LEFT)
        case 'Right':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.RIGHT)
        case 'Down':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.DOWN)
        case '<--':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.REV)
        case 'Play':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.PLAY)
        case '-->':
            http_response = roku_post(ROKU_HOST, Roku_Button_Code.FWD)
    window['-OUTPUT-'].update("Response " + str(http_response.status_code))

# Finish up by removing the window from the screen
window.close()
