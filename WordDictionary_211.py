# 设计一个支持以下两种操作的数据结构：
# #
# # void addWord(word)
# # bool search(word)
# # search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
# #
# # 示例:
# #
# # addWord("bad")
# # addWord("dad")
# # addWord("mad")
# # search("pad") -> false
# # search("bad") -> true
# # search(".ad") -> true
# # search("b..") -> true
# # 说明:
# #
# # 你可以假设所有单词都是由小写字母 a-z 组成的。



# 这题的感受是，估计python的dict用的好，会有捷径。
# 如果只有Trie，大概的思路就是DFS穷举。
# 如果要优化，感觉就从Trie的层入手，但是Trie目前使用的是单向结构，需要优化成双向结构，这样....d就可以从第五层的d往上找，或者说只要第五层有d，并且d是end，就算找到了，这里只要true和false。
# 这个链接我觉得省倒是省不掉，纯用层来办这个事应该是办不到，..a..b..c，不能只搜索三个对应层就确定单词是否存在，他们可能不在一条线上，
# 另一种“好”方法，当然是映射全都确定，这样第三层的第N个d，能映射到第二层某一个下标，这个就能确定一条线，但是这个空间无限大，估计不允许的。





#其实就是用的野蛮方法
# 暴漏的问题：都是按C++的逻辑走的，不够python，这个传参word属于复制了
TRIE_MAX_CHAR_NUM = 26

class TrieNode:
    def __init__(self):
        self.child = [None] * TRIE_MAX_CHAR_NUM
        self.is_end = False
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
        # return self.root
    def get_root(self):
        return self.root

    def get_all_word_from_trie(self, stack, result):
        self.__get_all_word_from_trie(self.root,stack,result)#把独立函数复制到类中，再把原来函数的root直接改成self.root来递归就不正确了，所以先套一层
    def __get_all_word_from_trie(self,root, stack, result):#这个root只是子树root，习惯而已，要不就叫node
        for i in range(TRIE_MAX_CHAR_NUM):
            if root.child[i]:
                stack.append(chr(ord('a') + i))
                self.__get_all_word_from_trie(root.child[i], stack, result)
                stack.pop()
        if root.is_end:
            result.append(''.join(stack))
    def addWord(self,word):
        ptr = self.root
        n = len(word)
        for i in range(n):
            if not ptr.child[ord(word[i]) - ord('a')]:
                ptr.child[ord(word[i]) - ord('a')] = self.__new_node()
            ptr = ptr.child[ord(word[i]) - ord('a')]
        ptr.is_end = True



    def search(self,word):
        return self.__search(self.root,word)
    def __search(self,node,word):
        #如果到这一层word已经空了，直接看node.is_end，循环不进入
        # 不能默认是word先结束，以为for循环不会再进去，可能word过长，所以这里必须提前判定。
        #for循环结束需要返回false，被word过长的情况给占用了，所以必须在前边先做id_end的处理
        if not word:
            return node.is_end

        n = len(word)
        # print('word is ',word)
        if word[0] == '.':#另外，循环结构也不一样，改递归了，没有那个for循环了，for循环是.内部的逻辑
            for i in range(TRIE_MAX_CHAR_NUM):
                # if node.child[ord(word[i]) - ord('a')] and self.__search(node.child[ord(word[i]) - ord('a')],word[1:]):#这是个严重错误，我在遍历寻找哪个子节点存在，和word[i]有毛关系，word不一定有这么长，i是0~25，
                if node.child[i] and self.__search(node.child[i],word[1:]):
                    return True
        else:
            # print('else')
            if node.child[ord(word[0]) - ord('a')] and self.__search(node.child[ord(word[0]) - ord('a')], word[1:]):
                # print('word is ',word,' return true')
                return True
        # return node.is_end#wrong
        return False

    def __new_node(self):
        # print('new node')
        return TrieNode()

#
t1 = WordDictionary()
t1.insert('hahah')
# # print(t1.search('hahah'))
# # print(t1.search('haha'))
# print(t1.search('hahaha'))
print(t1.search('haha.'))
print(t1.search('.aha.'))
print(t1.search('...a.'))
print(t1.search('ha.'))
print(t1.search('ha...'))



# word = 'a'
# print(word[1:])
# print(not word[1:])
# print(word)
#
#
# child = [0] * 26
# print([ord('e') - ord('a')])
# print(child[ord('e') - ord('a')])