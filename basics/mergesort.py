def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def mergesort(array):
    if len(array) <= 1:
        return array

    print("array:", array)
    m = len(array) // 2
    print("m:", m)

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    merged = merge(left, right)
    print("Merging...")
    print("left:", left)
    print("right:", right)
    print("merged:", merged)
    return merged

if __name__ == "__main__":
    numbers = input("Enter numbers, separated by ',': ").split(',')
    value_list = [int(n.strip()) for n in numbers if n.strip()]
    print("input_list:", numbers)
    print("value_list:", value_list)
    sorted_list = mergesort(value_list)
    print(sorted_list)
