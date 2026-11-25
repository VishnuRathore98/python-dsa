def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)    # sort left of pivot
        quick_sort(arr, p + 1, high)   # sort right of pivot


def partition(arr, low, high):
    pivot = arr[high]    # choose last element as pivot
    i = low - 1          # boundary of the "smaller than pivot" zone

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # move small element into the zone

    arr[i + 1], arr[high] = arr[high], arr[i + 1]   # place pivot after the zone
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)   # [1, 5, 7, 8, 9, 10]
