import base64, codecs

chars = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

with open("al.png", "rb") as imagefile:
    b = imagefile.read()

for i in chars:
    with open(i + "l.png", "wb") as outputfile:
        outputfile.write(b)