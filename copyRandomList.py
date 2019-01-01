#   复制带随机指针的链表
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
#
# 要求返回这个链表的深度拷贝。



# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution(object):
    def copyRandomList_failed(self, head):#不通过，因为还可能有向前指的，计数器这招不好用。
        new_head = RandomListNode(0)
        q = new_head
        p = head
        while p:
            new = RandomListNode(p.label)
            q.next = new
            q = new
            #new.random = p.random#这才是终点，这个random不能指向原来的.现在又没有后边的point，只能加一些计数器之类的，然后整个表建完再赋值random
            # 计数方法，让一个point1指向p.next，让一个point2去找next，直到point1 == point2或者point1 == None就不用了
            # 可以先用random存住这个值，下次循环拿出这个值，然后当做计数找到目标指针。
            if p.random:
                target = p.random
                iter = p
                count = 0
                cnt = 0
                while iter:
                    cnt += 1
                    if iter == target:
                        count = cnt
                        break
                    iter = iter.next
                print('count:',count)
                if count == 0:#reverse
                    iter = p
                    while iter and iter != target:
                        count -= 1
                        iter = iter.prev#问题是不存在prev，虽然没有prev，但是random朝前是可以的。
                q.random = count
            else:
                q.random = None
            p = p.next
        q = new_head.next
        while q:
            if q.random:
                target_cnt = q.random
                iter = q
                while target_cnt:
                    iter = iter.next
                    target_cnt -= 1
                q.random = iter
            q = q.next
        # p = head
        # while p:
        #     # print('before:', p.label)
        #     p = p.next
        # p = new_head.next
        # while p:
        #     print('after:', p.label)
        #     if p.random:
        #         print('p.random.val:',p.random.label)
        #     p = p.next

        if new_head.next:
            return new_head.next
        return None
# 方法二：充分利用原始链表的信息，不用保存原始链表的映射关系，构建新节点时，指针做如下变化，即把新节点插入到相应的旧节点后面（参考）：
#     RandomListNode *copyRandomList(RandomListNode *head) {
#         if (!head)
#             return NULL;
#
#         //首先，复制原始的节点，连接自身后面
#         RandomListNode *p = head;
#         while (p)
#         {
#             RandomListNode *tmp = new RandomListNode(p->label);
#             //保存后续节点
#             RandomListNode *r = p->next;
#
#             tmp->next = r;
#             p->next = tmp;
#
#             p = r;
#         }//while
#
#         //然后，将添加的节点random 链接到原始节点random的下一个位置
#         p = head;
#         while (p)
#         {
#             RandomListNode *q = p->next;
#             if (p->random == NULL)
#                 q->random = NULL;
#             else{
#                 q->random = p->random->next;
#             }//else
#             //处理下一个原始节点
#             p = q->next;
#         }//while
#
#         //最后，恢复原始链表，得到新链表
#         RandomListNode *ret = head->next;
#
#         p = head;
#         RandomListNode *q = head->next;
#         while (q->next)
#         {
#             p->next = q->next;
#             p = q;
#             if (q->next)
#                 q = q->next;
#         }
#         p->next = NULL;
#         q->next = NULL;
#         return ret;
#     }
# 或者干脆用哈希表，道理和我之前做的一样，只不过不是简单往前往后找，直接记住“下标”

# 其实很简单，每一个节点后接一个跟屁虫，l2（l1.next）的random就是l1.random.next。
# 最后，错位分拆回去，random是不影响整体结构的。

    def copyRandomList(self, head):#不通过，因为还可能有向前指的，计数器这招不好用。
        if not head:
            return None
        p = head
        while p:
            q = RandomListNode(p.label)
            q.next = p.next
            p.next = q
            p = q.next
        p = head
        while p:
            if p.random and p.next:
                p.next.random = p.random.next
            p = p.next.next
        p = head
        while p:
            # print('before:', p.label)
            # if p.random:
            #     print('p.random.val:', p.random.label)
            p = p.next
        p = head
        head2 =p.next
        while p and p.next:
            q = p.next
            p.next = p.next.next
            p = p.next   #watch out: not p.next.next
            if p:
                q.next = p.next

        return head2








node1 = RandomListNode(1)
node2 = RandomListNode(2)
node3 = RandomListNode(3)
# node22 = RandomListNode(22)
# node23 = RandomListNode(23)
node1.next = node2
node1.random = node3
node2.next = node3
node3.random = node1


# p = node1
# while p:
#     print('before:', p.label)
#     if p.random:
#         print('p.random.val:',p.random.label)
#     p = p.next
s= Solution()
ret = s.copyRandomList(node1)
print('ret:',ret)


p = ret
while p:
    print('after:', p.label)
    if p.random:
        print('p.random.val:',p.random.label)
    p = p.next


