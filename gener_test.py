def flat_generator(list_to_flatten):
    cursor_main: int = 0
    cursor_aux: int = 0
    for _ in list_to_flatten:
        cursor_main += 1
        if isinstance(list_to_flatten[cursor_main - 1], list):
            while cursor_aux < len(list_to_flatten[cursor_main - 1]):
                # print('111', cursor_aux, len(list_to_flatten[cursor_main - 1]))
                cursor_aux += 1
                yield list_to_flatten[cursor_main - 1][cursor_aux - 1]
            else:
                cursor_aux = 0
            continue
        else:
            # cursor_main += 1
            yield list_to_flatten[cursor_main - 1]



if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    print(list(flat_generator(list_of_lists_1)))

