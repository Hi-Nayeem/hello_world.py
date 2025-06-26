def merge_sort(array):
    if len(array) > 1:
        m = len(array) // 2
        print(f"m: {m}")

        left = array[:m]
        print(f"array: {left}")
        merge_sort(left)

        right = array[m:]
        print(f"array: {right}")
        merge_sort(right)

        print("Merging...")
        print(f"left: {left}")
        print(f"right: {right}")

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        print(f"merged: {array}")

if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")
    print(f"input_list: {input_str.split(',')}")
    
    value_list = list(map(int, input_str.split(',')))
    print(f"value_list: {value_list}")
    
    array = value_list
    print(f"array: {array}")

    merge_sort(array)
    print(array)
