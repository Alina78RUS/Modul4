''' Изучить и реализовать алгортм бинарного поиска
в отсортированном массиве. '''

array = [32,2,43,44,12,56,72,67,88,33,98] # Произвольный массив 

array.sort()

print (array)

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