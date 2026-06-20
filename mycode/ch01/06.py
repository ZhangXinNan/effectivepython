
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]


def bubble_sort2(a):
    for _ in range(len(a)):
        for i in range(len(a) - 1, 0, -1):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]



names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)


arr = [3, 1, 5, 4, 2, 6, 7]
bubble_sort(arr)
print(arr)
bubble_sort2(arr)
print(arr)
