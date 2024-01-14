import math
import random
from tkinter import *
from PIL import Image, ImageDraw, ImageFont


width = 400
height = 300
white = (255, 255, 255)
green = (0,128,0)


def T(antal):
    return random.randint(1, antal)
    
def startDoc(w, h):
    global image1
    global draw
    global width
    global height
    width = w
    height = h
    image1 = Image.new("RGBA", (w, h), white)
    draw = ImageDraw.Draw(image1)
    return draw

def endDoc():
    global image1
    global draw
    # PIL image can be saved as .png .jpg .gif or .bmp file (among others)
    filename = "my_drawing.png"
    image1.save(filename)
    image1.show()

def readData():
    global tiledata
    global extradata
    global totalrate
    
        # Using readlines()
    file1 = open('data.ini', 'r', encoding="utf-8")
    Lines = file1.readlines()
    tiledata = []
    extradata = []
    totalrate = 0
    # Strips the newline character
    for line in Lines:
        ls = line.split(";")
        if (len(ls) >=3):
            data = {}
            data["id"] = ls[1]
            data["name"] = ls[2]
            data["rate"] = int(ls[3])
            data["image"] = ls[4]
            if line[0] == 't' :
                for i in range(data["rate"]):
                    tiledata.append(data)
                    totalrate += 1
            if line[0] == 'e' :
                for i in range(data["rate"]):
                    extradata.append(data)
            
            
    print(tiledata)
    print(extradata)
    diff = len(tiledata) - len(extradata)
    for i in range(diff):
        data = {}
        data["id"] = ""
        data["name"] = ""
        data["rate"] = 0
        data["image"] = "tom.png"
        extradata.append(data)

def col_width(radie):
    return radie * 3

 
def row_height(radie):
    return math.sin(math.pi / 3) * radie


def hexagon(x,y,radie):
    points = []
    for angle in range(0, 360+60, 60):
        x1 = x + math.cos(math.radians(angle)) * radie
        y1 = y + math.sin(math.radians(angle)) * radie
        points.append((x1,y1))
    return points

def drawHex(x,y,r):
    global draw
    points = hexagon(x,y,r)
    #draw.polygon(list(hexagon), outline='black', fill='white')
    draw.line(points, fill='black', width=2)

def drawTileInfo(x,y,r):
    global draw
    rowheight = row_height(r)*2
    typ = T(totalrate)-1
    typtext = tiledata[typ]["name"]
    typimage = Image.open("./asset/"+tiledata[typ]["image"], 'r')
    imagewidth = int(rowheight)
    typimage = typimage.resize((imagewidth,imagewidth), Image.LANCZOS)
    extra = T(totalrate)-1
    extratext = extradata[extra]["name"]
    extraimage = Image.open("./asset/"+extradata[extra]["image"], 'r')
    
    extraimage = extraimage.resize((int(imagewidth/2),int(imagewidth/2)), Image.LANCZOS)
    
    font = ImageFont.truetype("DejaVuSans.ttf", int(r*1), encoding="unic")
    font2 = ImageFont.truetype("DejaVuSans.ttf", int(r*0.1), encoding="unic")

    
    #SLÄTT	SKOG	MÖRK SKOG	KULLAR	BERG	SJÖ	TRÄSK	MYR	RUINSTAD	STAD
    # if ( typ == 1):
    #     typtext = "F" #slätt = fält   
    # if ( typ == 2):
    #     typtext = "S" # Skog
    # if ( typ == 3):
    #     typtext = "MS" #Mörk skog
    # if ( typ == 4):
    #     typtext = "K"
    # if ( typ == 5):
    #     typtext = "B"
    # if ( typ == 6):
    #     typtext = "V"
    # if ( typ == 7):
    #     typtext = "T"
    # if ( typ == 8):
    #     typtext = "M"
    # if ( typ == 9):
    #     typtext = "R"
    # if ( typ == 10):
    #     typtext = "ST"
    w = draw.textlength(typtext, font=font2)
    w2 = draw.textlength(extratext, font=font2)
    h = r
    h2 = r*0.1
    
    mask = Image.new("L", typimage.size)
    points = hexagon(rowheight/2,rowheight/2,r-2)
    d = ImageDraw.Draw(mask)
    d.polygon(points,fill=255)
    
    image1.paste(typimage,(int(x-imagewidth/2), int(y-imagewidth/2)), mask)
    
    
    image1.paste(extraimage,(int(x-imagewidth/2), int(y-imagewidth/2)), extraimage)
    
    draw.text((x-w/2, y-rowheight/2+5), typtext, "black", font=font2, anchor="ms", align="center")
    draw.text((x-w2/2, y+rowheight/2-h2-5), extratext, "black", font=font2, anchor="ms", align="center")
    
    
def hexGrid(antal):
    global width
    global height
    global rowheight
    
    size = height/antal
    offx = size
    offy = size
    for row in range(antal):
        for col in range(antal):
            x = (col + 0.5 * (row % 2)) * col_width(size)
            y = row * row_height(size)
            
            #print(x)
            drawHex(offx+x, offy+y, size)
            #draw.text((offx+x, offy+y), ""+str(row)+","+str(col)+ "T"+str(T(6)), align ="center", fill="black")
            drawTileInfo(offx+x, offy+y, size)


readData()
startDoc(3508, 2480)

hexGrid(18)
# do the PIL image/draw (in memory) drawings
#draw.line([0, center, width, center], green)

endDoc()
