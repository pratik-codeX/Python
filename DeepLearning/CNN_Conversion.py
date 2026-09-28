from PIL import Image


img = Image.open("digit.png")
print(img.size)

img = img.convert("L")      #Grayscale
img = img.resize((28,28))

img.save("digit_28x28.png")

print(img.size)