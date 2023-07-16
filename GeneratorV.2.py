txt = ''
secret = ''
UserInput = ''


def encode():
    global txt, secret
    txt = str(input('Enter your words to encode, Please note to start with a space'))
    secret = ''
    for i in txt:
        secret += chr(ord(i) + 2)
    print(secret)
    ask()


def decode():
    global txt, secret
    txt = str(input('Enter your words to decode, Please note to start with a space'))
    secret = ''
    for y in txt:
        secret += chr(ord(y) - 2)
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
