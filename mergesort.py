def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        print(f"array: {arr}")
        print(f"m: {m}")

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        print("Merging...")
        print(f"left: {left}")
        print(f"right: {right}")

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        print(f"merged: {arr}")

if __name__ == "__main__":
    user_input = input("Enter numbers, separated by ',': ")
    input_list = user_input.split(',')
    print(f"input_list: {input_list}")

    value_list = list(map(int, input_list))
    print(f"value_list: {value_list}")

    merge_sort(value_list)
    print(value_list)
