# Text Encoder
I created this project, because I was learning about PPM files and how they store each pixel value in an array. I thought it would be cool to alter a file to hide information in a picture. This is a clever way to communicate secretly online. Since this program has a unique way of running, the only way to decode the image is to run it through the same program that encoded it.

## Planned Features

- Allow for multiple file formats (PNG, JPEG...)
- Allow custom offsets to make the encoding more secure

## Getting started
```shell script
git clone https://github.com/khevamann/text-embed.git
cd text-embed

# To encode a file
python3 embed_string.py <image> <string or text_file>

# To decode a file
python3 embed_string.py <image>
```

### Here is a sample run
Running the below script will encode the text file sample.txt into the image sample.ppm. The images below show the before and after. As you can see it is hard to notice the encoded string. 

```shell script
python3 embed_string.py sample.ppm sample.txt
```

Without String             |  With String Encoded
:-------------------------:|:-------------------------:
![Input Image](docs/sample.jpg) |  ![Output Image](docs/output.jpg)

> If you zoom in really close on the right image you can see the pixels that are altered with text. You will see some pixels that are clearly not the right color. However this is very hard to notice if not looking for it. To make it even more discrete you can use a larger image.



