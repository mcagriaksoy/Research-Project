import webcolors
from PIL import Image

def closest_colour(average_color):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - average_color[0]) ** 2
        gd = (g_c - average_color[1]) ** 2
        bd = (b_c - average_color[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(average_color):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(average_color)
    except ValueError:
        closest_name = closest_colour(average_color)
        actual_name = None
    return actual_name, closest_name

def resize(img):
    basewidth = 100
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('camres.jpg')

def compute_average_image_color(imgres):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total/count, g_total/count, b_total/count)

img = Image.open('cam.jpg')
resize(img)
imgres = Image.open('camres.jpg')
#img = img.resize((50,50))  # Small optimization
average_color = compute_average_image_color(imgres)
actual_name, closest_name = get_colour_name(average_color)
print(average_color)
print "Actual colour name:", actual_name, ", closest colour name:", closest_name