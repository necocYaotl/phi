import hanged


def main():
    state = hanged.valid('l', 'hello')
    print(state)
    state = hanged.valid('frrrr', 'hello')
    print(state)
    state = hanged.valid('4', 'hello')
    print(state)
    state = hanged.valid('hello', 'hello')
    print(state)
    state = hanged.valid('b', 'hello')
    print(state)

    hangedMan = hanged.hangedMan(1)
    print(hangedMan)



if __name__ == '__main__':
    main()
