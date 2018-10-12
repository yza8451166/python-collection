# __anthor:  "xuchen:
# date:   2018/3/12
# import redis
# pool=redis.ConnectionPool(host='162.218.211.180',port=6379,password='xc123456')
# r=redis.Redis(connection_pool=pool)
#
# r.set('foo','Bar')
# r.set('foo2','xc')
# print(r.get('foo2'))

# add = lambda x,y:x+y
# add(1,2)
# x =1
# y=2
#
# print(x if(x>y) else y)
#
# list4 =[2*n+1 for n in range(3,11)]


# from multiprocessing import process
# import time
# def f(name):
#     time.sleep(1)
#     print('hello',name,time.ctime())
#
#
# if __name__=='__main__':
#     p_list=[]
#     for i in range(3):
#         p=process(target=f,args=('alvin',))
#         p_list.append(p)
#         p.start()
#     for i in p_list:
#         p.join()
#     print('end')
# def reverse():
# #     s=input("input content :")
# #     return s[::-1]
# # print(reverse())
def gen():
    value = 0
    while True:
        receive = yield value
        if receive == 'e':
            break
        value = 'got: %s' % receive


g = gen()
print(g.send(None))
print(g.send('hello'))
print(g.send(123456))
print(g.send('e'))
