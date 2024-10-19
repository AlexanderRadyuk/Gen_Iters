

class FlatIterator:

    def __init__(self, list_to_iter):
        self.list_to_iter = list_to_iter

    def __iter__(self):
        self.cursor = -1
        self.aux_cursor = 0
        self.flat_list = []
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.list_to_iter):
            raise StopIteration
        if isinstance(self.list_to_iter[self.cursor], list): # проваливаемся во влож список
            while self.aux_cursor < len(self.list_to_iter[self.cursor]): # проходим по индексам влож списка
                self.flat_list.append(self.list_to_iter[self.cursor][self.aux_cursor])
                self.aux_cursor += 1
            self.aux_cursor = 0
        else:
            self.flat_list.append(self.list_to_iter[self.cursor])

        return self.flat_list




def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    print(list(FlatIterator(list_of_lists_1)))