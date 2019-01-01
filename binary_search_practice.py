#binary search practice

A = [-1,2,5,20,90,100,207,800]
B = [50,90,3,-1,207,80]

n = len(B)
C = n * [0]
finish_point = n * [0]
print(C)
for i in range(n):
    search = B[i]
    r = len(A)
    l = 0
    while l < r:
        mid = (l+r) // 2
        if search == A[mid]:
            C[i] = 1
            break
        if search > A[mid]:#关于循环会卡住，要让循环终结。其实这个关键点也很好找，l对应4，r对应6，你要search5，就看这个卡住的点，因为左侧的点肯定比过了，所以就让左边更进一步
            l = mid + 1
        else:
            r = mid
    # 当然，本例没必要用这种方法，这种方法应该还能拿出最后一个元素进行一些处理
    # 而且我这样找法，根据移动l和移动r不同，可以做不同的操作?????NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #4,6之间找5，如果是移动l，最后找到的是6，移动r，最后找到的是4??不光是这样，看下边的例子!!!!!!!!!!!!
    else:#只是打印出来作为对比
        print('l is ',l)
        finish_point[i] = A[l]#找到的都走不到这个循环，所以对应元素是0

print(C)
print('finish_point 1:',finish_point)

#这个例子其实不对，移动右边不能代替移动左边，因为你比较的是左边的点，所以默认最好是移动左边，要么两边一起动
# 调整r的起点也不太对，最好别用这种方法，有点问题，要是想让r=mid-1，最好也让l=mid+1，l的操作必不可少！！！
#临界时，比的就是l，不移动l怎么能行，除非颠倒一下mid的计算方法，拿r去比。
'''
n = len(B)
C = n * [0]
finish_point = n * [0]
print(C)
for i in range(n):
    search = B[i]
    r = len(A) - 1
    l = 0
    count = 10
    while l < r:

        print('loop search:',search,' l:',l,' r:',r)
        mid = (l+r) // 2
        if search == A[mid]:
            C[i] = 1
            break
        if search > A[mid]:#关于循环会卡住，要让循环终结。其实这个关键点也很好找，l对应4，r对应6，你要search5，就看这个卡住的点，因为左侧的点肯定比过了，所以就让左边更进一步
            l = mid
        else:
            r = mid - 1
        count -= 1
        if not count:
            break
    # 当然，本例没必要用这种方法，这种方法应该还能拿出最后一个元素进行一些处理
    # 而且我这样找法，根据移动l和移动r不同，可以做不同的操作
    #4,6之间找5，如果是移动l，最后找到的是6，移动r，最后找到的是4
    else:#只是打印出来作为对比
        print('l is ',l)
        finish_point[i] = A[l]#找到的都走不到这个循环，所以对应元素是0

print(C)
print('finish_point 2:',finish_point)
'''




# 如果只想要结果，找得到还是找不到，那么用<=更好

n = len(B)
C = n * [0]
print(C)
for i in range(n):
    search = B[i]
    r = len(A)
    l = 0
    while l <= r:
        mid = (l+r) // 2
        if search == A[mid]:
            C[i] = 1
            break
        if search > A[mid]:#关于循环会卡住，要让循环终结。其实这个关键点也很好找，l对应4，r对应6，你要search5，就看这个卡住的点，因为左侧的点肯定比过了，所以就让左边更进一步
            l = mid + 1
        else:
            r = mid - 1
    else:#只是打印出来作为对比
        print('l is ',l)
        print('but nothing was found')

print(C)



















