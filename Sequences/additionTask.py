
class Sort:
    def __init__(self):
        self.sort_list = []
        n = input('Enter some numbers, split "Enter": ').split()
        for item in n:
            self.sort_list.append(item)

    def sorting(self):
        sort_list = self.sort_list
        sort_list = sorted(sort_list)
        return sort_list


sort = Sort()
print(sort.sorting())

