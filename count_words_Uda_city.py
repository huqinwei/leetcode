"""Count words."""
# 优达学城的，过不去，但是我觉得完全没有什么道理，凭什么答案是死的？bitter和betty都出现一次。如果非要按什么字母比较的话，a也不该出现？a好像算出现1次中最小的
#只能在最后一个做比较了？
#不能在第n-1个做比较，可能n-2也不是想要的，他想要字符最小的a和betty，我如果先输出bought，后边把bitter换成betty也是错
#或许他的样本就这么小，他想要的，只是直接split出几个数组，然后去重，不同的出现频率扔在不同的heap？然后heap内再比较排序？
# Evaluating...
# [FAILED] Wrong word found: 'bitter' where it should be 'betty'
# Inputs: ('betty bought a bit of butter but the butter was bitter', 3)
# Output: [('butter', 2), ('a', 1), ('bitter', 1)]

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    top_n = []
    dict = {}
    # TODO: Count the number of occurences of each word in s
    s = s.split()
    word_freq_cnt = 0
    for word in s:
        if dict.get(word,0) == 0:
            dict[word] = 1
        else:
            dict[word] += 1
            word_freq_cnt = max(word_freq_cnt,dict[word])
            # print('word_cnt:',word_freq_cnt)

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    heap = [[] for i in  range(word_freq_cnt)]
    # print('heap:',heap)
    print('dict:',dict)
    for word in dict:
        heap[dict[word]-1].append(word)
        # print(heap)
    for h in heap:
        h.sort()
    print('sorted:',heap)

    for i in range(len(heap)-1,-1,-1):
        # print(heap[i])
        for j in range(len(heap[i])):
            # print(heap[i][j])
            top_n.append((heap[i][j],i+1))
            n -= 1
            # print('n is ',n)
            if 0 == n:
                return top_n##两层循环的问题，break不好用
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))
    print(count_words('a bb bb ccc ccc ccc dddd dddd dddd dddd', 2))


if __name__ == '__main__':
    test_run()





#实测，只用一个key，无论如何也排不出来
d = {'beautiful':10,'beaa':15,'beaw':10,'wonderful':12,'love':17}

# d = {'bought': 1, 'bitter': 1, 'bit': 1, 'the': 1, 'was': 1, 'but': 1, 'betty': 1, 'a': 1, 'butter': 2, 'of': 1}

content = list(d.items())
print(content)


content.sort(key=lambda x:x[0])
print(content)
content.sort(key=lambda x:x[1])
print(content)
content.sort(key=lambda x:x[1],reverse=True)
print(content)

