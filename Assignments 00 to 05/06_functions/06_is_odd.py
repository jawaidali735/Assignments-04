#10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def main():
    for i in range(10):
        if is_odd(i):
            print( i ,'odd')
        else:
            print(i ,'even')


def is_odd(value):

    remainder = value % 2
    return remainder == 1

if __name__ == '__main__':
    main()