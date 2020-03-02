import sys


def main():
    if len(sys.argv) == 3:
        pixel_values, width, height = parse_file(sys.argv[1])

        # if the argument is a text file, it must be loaded before preceding
        if ".txt" in sys.argv[2]:
            string = read_file(sys.argv[2])
        else:
            string = sys.argv[2]
        pixel_values = encode(pixel_values, string)
        write_image_file(pixel_values, width, height)
    elif len(sys.argv) == 2:
        pixel_values, width, height = parse_file(sys.argv[1])
        string = decode(pixel_values)
        write_text_file(string)
    else:
        print('ENCODE: python3 embed_string.py <image> <string or text_file>')
        print('DECODE: python3 embed_string.py <image>')


def read_file(file):
    """
    opens a text file for reading
    :param file:  the file to open
    :return:  a string of text to encode
    """
    try:
        fin = open(file)
    except FileNotFoundError:
        print('Unable to open ', file)
        exit(1)
    string = ''
    for line in fin:
        string += line
    fin.close()
    return string


def parse_file(file):
    """
    opens and loads information from the given PPM file
    :param file:  the file to load
    :return:  a tuple of pixel_values and the width and height of the image
    """
    pixel_values = []
    try:
        fin = open(file)
    except FileNotFoundError:
        print('Unable to open', file)
        exit(1)
    fin.readline()
    dimensions = fin.readline().split()
    fin.readline()
    for line in fin:
        pixel_values.append(int(line[:-1]))
    fin.close()
    return pixel_values, int(dimensions[0]), int(dimensions[1])


def write_image_file(pixel_values, width, height):
    """
    writes a list of pixel values to a PPM file
    :param pixel_values:  an array of pixels in the PPM
    :param width:  the width of the image
    :param height:  the height of the image
    :return:
    """
    fin = open('output.ppm', 'w')
    fin.write('P3\n')
    fin.write(str(width) + ' ' + str(height) + '\n')
    fin.write(str(255) + '\n')
    for value in pixel_values:
        fin.write(str(value) + '\n')
    fin.close()


def write_text_file(string):
    """
    writes the string to a text file
    :param string:  the string to write
    :return: void
    """
    fin = open('output.txt', 'w')
    fin.write(string)
    fin.close()


def encode(pixel_values, string):
    """
    encodes a string in a given image
    :param pixel_values:  an array of pixel values from the PPM
    :param string:  the string to encode
    :return:  an array of pixel values from the PPM with the string encoded
    """
    # Store the string length (decode key) in the first position
    pixel_values[0] = len(string)
    step = len(pixel_values) // len(string)
    if step < 1:
        print('Choose a larger image to encode this string')
        exit()

    # loop through and set each pixel value to the character's ord() value
    for index in range(len(string)):
        pixel_values[step * index + 1] = ord(string[index])
    return pixel_values


def decode(pixel_values):
    """
    extracts a string from an image
    :param pixel_values:  an array of pixel values from the PPM
    :return:  the extracted string
    """
    string = ""

    # gets the decode key which is set at the first pixel
    step = len(pixel_values) // pixel_values[0]

    # loop through and get each character from the pixel value at each step
    for index in range(1, pixel_values[0] + 1):
        string += chr(pixel_values[(index - 1) * step + 1])
    return string


if __name__ == '__main__':
    main()
