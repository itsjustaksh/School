def foo(lis):
    item0 = lis[0]
    item1 = lis[1]
    lis[1] = 'updated1'

    print(item0, item1, lis)


lis = ['original0','original1','original2']
foo(lis)

print(lis)