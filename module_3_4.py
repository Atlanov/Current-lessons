print('Самостоятельная работа по уроку "Произвольное число параметров"')


def single_root_words(root_word, *other_words):
    same_words = []
    print(f'Root word: {root_word}')
    for i in range(0,len(other_words)):
        if other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])
        elif root_word.lower() in other_words[i].lower():
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('be', 'beer', 'bear', 'Robert', 'breget', 'molbert')
result2 = single_root_words('extradition', 'tradition', 'Extra', 'Trader','on','out')
print('Result 1:', result1)
print('Result 2:', result2)
