''' Изучить и реализовать алгоритм сортировки вставками.
Напишите функцию, которая будет сортировать массив. '''

array = [21,23,3,5,1,45]  # Произвольный массив


def arr_sort(array):	  # Функция сортировки вставками
    for i in range(1, len(array)):
        y = array[i]
        j = i-1
        while j >=0 and y < array[j] :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = y
    return array 
print (arr_sort(array))   
