vowels = "ёйуеыаоэяию"

print("Введите стихотворение в одну строку, разделенную пробелами")
poem=input()

def cnt_vowels(word):
    return list(map(lambda x: x in vowels, word)).count(True)

if len(set(map(cnt_vowels, poem.split())))==1:
    print('Парам пам-пам')
else:
    print('Пам парам')






'''
#poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
cnt_first_word=cnt_vowels(poem.split()[1])
ret='Парам пам-пам'
for i in poem.split():
    if cnt_vowels(i)!=cnt_first_word:
        ret='Пам парам'

print(ret)
'''