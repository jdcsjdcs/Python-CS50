import sys
from PIL import Image, ImageOps
import os


def main():

    check_arg()

    try:
        my_image = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("File does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    my_image_sized = ImageOps.fit(my_image, size)
    my_image_sized.paste(shirt, shirt)
    my_image_sized.save(sys.argv[2])

def check_arg():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    ext = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])

    if (ext1[1] not in ext) or (ext2[1] not in ext):
        sys.exit("Invalid output")

    elif ext1[1] != ext2[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
