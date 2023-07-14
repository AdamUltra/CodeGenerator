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
          ' ': ' '}


def encode():
    txt = str(input('Enter your words to encode, Please note to start with a space'))
    secret = ''
    for i in txt:
        if i in Encode:
            secret += Encode[i]
    print(secret)
    encode()


encode()
