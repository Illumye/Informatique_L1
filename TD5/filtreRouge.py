def filtreRouge(img):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (r, 0, 0))