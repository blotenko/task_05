# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# 1 Дано целое число (int). Определить сколько нулей в этом числе.
def countZero(n):
    if (n == 0):
        print(1)
        exit()

    num_zeroes = 0
    for num in str(n):
        if num == '0':
            num_zeroes=num_zeroes+1
    #print(num_zeroes)
    return num_zeroes
# 2 Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
def countEndZero(n):
    if (n == 0):
        print(1)
        exit()

    countZero = 0
    while (n % 10 == 0):
        n //= 10
        countZero += 1
    #print(countZero)
    return countZero
# 3 Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
def task_03():
    my_list_1 = [1,3,5,7]
    my_list_2 = [2,4,6,8]
    my_result = []
    j = 1
    for i in my_list_1:
        if j % 2 ==0:
           my_result.append(i)
        j=j+1
    j = 2
    for i in my_list_2:
        if j % 2 ==0:
           my_result.append(i)
        j=j+1

    return my_result

# 4 Dан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]


def task_04():
    my_list=[1,2,3,4,5]
    new_list= []
    new_list.insert(0,my_list[len(my_list)-1])
    for i in my_list:
        if i == my_list[len(my_list)-1]:
            break
        new_list.append(i)

    return new_list

# 5 Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

def task_05():
    my_list=[1,2,3,4,5]
    n = len(my_list)-1
    my_list.insert(n,my_list.pop(0))
    my_list.insert(0, my_list.pop(n-1))
    return my_list
# 6 Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

def task_06(s):
    total, current = 0, ''
    for ch in s:
        if ch.isdigit():
            current += ch
        elif current != '':
            total += int(current)
            current = ''
    if current != '':
        total += int(current)
    return total
# Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

def task_07():
    my_str = "My long string"
    l_limit = "o"
    r_limit = "g"
    num1 = []
    num2 = []
    sub_str=""
    i = 0
    for symbol in my_str:
        if(symbol == r_limit):
            num1.append(i)
        if (symbol == l_limit):
            num2.append(i)
        i = i + 1
    max = 0
    maxid=[]
    for n in num1:
       for m in num2:
           if max < n -m:
               max = n-m
               maxid*=0
               maxid.append(n)
               maxid.append(m)

    i =maxid[1]+1
    while i < maxid[0]:
        sub_str = sub_str+my_str[i]
        i = i+1
    print(sub_str)


# Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

def task_08():
    my_str="abcdfs"
    leng = len(my_str)
    spisok = []
    i = 0
    if leng % 2 ==0:
        while i < leng:
          spisok.append(my_str[i]+my_str[i+1])
          i = i+2
    else:
        while i < leng:
            if i+1 == leng:
                spisok.append(my_str[i]+'_')
            else:
               spisok.append(my_str[i]+my_str[i+1])
            i = i+2

    print(spisok)


# Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

def task_09():
    num = [2,2,1,5,3,9,0,7]
    count = 0
    i =1
    while i < len(num)-1:
        if num[i]>num[i-1]+num[i+1]:
            count+=1
        i+=1
    print(count)



if __name__ == '__main__':
    n = 300400
    print("1: ",countZero(n))
    print("2: ", countEndZero(n))
    print("3: ", task_03())
    print("4: ", task_04())
    print("5: ", task_05())
    print "6: ", task_06("43 больше чем 34 но меньше чем 56")
    task_07()
    task_08()
    task_09()








