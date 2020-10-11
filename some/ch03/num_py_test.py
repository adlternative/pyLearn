import numpy as np


def test1():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a)

    b = np.random.random((2, 2))
    print(b)

    x = np.empty([3, 2])
    print(x)

    x = np.zeros(5)
    print(x)
    y = np.zeros((5,), dtype=np.int)
    print(y)
    z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
    print(z)

    x = np.ones(5)
    print(x)

    x = np.ones([2, 2], dtype=int)
    print(x)

    x = [1, 2, 3]
    a = np.asarray(x)
    print(a)
    x = np.arange(5)
    print(x)  # [0  1  2  3  4]

    print(x.ndim)
    print(x.shape)
    print(x.size)
    print(x.dtype)
    print(x.itemsize)
    print(x.flags)
    print(x.real)
    print(x.imag)
    print(x.data)


def test2():
    # 3  修改
    arry = np.array([1, 2, 3, 4, 5])
    # arry[2]=10
    arry[0:2] = 8
    # print(arry)


def test3():
    a = np.array(
        [
            [
                [1, 2, 3],
                [4, 5, 6]
            ],
            [
                [1, 2, 3],
                [2, 4, 5]
            ]
        ]
    )
    print(a[0, 1])
    print(a.shape)
    print(a[:, 0:2])  # 任意0维,1维索引0~2
    # print(a[:, 1:2])
    print(a[a > 2])
    a[a > 2] = 0
    print(a)
    x = np.array([[1,  2],  [3,  4],  [5,  6]])
    y = x[[0, 1, 2],  [0, 1, 0]]
    print(y)


def test4():
    # t = [5 6 7 3 8 9 7 3 8 8 1 2 8 2 4 0 6 7 4 3 9 3 6 2 9 1 3 7 1 2 6 7 4 5 0 9 1
    #      9 4 0 0 5 9 5 2 9 8 3 7 4 8 1 4 4 0 2 5 7 7 1 5 7 2 0 3 0 5 4 7 1 4 7 5 5
    #      5 2 1 3 5 5 1 7 5 0 5 8 9 4 9 8 3 2 4 9 1 2 1 1 3 9]
    t=np.random.choice(4,2)

    print(t)
    b = np.arange(12).reshape(3, 4)
    print(b)
    print(b[np.arange(2), t])
        #第0列选择index=1
        #第1列选择index=2
        #第3列选择index=1

if __name__ == '__main__':
    test4()
