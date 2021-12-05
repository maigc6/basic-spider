import A
name =input("查询书的名字:")
page = int(input("要看第几页:"))
A.liblist(name,page)
num = int(input("输入bookId,查询详情:"))
A.data(num)
A.picture(num)