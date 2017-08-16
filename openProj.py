########################## OPEN PROj SCREEN ###########################
import os, os.path
from PIL import Image, ImageTk

def openProjMousePressed(event, data): pass

def openProjKeyPressed(event, data): pass

def openProjTimerFired(data): pass

def openProjRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    drawProjects(canvas, data)

def drawProjects(canvas, data):
    number =  str(len([name for name in os.listdir("savedFiles") 
               if os.path.isfile(name)])+1) # this line is from bit.ly/2gx1QWl
    if (number == 0):
        canvas.create_text(data.cx, data.cy, text = "No projects created yet!",
        font = ("Lato Thin Italic", 80))
    else:
        i = 0
        for project in range(1, len(number)+1):
            i += 1
            im = Image.open("savedScreenies/1.gif")

            im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)
            im.save('savedScreenies/1.gif')
            screenieCropped = im.crop((10,50,800,800))
            #screenie = PhotoImage(file = "savedScreenies/%s.gif"%str(project))
            canvas.create_image(50*i, 50, image = screenieCropped)
    
