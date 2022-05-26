''' Изучить и реализовать алгортм бинарного поиска
в отсортированном массиве. '''

array = [1,2,3,44,55,56,67,88,99,988] # Произвольный массив 


def BinarySearch(array, num):   # Функция поиска
    first = 0
    last = len(array)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if array[mid] == num:
            index = mid
        else:
            if num<array[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print (BinarySearch(array, 44)) # Вывод на экран индекса заданного числа в массиве