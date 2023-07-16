import random
txt = ''
secret = ''
UserInput = ''
enc = 0


def encrypt():
    global enc
    enc = random.randint(2, 50)


def encode():
    global txt, secret
    txt = str(input('Enter your words to encode'))
    secret = ''
    for i in txt:
        secret += chr(ord(i) + enc)
    print(secret)
    ask()


def decode():
    global txt, secret
    txt = str(input('Enter your words to decode'))
    secret = ''
    for y in txt:
        secret += chr(ord(y) - enc)
    print(secret)
    ask()


def ask():
    global UserInput
    UserInput = str(input('decode or encode?'))
    if UserInput == 'decode':
        decode()
    elif UserInput == 'encode':
        encrypt()
        encode()
    else:
        print('Invalid input, please try again')
        ask()


ask()
