

import types


def flat_generator(list_to_flatten):
    cursor_main: int = 0
    cursor_aux: int = 0
    for _ in list_to_flatten:
        cursor_main += 1
        if isinstance(list_to_flatten[cursor_main - 1], list):
            while cursor_aux < len(list_to_flatten[cursor_main - 1]):
                cursor_aux += 1
                yield list_to_flatten[cursor_main - 1][cursor_aux - 1]
            else:
                cursor_aux = 0
            continue
        else:
            yield list_to_flatten[cursor_main - 1]


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
