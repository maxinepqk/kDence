############################ PLAY SCREEN #############################
from helperfunctions import loadVars

def playMousePressed(event, data):
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR)
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr) 
    (savex0, savey0, savex1, savey1, saver) = (backx0, backy0+backr*3, backx1, 
                                               backy1+backr*3, backr)
    if (event.x > addx0 and event.x < addx1 and event.y > addy0 
        and event.y < addy1):
        data.mode = "playAddInstrument" # clicked the add button
    elif (event.x > backx0 and event.x < backx1 and event.y > backy0 
        and event.y < backy1):
        data.mode = "main" # clicked the back button
    elif (event.x > savex0 and event.x < savex1 and event.y > savey0 
        and event.y < savey1):
        loadVars(data) # clicked the save button
        data.mode = "recordEnd"

def playKeyPressed(event, data): pass

def playTimerFired(data): pass

def playDrawButtons(canvas, data):
    ## Add button
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR) 
    canvas.create_oval(addx0, addy0, addx1, addy1, activefill = data.blue3, 
                       fill = data.blue2, width = 0)
    canvas.create_rectangle(addx0+addr-1, addy0+10, addx1-addr+1, addy1-10, 
                            fill = data.blue0, width = 0) # vertical
    canvas.create_rectangle(addx0+10, addy0+addr-1, addx1-10, addy1-addr+1, 
                            fill = data.blue0, width = 0) # horizontal

    ## Back button
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr)
    canvas.create_oval(backx0, backy0, backx1, backy1, activefill = data.blue3,
                       fill = data.blue2, width = 0)
    canvas.create_polygon(backx0+10, backy0+backr, backx1-14, backy0+10,
                          backx1-14, backy1-10, fill = data.blue0, width = 0)

def playRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    playDrawButtons(canvas, data)
