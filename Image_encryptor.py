from PIL import Image

def encrypt_image(path):
    img = Image.open(path)
    pixels = img.load()
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)  # invert RGB

    img.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

encrypt_image("input_image.png")