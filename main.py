A = [5, -3, 7, -8, 4, -2, 9, -1]

min_index = A.index(min(A))
max_index = A.index(max(A))

start = min(min_index, max_index)
end = max(min_index, max_index)

negative_sum = 0
for x in A[start + 1:end]:
    if x < 0:
        negative_sum += x

print("Массив:", A)
print("Минимальный элемент:", A[min_index], "индекс:", min_index)
print("Максимальный элемент:", A[max_index], "индекс:", max_index)
print("Сумма отрицательных элементов между ними:", negative_sum)
