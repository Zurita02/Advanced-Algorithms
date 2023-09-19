from PIL import Image, ImageMode
import sys
import re

# Declare the inputs and outputs
# Exception: The name of the file was not provided as a command line argument.
try:
    INPUT_FILE_NAME = sys.argv[1]
except IndexError:
    print('The name of the file was not provided as a command line argument.') 
    quit()
# INPUT_FILE_NAME = "scarlett.png"

# Regex to extract the name of the input file
regex_list = re.findall(r"([^\.]+)\.png$", INPUT_FILE_NAME)

try:
    filename = regex_list[0]
except IndexError:
    print('The provided file name doesn’t have a .png extension.')
    quit()

OUTPUT_FILE_NAME_RED = filename + '_channel_1_red.png'
OUTPUT_FILE_NAME_GREEN = filename + '_channel_2_green.png'
OUTPUT_FILE_NAME_BLUE = filename + '_channel_3_blue.png'

# except IndexError:
#     print('Index out of range')
    
def process_image() -> None:
    try:
        with Image.open(INPUT_FILE_NAME) as input_file: # With guarantees that when we finish opening the resource, at the end will close it.
            # print(input_file.mode)
            pixin = input_file.load()
            width, height = input_file.size
    except FileNotFoundError:
        print(f'No such file or directory: {INPUT_FILE_NAME}')
        quit()

    output_image_red = Image.new('1', (width, height)) # Create an image that doesn't exists for the red channel
    output_image_green = Image.new('1', (width, height)) # Create an image that doesn't exists for the green channel
    output_image_blue = Image.new('1', (width, height)) # Create an image that doesn't exists for the blue channel

    # Load the images to fill them up with the least significative bit of each channel
    pixout_red = output_image_red.load() 
    pixout_green = output_image_green.load()
    pixout_blue = output_image_blue.load()

    # Go through all the bits of the original image
    for y in range(height):
        for x in range(width):
            try: 
                r, g, b = pixin[x, y]
            except TypeError:
                print(f'The image isn\'t in RGB, so it can\'t be unpacked. It is in: {input_file.mode} mode.')
                quit()

            # Get the least significative bit
            r_lb = (r & 1)
            g_lb = (g & 1)
            b_lb = (b & 1)

            # Fill the images up with each lsb
            pixout_red[x, y] = r_lb
            pixout_green[x, y] = g_lb
            pixout_blue[x, y] = b_lb

    # Saving the output images
    output_image_red.save(OUTPUT_FILE_NAME_RED)
    output_image_green.save(OUTPUT_FILE_NAME_GREEN)
    output_image_blue.save(OUTPUT_FILE_NAME_BLUE)


if __name__ == '__main__':
    process_image()
