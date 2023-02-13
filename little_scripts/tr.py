# # d = range(1, 7)
# # print(d)
# #
# # for i in d:
# #     print(d)
#
# # b = a =='5'
# # print({a=='5':'5'})
#
#
# c=[x ** 2 for x in range(10)]
# # c = [1,2,4,5,6]
# # print([x for x in c if x % 2 == 0])
# # print(filter(lambda el: el == 5, c))
# # print(map(lambda el: el * -1, c))
# # print(c)
# # c.extend(7)
# # print(c)
#
# print(c)
# print(c.pop())
# c.pop()
# print(c)
# c.pop()
# print(c)
# print(c.pop())
# print(c)


# def append_list(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = append_list(10)
# list2 = append_list(123, [])
# list3 = append_list('a')
# print(list1, list2, list3)


a={'a':1,'b': 2}
print(a.get('a',0))
print(a.get('c',0))
print(a.get('e',1))
a.setdefault('d',0)
print(a)
