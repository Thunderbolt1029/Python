from PIL import ImageGrab

image = ImageGrab.grab()
color = image.getpixel((840, 516))

(r, g, b) = color

print(color)
print(r, g, b)
