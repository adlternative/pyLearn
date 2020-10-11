```
    t=np.random.choice(4,3)

    print(t)
    b = np.arange(12).reshape(3, 4)
    print(b)
    print(b[np.arange(3), t])
        #第0列选择index=1
        #第1列选择index=2
        #第3列选择index=1
```

其中`b[np.arange(3), t]`
选取b中0~3行每一行分别取`index=t[i]`,需要满足条件为`b[arr1,arr2] arr1.shape[0]==arr.shape[1]`




