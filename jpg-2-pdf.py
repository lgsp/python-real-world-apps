from PIL import Image

source_path = input("Enter the path to get the jpg file you want to convert:\n")
image_name = input("Enter the image name: ")

if source_path[-1] == '/':
    source_image = source_path + image_name
else:
    source_image = source_path + '/' + image_name

img = Image.open(r"{si}".format(si=source_image))

imgg = img.convert("RGB")

target_path = input("Enter the target path to store the pdf:\n")
new_image_name = input("Enter the image name: ")

if source_path[-1] == '/':
    target_image = target_path + new_image_name
else:
    target_image = target_path + '/' + new_image_name

img.save(r"{ti}".format(ti=target_image))

print("Image saved as pdf")
