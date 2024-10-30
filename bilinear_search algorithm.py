# Алгоритм билинейного поиска
array = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(array,
'\n 0  1  2  3  4   5   6   7   8   9   10')
target = int(input('Введите элемент, индекс которого надо найти: '))
def bilinear_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        if array[left] == target:
            return f'(Нашел left)Элемент {target} найден на индексе {left}'
        if array[right] == target:
            return f'(Нашел right)Элемент {target} найден на индексе {right}'    
        if array[left] < target:
            left += 1
        
        if array[right] > target:
            right -= 1
        
    if left > right:
        return 'элемент не найден'
    
print(bilinear_search(array, target))