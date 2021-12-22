import random
character=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'!','”','$','%'	,'&','’','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@']


def caeser():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode':
        encode()
    elif direction == 'decode':
        decode()
    else:
        print('wrong input!')
        caeser()



def encode():
    end_text=""
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    for char in text:
        position=character.index(char)+shift
        if shift>47:
            end_text+=character[position]-47
        else:
            end_text+=character[position]
    print(end_text)

def decode():
    end_text=""
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    for char in text:
        position = character.index(char) -shift
        if shift>47:
            end_text+=character[position]-47
        else:
            end_text+=character[position]
    print(end_text)

caeser()




