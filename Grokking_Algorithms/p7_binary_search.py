def binary_search(target_list, num):
    """
    list is a sorted list
    num to search
    :return:
    """
    low = 0
    high = len(target_list) - 1
    step = 0
    while low <= high:
        mid = (low + high) // 2
        guess = target_list[mid]
        step += 1
        if guess == num:
            print(step)
            return mid
        elif guess < num:
            low = mid + 1
        elif guess > num:
            high = mid - 1
        else:
            return None


list01 = [1,2,3,4,5,6,7,8,9]
print(binary_search(list01, 6))
