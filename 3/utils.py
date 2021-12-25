def read_bits(file: str):
    with open(file, encoding='utf8') as f:
        lines = f.readlines()
        return _create_2d_array(lines)


def _create_2d_array(lines: [str]):
    return list(map(lambda x: list(x.strip()), lines))
