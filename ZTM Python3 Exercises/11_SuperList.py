class SuperList(object):
    def __init__(self, *args):
        self._items = list(args)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'SuperList({self._items})'

    def append(self, value):
        self._items.append(value)

    def remove(self, value):
        self._items.remove(value)

    def pop(self, index=-1):
        return self._items.pop(index)


super_list = SuperList(1, 2, 3, 4, 5)
# Example usage
print(super_list)  # Output: SuperList([1, 2, 3, 4, 5])
super_list.append(6)
print(super_list)  # Output: SuperList([1, 2, 3, 4, 5, 6])
super_list.remove(3)
print(super_list)  # Output: SuperList([1, 2, 4, 5, 6])
print(super_list[0])  # Output: 1
print(len(super_list))  # Output: 5
super_list[1] = 10
print(super_list)  # Output: SuperList([1, 10, 4, 5, 6])
print(super_list.pop())  # Output: 6
print(super_list)  # Output: SuperList([1, 10, 4, 5])
# Example of using the SuperList class
print(super_list[2])  # Output: 4
# Example of iterating through the SuperList
for item in super_list:
    print(item)  # Output: 1, 10, 4, 5 (each on a new line)


class SuperList2(list):
    def __len__(self):
        return 999


super_list2 = SuperList2()
print(len(super_list2))  # Output: 999
# Example usage of SuperList2
super_list2.append(1)
super_list2.append(2)
super_list2.append(3)
print(super_list2)  # Output: [1, 2, 3]
print(len(super_list2))  # Output: 999
print(super_list2[0])  # Output: 1
print(issubclass(SuperList2, list))  # Output: True
print(issubclass(list, object))  # Output: True
print(isinstance(super_list2, list))  # Output: True