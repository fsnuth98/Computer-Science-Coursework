from images import *

file_name = "llamas.gif"
#file_name = "uc_sweatshirt.gif"
#file_name = "Triumph_T100_Boy_Racer_1971.gif"

# Load image into memory
picture = Image(file_name)

# Visit every pixel in the image
for y in range(0, picture.getHeight()):
    for x in range(0, picture.getWidth()):
        r,g,b = picture.getPixel(x, y)
       
        # Manipulation of pixels happens here.
        # r, g an b should have values between 0 and 255.

        picture.setPixel(x, y, (50,50,50))
        
picture.draw()
