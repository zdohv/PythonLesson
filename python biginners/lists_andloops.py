""" list, loops, for, while """

# list()
# list- (списки) - колеция элеиентов. изменяемый упорядеченный индексируемый итерируемый тип данных 
# используется для хронения наюора элементов 

# элементами мписка могут быть любые типы данных

# list_with_all_data_types = [1, 'string', True, False, None, [1,2], {'a': 10 }, {1,2}, ('a', 1,'b')]

# list_of_numbers = [1, 2, 3, 4, 5, [6, 7]]
# list_of_numbers[0]
# list_of_numbers[1]
# list_of_numbers[5][1]

#   a = [1, 2, 3]
# print('до', a)
# a.append(4)
# print('после', a)

# a.insert(1,0.5)
# print(a)
# a.insert(index, element)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# new_list = list1 + list2
# print(new_list)


""" заменв элемнтов """
letters = ['a', 'b', 'c', 'd']
letters [3] = 'g'
# print(letters)


# """ удалене элементов """

letters = ['a', 'b', 'c', 'd']
letters.pop(2)
# print(letters)


letters = ['a', 'b', 'c', 'd']
deleted_el = letters.pop(2)
# print(deleted_el)

letters = ['a', 'b', 'c', 'd']
deleted_el = letters.pop()
# print(deleted_el)

letters = ['a', 'b', 'c', 'd']
letters.remove('a')
# print(letters)
# letters.remove('g')

# letters.clear()
# print(letters)

# del letters[1]
# print(letters)

""" сортировка и копирование списка """

nums = [1, 2, 3, 4]
nums_copy = nums.copy()
nums_copy2 = nums[:]

# nums = [1, 2, 3, 4]
# nums2 = nums
# nums2.append(5)
# print(nums2)
# print(nums)
# print(nums is nums2)

nums_list = [8, 6, 10, 5]
nums_list.sort()
nums_list.sort(reverse=True)
# print(nums_list)

# name = ['kolya', 'Oma', 'Ivan', 'Emil']
# new_name = sorted(names)
# print(new_name)

""" циклы """

# цикл - многократн6ое выполнение опрудуленного учасмтка кода

# итерируемый обект - обьктб к котророму монжо применить цикл

# 1)for
# nums_list = [1, 2, 3, 4, 5]
# for num in nums_list:
    # print(num)


# for - цикл который перебивает каждый элемент в интеррируемом обекте  и работвет до тех пор пока эти элементы не закончятся
# for элемент in интерируемый _об:
# теле цикла

# string = 'Hello world'
# for letter in string:
    # print(letter)






# nums = range(10)
# for num in nums:
    # print(num)

# new_nums = []
# for num in range(1, 21):
#     if num % 2 == 0:
#         new_nums.append(num)

# print(new_nums)

list_of_lists = [[1, 2, 3], ['Katya', 'Masha', 'Sanya'], [4, 5, 6]]

# for list_ in list_of_lists:
#     for element in list_:
#         print(element)


# for element in list_of_lists[-1]:
    # print(element)


# while условие 
#  while цикл клторый работает до тех пор пока условие возврящяе True

# import time

# counter = 0
# while counter < 5:
#     print('counter')
#     print('hello world')
#     counter += 1
#     time.sleep(1)

# while True:
    # print('hello world')

#  CTRL + c останоыка бесконечного цикла/процесса
# msg = input('введите сообщение тлт стоп')
# while msg !='stop':
    # print(f'ваше сообщение\n{msg}')
    # msg = input('введите сообшение тлт stop:

# while True:
#     msg = input('сообщение или стоп')
#     if msg =='ятоп':
#         print('цонкл остоновлен')
#         break
#     print(msg)


# break - опертор для остановку цикла
# continue начинает цикл заново пропуская остальные тело цикла


# a = 'privetik'
# b = ''
# for letter in a:
#     if letter == 'i':
#         continue
#     b += letter

# print(b)


""" else в циклах  """
nums = range(0, 101, 2)
result = 0
for num in nums:
    if num == 50:
        break
    result += num
else:
    print(result)