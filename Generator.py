Encode = {'a': 'c',
          'b': 'd',
          'c': 'e',
          'd': 'f',
          'e': 'g',
          'f': 'h',
          'g': 'i',
          'h': 'j',
          'i': 'k',
          'j': 'l',
          'k': 'm',
          'l': 'n',
          'm': 'o',
          'n': 'p',
          'o': 'q',
          'p': 'r',
          'q': 's',
          'r': 't',
          's': 'u',
          't': 'v',
          'u': 'w',
          'v': 'x',
          'w': 'y',
          'x': 'z',
          'y': 'a',
          'z': 'b',
          ' ': ' ',
          '\'': '\''}


Decode = {'c': 'a',
          'd': 'b',
          'e': 'c',
          'f': 'd',
          'g': 'e',
          'h': 'f',
          'i': 'g',
          'j': 'h',
          'k': 'i',
          'l': 'j',
          'm': 'k',
          'n': 'l',
          'o': 'm',
          'p': 'n',
          'q': 'o',
          'r': 'p',
          's': 'q',
          't': 'r',
          'u': 's',
          'v': 't',
          'w': 'u',
          'x': 'v',
          'y': 'w',
          'z': 'x',
          'a': 'y',
          'b': 'z',
          ' ': ' ',
          ',': ',',
          '\'': '\''}


def encode():
    txt = str(input('Enter your words to encode, Please note to start with a space'))
    secret = ''
    for i in txt:
        if i in Encode:
            secret += Encode[i]
    print(secret)
    ask()


def decode():
    global txt, secret
    txt = str(input('Enter your words to decode, Please note to start with a space'))
    secret = ''
    for y in txt:
        if y in Decode:
            secret += Decode[y]
    print(secret)
    ask()


def ask():
    global UserInput
    UserInput = str(input('decode or encode?'))
    if UserInput == 'decode':
        decode()
    elif UserInput == 'encode':
        encode()
    else:
        print('Invalid input, please try again')
        ask()


ask()
