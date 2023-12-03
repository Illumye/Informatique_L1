from PIL import Image
from filtreRouge import filtreRouge

def solideRec(img: Image, x1: int, x2: int, y1: int, y2: int, color: tuple) -> None:
    for x in range(x1, x2):
        for y in range(y1, y2):
            img.putpixel((x, y), color)

def filtreBleu(img: Image):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (0, 0, b))

def filtreVert(img: Image):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (0, g, 0))
            
def monochrome(img: Image):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            moy = int(0.3 * r + 0.59 * g + 0.11 * b)
            img.putpixel((x, y), (moy, moy, moy))
            
def binarisation(img: Image):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            moy = int(0.3 * r + 0.59 * g + 0.11 * b)
            if moy < 128:
                img.putpixel((x, y), (0, 0, 0))
            else:
                img.putpixel((x, y), (255, 255, 255))


def blur(img: Image):
    largeur, hauteur = img.size
    
    b1 = Image.new("RGB", (largeur, hauteur))
    
    for y in range(1, hauteur-1):
        for x in range(1, largeur-1):
            
            r_moy, g_moy, b_moy = 0, 0, 0
            for y1 in range(y-1, y-2):
                for x1 in range(x-1, x-2):
                    r, g, b = img.getpixel((x1, y1))
                    r_moy += r
                    g_moy += g
                    b_moy += b
            b1.putpixel((x, y), (r_moy//9, g_moy//9, b_moy//9))

def ajustementLineaire(img: Image, a, b):
    for x in range(img.width):
        for y in range(img.height):
            r, g, blue = img.getpixel((x, y))
            img.putpixel((x, y), (int(a * r + b), int(a * g + b), int(a * blue + b)))

def histogramme(img: Image):
    histo = [0] * 256
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            moy = int(0.3 * r + 0.59 * g + 0.11 * b)
            histo[moy] += 1
    return histo

def normalisationSimple(img: Image):
    histo = histogramme(img)
    min = 0
    while histo[min] == 0:
        min += 1
    max = 255
    while histo[max] == 0:
        max -= 1
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            moy = int(0.3 * r + 0.59 * g + 0.11 * b)
            img.putpixel((x, y), (int((moy - min) / (max - min) * 255), int((moy - min) / (max - min) * 255), int((moy - min) / (max - min) * 255)))
            
def normalisationGlobale(img: Image):
    # exploite les statistiques globales de l'image tel que la moyenne d'intensité et l'écart type
    # J(x, y)= (I(x, y) - moyenne) / écart type
    # moyenne = somme des intensités / nombre de pixels
    # écart type = racine carrée de la somme des (intensité - moyenne)² / nombre de pixels
    # on peut aussi utiliser la variance qui est égale à l'écart type au carré
    moyenne = 0
    for x in range(img.width):
        for y in range(img.height):
            moyenne += img.getpixel((x, y))[0]
    moyenne /= img.width * img.height
    ecartType = 0
    for x in range(img.width):
        for y in range(img.height):
            ecartType += (img.getpixel((x, y))[0] - moyenne) ** 2
    ecartType /= img.width * img.height
    ecartType **= 0.5
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (int((r - moyenne) / ecartType * 255), int((g - moyenne) / ecartType * 255), int((b - moyenne) / ecartType * 255)))

def nettoyerFondIndesirable(img: Image):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            if r > 100 and g > 100 and b > 100:
                img.putpixel((x, y), (255, 255, 255))
            else:
                img.putpixel((x, y), (0, 0, 0))
                
def translationPixelToLeft(img: Image, xi, yi, xf, yf, value):
    for y in range(yi, yf+1):
        for x in range(xi, xf+1):
            col = img.getpixel((x, y))
            if x >= value:
                img.putpixel((x-value, y), col)
            img.putpixel((x, y), (0, 0, 0))
             
                       

livre = Image.open("livre.jpg")
lion = Image.open("lion.png")
translationPixelToLeft(lion)
lion.show()
