## DRAWING FUNCTIONS

# METRONOME
def drawMetronome(canvas, data):
    (cx, cy, r) = (60, data.height-60, 35)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, activefill = data.blue1, 
                       fill = data.blue05, width = 0)
    canvas.create_image(cx, cy, image = data.picMetro)

def drawMetroMenu(canvas, data):
    (metrox0, metroy0, metrox1, metroy1, metror) = (25, data.height-95, 95, 
                                            data.height-25, 35)
    canvas.create_polygon(metrox1+40, metroy1, metrox1+25, metroy1-15,
                          metrox1+55, metroy1-15, activefill = data.blue2, 
                          fill = data.blue4, width = 0)
    canvas.create_polygon(metrox1+40, metroy0, metrox1+25, metroy0+15,
                          metrox1+55, metroy0+15, activefill = data.blue2, 
                          fill = data.blue4, width = 0)
    canvas.create_text(metrox1+40, (metroy0+metroy1)//2, 
    text = data.metronomeBPM, font = ("Lato Thin", 25), fill = data.blue4)