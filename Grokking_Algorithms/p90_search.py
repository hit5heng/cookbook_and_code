import collections

def search(name):
    """
    广度优先搜索
    deque()双向队列: append(往右边添加一个元素), appendleft（往左边添加一个元素）
    :param name:
    :return:
    """
    search_queue = collections.deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == name:
                print("this is the person we searched", person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False




graph = {}
graph["a"] = ["a1", "a2", "a3"]
graph["b"] = ["b1", "b2", "b3"]
graph["c"] = ["a1", "b2", "c3"]

search("c")