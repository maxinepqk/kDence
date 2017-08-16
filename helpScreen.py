########################## HELP SCREEN ###########################

def helpScreenMousePressed(event, data):
    (prevx0, prevy0, prevx1, prevy1)  = (50, data.cy-25, 100, data.cy+25)
    (nextx0, nexty0, nextx1, nexty1) = (data.width-100, data.cy-25, data.width-50, 
                                        data.cy+25)

    if (event.x < prevx0 and event.x > prevx1 and event.y < prevy0 and 
        event.y > prevy1):
        data.helpPage -= 1
        if (data.helpPage == 0):
            data.mode = "main"
    elif (event.x < nextx0 and event.x > nextx1 and event.y < nexty0 and 
        event.y > nexty1): 
        data.helpPage += 1
        if (data.helpPage > 7):
            data.mode = "main"

def helpScreenKeyPressed(event, data):
    if (event.keysym == "Left"): data.helpPage -=1
    elif (event.keysym == "Right"): data.helpPage += 1

def helpScreenTimerFired(data): pass

def helpScreenRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    canvas.create_polygon(50, data.cy, 100, data.cy-25, 100, data.cy+25, 
                          activefill = data.blue2, fill=data.blue4, width = 0)
    canvas.create_polygon(data.width-50, data.cy, data.width-100, data.cy-25, 
                          data.width-100, data.cy+25, activefill = data.blue2,
                          fill=data.blue4, width = 0)
    canvas.create_image(data.cx, data.cy, image = data.helpPic1)