# Escoolhe o Termo do Wikipedia
def askAndReturnSeachTerm():
    return 'Michael Jackson'  # input("Choose a term of Wikipedia: ")


# Escolhe o prefixo a ser pesquisado
def askAndReturnPrefix():
    menu = {1: 'What is ', 2: 'Who is', 3: 'The history of '}
    for i in menu:
        print(i, ':', menu[i])
    prefix = 3
    # prefix = int(input("Choose one option: "))
    return menu[prefix]
