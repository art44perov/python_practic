import random

def generate_psw(len):
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&?><(){}[]_+=/*'
    psw = ['0'] * len
    psw = [random.choice(a) for x in psw]
    print(''.join([str(elem) for elem in psw]))

