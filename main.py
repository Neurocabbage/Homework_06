'''Дан список интов, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
 Примеры:
[1,4,5,2,3,9,8,11,0] => »0–5,8–9,11»
[1,4,3,2] => "1–4"
[1,4] => "1,4"'''

# arr1 = [1, 4, 5, 2, 3, 9, 8, 11, 0]
# arr2 = [1, 4, 3, 2]
# arr3 = [1, 4]
#
#
# def shrink(arr):
#     print(arr)
#     a = sorted(arr)
#     print(a)
#     str1 = str(a[0])
#     iteration = False
#     for i in range(1, len(a)):
#         if a[i - 1] + 1 == a[i]:
#             iteration = True
#         else:
#             if iteration == False:
#                 str1 += ', ' + str(a[i])
#             else:
#                 str1 += '-' + str(a[i - 1]) + ', ' + str(a[i])
#                 iteration = False
#     if iteration:
#         str1 += '-' + str(a[a.length - 1])
#     return str1
#
#
# print(shrink(arr1))

'''Дана строка, состоящая из букв A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида:
A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения:
Если символ встречается 1 раз, он остается без изменений;
Если символ повторяется более 1 раза, к нему добавляется количество повторений.'''


def convert(string):
    check = lambda string: not all('A'<=x<='Z' for x in string.upper())
    try:
        if check != True:
            print('строка должна состоять из букв A-Z:')
        else:
            result = []
            last_sym = string[0]
            count = 0
            for sym in (list(string)):
                if last_sym and sym != last_sym:
                    if count == 1:
                        result.append(last_sym)
                    else:
                        result.append(last_sym + str(count))
                    count = 1
                    last_sym = sym
                else:
                    count += 1
            return ''.join(result)
    except:
        print('Какая-то ошибка')


s = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
w = 'цвфцукфффффв'
print(convert(w))
