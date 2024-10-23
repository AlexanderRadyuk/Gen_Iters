class FlatIterator:

    def __init__(self, list_to_iter):
        self.list_to_iter = list_to_iter
        self.cursor = -1
        self.list_len = len(self.list_to_iter)

    def __iter__(self):
        self.cursor += 1
        self.aux_cursor = 0
        # self.flat_list = []
        return self

    def __next__(self):
        if self.aux_cursor == len(self.list_to_iter[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.aux_cursor += 1
        return self.list_to_iter[self.cursor][self.aux_cursor - 1]



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
    test_1()
