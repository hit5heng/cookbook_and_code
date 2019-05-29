"""
快速排序
"""
def quicksort(array):
    if len(array) < 2:
        return array  # 基线条件： 空或者之后一个元素的数组是有序的
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


a01 = [12,45,7,98,0,34,12,54,6,99]
a01_sorted = quicksort(a01)
print(a01_sorted)


"""
选择
"""
def order_by(target, condition):
    """
    按照某一参数排序 类似 sorted(list, key = lambda:..., reverse=True)
    :param target:
    :param condition:
    :return:
    """
    # new_list = target  #（新建列表，不动原列表）
    for r in range(len(target) - 1):
        for c in range(r + 1, len(target)):
            if condition(target[r]) > condition(target[c]):
                target[r], target[c] = target[c], target[r]
    # return new_list

def order(target):
    for r in range(len(target) - 1):
        for c in range(r + 1, len(target)):
            if target[r] > target[c]:
                target[r], target[c] = target[c], target[r]


a01_sorted = order(a01)
print(a01)
