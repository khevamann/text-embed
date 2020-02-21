import sys


def main():
    if len(sys.argv) == 3:
        pixel_values, width, height = parse_file(sys.argv[1])
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
        print('ENCODE: python embed_string.py <image> <string or text_file>')
        print('DECODE: python embed_string.py <image>')


def read_file(file):
    try:
        fin = open(file)
    except FileNotFoundError:
        print('Unable to open', file)
    string = ''
    for line in fin:
        string += line
    fin.close()
    return string


def parse_file(file):
    pixel_values = []
    try:
        fin = open(file)
    except FileNotFoundError:
        print('Unable to open', file)
    fin.readline()
    dimensions = fin.readline().split()
    fin.readline()
    for line in fin:
        pixel_values.append(int(line[:-1]))
    fin.close()
    return pixel_values, int(dimensions[0]), int(dimensions[1])


def write_image_file(pixel_values, width, height):
    fin = open('output.ppm', 'w')
    fin.write('P3\n')
    fin.write(str(width)+' '+str(height)+'\n')
    fin.write(str(255)+'\n')
    for value in pixel_values:
        fin.write(str(value)+'\n')
    fin.close()


def write_text_file(string):
    fin = open('output.txt', 'w')
    fin.write(string)
    fin.close()


def encode(pixel_values, string):
    pixel_values[0] = len(string)
    step = len(pixel_values)//len(string)
    if step < 1:
        print('Choose a larger image to encode this string')
        exit()
    for index in range(len(string)):
        pixel_values[step*index+1] = ord(string[index])
    return pixel_values


def decode(pixel_values):
    string = ""
    step = len(pixel_values) // pixel_values[0]
    for index in range(1, pixel_values[0]+1):
        string += chr(pixel_values[(index-1)*step+1])
    return string


if __name__ == '__main__':
    main()
