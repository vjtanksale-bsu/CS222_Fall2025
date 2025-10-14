def BinarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False