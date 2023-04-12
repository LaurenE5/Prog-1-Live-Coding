def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

insertion_sort(numbers)

print(numbers)
