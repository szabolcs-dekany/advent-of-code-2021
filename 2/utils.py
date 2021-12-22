def read_directions():
    with open('input.txt', encoding='utf8') as f:
        lines = f.readlines()
        return list(map(_create_tuple_from_line, lines))


def _create_tuple_from_line(s: str):
    split_text = s.strip().split(" ")
    return split_text[0], int(split_text[1])
