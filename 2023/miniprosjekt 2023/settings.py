import screeninfo, saves, saves_V2
colors = {
    "BG": "#F2EFC7",
    "TXT": "#9F7E69",
    "UI":"#D2BBA0",
    "HP":"#9F7E69"
}
WW, WH = screeninfo.get_monitors()[0].width, screeninfo.get_monitors()[0].height

FPS = 30

currentSave = saves_V2.save_1
respondToMouse = 1
background = 1