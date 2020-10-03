def lines(file):
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):  # 取出每一行
        if line.strip():  # 去除前空格后非空
            block.append(line)
        elif block:
            yield (''.join(block).strip())
            block = []


if __name__ == '__main__':
    for item in blocks(open('c.txt')):
      print(item)
