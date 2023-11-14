import screeninfo
colors = {
    "BG": "#F2EFC7",
    "TXT": "#9F7E69",
    "UI":"#D2BBA0",
    "HP":"#9F7E69"
}
WW, WH = screeninfo.get_monitors()[0].width, screeninfo.get_monitors()[0].height

FPS = 30

respondToMouse = True
background = True