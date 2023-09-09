from PIL import Image


INPUT_FILE_NAME = 'images/scarlett.png'
OUTPUT_FILE_NAME = 'images/out3_one_bit.png'


def process_image() -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load()
        width,height = input_file.size
    output_image = Image.new('1', (width, height))
    pixout = output_image.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixin[x,y]
            avg = (r+g+b)//3
            if avg < 128:
                pixout[x,y]=(0)
            else:
                pixout[x,y] = (1)
    output_image.save(OUTPUT_FILE_NAME)


if __name__ == '__main__':
    process_image()