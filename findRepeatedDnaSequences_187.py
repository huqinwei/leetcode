# 所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。

hash_map = 1048576 * [0]
#最简单的方法就是遍历，把所有长度10的都扔进dict
class Solution(object):
    def findRepeatedDnaSequences_myself(self, s):
        n = len(s)
        result = []
        if n < 10:
            return result
        dict = {}
        for start in range(0,n-9):
            # print(s[start:start+10])
            if dict.get(s[start:start+10],0) == 1:#只在刚刚达到二次时添加
                result.append(s[start:start+10])
            dict[s[start:start+10]] = dict.get(s[start:start+10],0) + 1
            print(dict)
        print(result)
        return result
 #别人的提交，名列前茅的时间，改成了set就快了这么多？还是说，因为用了两个set，导致set很小，很好查？注意if语句，首先是看seen，其实如果量级很大，repeat会更多？我也不会改成if in repeat对比了，逻辑不一样。而且其实他seen是没有动态删除的，所以，并不是因为这个。如果seen删了，这个逻辑反而不对，除非先查repeat
    def findRepeatedDnaSequences_fast(self, s):
        seen = set()
        repeat = set()
        N = len(s) - 9
        for i in range(N):
            if s[i:i+10] in seen:
                repeat.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])
        return list(repeat)

    # 最后一种方法，是把DNA序列通过位操作改成整数，依然是做哈希，。。。4个字母，10个长度，一个整数能覆盖。太繁琐，没有本质上快吧？
    # 另外，这个位操作可以练编程熟练度。
    # 利用了DNA序列的特性。# 不是数量级上的优化，但是略微减少了存储空间。
    # 10字符的字符串，能用一个整数搞定，4
    # 的10次方，32位足够。
    #吐槽一点，他虽然变整型，map搜索可能快了？但是他最后还要遍历一遍map才输出，而不是像前两种方法，前边查询过程就完成了result的整理
    #这个方法在leetcode直接超时或者报内存
    def change_int_to_DNA_str(self,DNA):#这是为了输出result，用来做转换的。
        ret = ''
        char_map = ['A','C','G','T']
        for i in range(10):
            ret += char_map[DNA % 4]
            DNA = DNA >> 2
        return ret

    def findRepeatedDnaSequences(self, s):
        # hash_map = 1048576*[0]
        global hash_map
        result = []
        n = len(s)
        if n < 10:
            return result
        char_map = 128*[0]
        char_map[ord('A')] = 0
        char_map[ord('C')] = 1
        char_map[ord('G')] = 2
        char_map[ord('T')] = 3
        k = 0
        print(s[0:10])
        for i in range(9,-1,-1):#init k
            print(s[i])
            k = k << 2#把进位放前边，后边就不用补回来了，反正刚开始是0，左移不影响
            k += char_map[ord(s[i])]
        print(k)
        # print(g_hash_map)
        print(len(hash_map))
        hash_map[k] = 1
        # for i in range(1,n-9)#wrong!!!!!!!!!!!!!!!!
        for i in range(10,n):#每次只需要拿一个字符就能变k，所以从第[10]个开始,前边init占了前10个
            k = k >> 2
            change = char_map[ord(s[i])]<< 18
            k = k + change
            hash_map[k] += 1
        for i in range(len(hash_map)):
            if hash_map[i] > 1:
                result.append(self.change_int_to_DNA_str(i))
        return result


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "CCGGCCGGCCGGCCGG"
# s = "AAAAAAAAAA"
s = "CCAAGTCTAAAAGAATGGGCAGAGTTGCTCTGCACGTTCCGGATACGATAAGAAGACTCCGCCGGGCACCGCCAGTCCCTCGCAGGGGGACACATTGGAATCGGATAATCGATCACTCCGCGCCACCCCGGGTTACGCACCTCACGTTGAGTGAGGAGATGGTGACATTTCGGCACCTATAGGCACGCTCTACCGGAACAGCATCTGTATCAGATGGCAATTCGATGGTATCTTGCGTGAATCAGGAAGTTTTATGTGGCTTCCGGATGACGCGAGATTTTGCGTGAGGTGAGCGGTTGCGTTACCGGTTAGTAGCCCTTAGTAGTTGAAGACAGGCGAGCAGGTGCAGCTGTCCACACGGTATAGGGCAATCAACTTCCATAAAGCATATGTTGTGTAACACCTGCCACCCCTTGTCACAGGTTTCACCAAGACCACATCGTGCTAAAGTTAAACAACATTCGTAAAAGTGCAGAAATTGAAGTATTTGATCTGAGATTACGTTTCAATCTGGAATCCGAAGCTATAGGAGAATGTTGGACCATACGGTGAGTAGAATCGCCACTCACGTTTCGGTACTAGCACATTAGTACGGATCCCGATCGGGGTGGTGGGGCGTTCTTCATGTATACCATTGCGACGGAGTCTGGCTAAACCTTTAGGCAGGTCGCAAGGCAGAATCATGAGCACAATCAGGGTGGCCTGGATCCGTCATGGAGGAATCGGGTCTTCCCGTTTGAGGGGGCGGACTTCGCGGCGCACGTCAGGACACCAAAGGCTCTAGTACCCTCCTATCGAAACTCTTTAGCGAGTTTTGTCCAGCTAGCTTCATCTAACAGGCTCAAAAGTCATAAGAAGGCTCACTTTAAGTAAAAAGTCAGGCGCAAAGTCTAGTGGCGCATTTGATACGTTCCCAGGGCACACATGCACCCCTCTGCAACATTTCAGGCCGCAATTACACTGTAGCTCACCGGGGTCGAAATAGTTAACTCAAGTTTCCGGTCCCTTCCCCACAAAGATCTGTATATGAACCATCAAGACGTGGCTAATAATTATATCTCCGGCCCCTGCCACAGGAGAGAGGGAGCCGGAATGACCGTAATTAGCTCATAAAACTTACCAGCTTATAGGAAGTCGGCTTCTTTGATGACTACGAAATGGTAGGGCGTTCGTTATGTGCTCTCGCGTTCAACATCCGGCGCGACCAATATGCCAACATTCGGAAGCGTGTGATAAATTGCTGAATCCATAGTCCCATAGTGGTTGATAGTTACTCCGGTTCTGAACTTGTGTAATAAATGCCAACATTCTCGTTACTCAGAACGACAGTCAAAGTGCGTGTCACGTTGGGCCTGGGGCACGTCGCTGGTATTCGGGTACTTTACTAATGAATAAGGATTGTGTTGTAGGCCCCTTAAAAACAGGGAATGGGCCGAATACATTTAGCTTGATTCCAGCGGTAGTACTTGGCGGAGTCATGTACCTTACCCGCGCATATAACTCCAGTCGGACATACGTTAGAATTTTGAAAAGGCTGGCGGGGACCGCGAGATGTCCGCCACCCATGTCGCGGCGTGAGGTGACATGACAGCCAGGCAGTTGGCTCGGTGTCCCAGGTGCACGGCCTCACTTAAACTAGCACCCGACGGATTCTTCATACCTGACGTGTGTATTTTTTGACTCTGAGGTTCTGAATAACATCCGTAGGCACATGTGAGAGCAGGGACGGTTCATCACCTATGGTCTCCAGGTACAGCCTACGTGGGGTAGGACCACAACACTCTGTGTGCCATACGGTCGGTCAAGACCTAATGGCGGGAAAAGTGGCTTTAGTCCCGTTGTACGAGGGAAATCAGTTTGGTTACGTGAAAAGTTAATGCTGCATCCAGTGACTACGATATTACCCGGCGAAACGAGATCGTAGTAGTTCTATGTCGGGCTGTCACCTAAGACACCATAAAAGGCGATTAAATATGGATGTGCGGAAGGGTGACTTCTACCCTCAAGACAACTGACTACCACCTTATACGCGCTTCATCGGGAGCTAGCGAGGCGCATCGCACAGTTACAAAGGGGTGTGGTAGGCACCCTGAACACAGAGAGTCACGCCGTGGGAAGACGACGGCGCCCGAACTGCTATCAGCTTCAAACTTCCAACGCCCATCGCGAGCGTACTGAGTTTTCACAGCGGGCTTCCACAAAGAAGTGGCCAGGCGACACCACATTACTGGGTCTGAGCCTCAGGCCAGGCGAAGTAATTGGTTTTGTGGGAATAGTGCACAAATGACCCATATGTGTTGTCAAGTCCCCTGCGACCGTTCGTCGGCGTACCCTTCGCTAATTTCCTAAGCACAATAATTGCAACCCCAAATGAGTCTCGTATTAGAGTAACGCAGAGTTAGGCTCCCCGAAAACGCTAGTCCGGAGCTTGGGATAAAAATAATGATGTAGGGCGGGACCCCGTACTTTCGCATAACAGGGTTTTTGTCGGTTGGCTTGTAAATGCAACTTGGGTTCCACAATCCCACTGGACAAGACAGGAAGGTGAAGAGGGAGCCGATTAAACCCAACTCAACTAGAACTTAGATCTTTCATTCACATCGTGTCAGTACAAATTTGAAAGAGAAGTAGGTACATGGGAGGAACGGGTTACGCCGAGTCTGATATTCTGTGGGAACTCCGTCTGGTCGCAGAGTTACGCCATCACAGCATTGGCTGAGTATCCAATTTGCCTATCACGCAACTACCATTTGCCGATAGCGGACCGACCCTATTTGAGCTATGGTATGTTCACGAATACAACTACGTCTGACAAGACGAGATCCTAAGCACAACTCCTACGATTCCGGACGTCTGGCCCTTGGAGCACTAATCCCTGGGGAATGTCACCAGAGATGTTTACGGCATGAAGAATGGAGGTCACAATTATTGAGAGACGGCGGTATGCACCATATCCAGGGTGCAGTGAGACGATAGACGTAGGGGAGCGGAGCGTCGAGGTGTCTCTGCCAAAGGGCCCCAATGATCCTGAATGGTGTAATCCGGAGACTCGATGGTATCCGCCGCAACGGTTCACTCCGCGTATGGCAGTTGGCTACGTGGTCGCGAGGACAGCTGTACGTTAAGCTAAACGATCCCTTAGCCTCTCGCAGATCGAAGTGCTAATAGTCCTGTCGCAGCCAGGATTGCGAAACTACGACTCAGGGGTAATCGCGGATAGCCTGATTTCATCCGAAAGACCCACACTATAGTCTGTGGTCGGTCCCAGGCGGTTCACGCCACCGGCGACATCGGCAAGTCTACAGGGGTTGGGCCAATTTCCGATAGGATCTCGGAAATGGTATCTCCGACCAGCGCAAACGCGCCACCCTGCGAGTCCGGAGTTTGCTACTCTTCAAATGAACCGATCGCGTCGTCGTTGAAACCGTGAGAGCAACCAGAATTACATTAAGCTCATCGGGATATTGATCCAATTGGGTAAATGTCAACGCTTCAATTTTTGCCGTGTCGCAACCTCCGGATAAACTTAGTACAGATCTTTTGTCGTAGAACGTTGTGGAAGCAGCAGGGAGACCCTGTACTTTCGTCACCTATCAACGTTTCCACCTCTGGTGATGTAAAAGCACGCAACCTACTCCGATACCAATCTGAGTTATGCTGTAAATTATTGGACGCCAATGGGATAAATGGGTAACGTGACCGATACGAAGCTGGCCCTTTCTCCCTCCAGTACCGATGGAATCTAGTACTTTTATAATGATTGGCACGGACGCACCGGTGTGGTTGACCGATTTGGCGGTAACATTGCGGGTTAGGGGGTTAATATATAACGCCTTCACCGATCGCACTACACGCAGATCGGAGGCTCCACTCAGACGTAGAATTTAAACAGAGATGGCTAGCGAAACTCCAAGCAGACGGCAAGGCTGTTCACCAGGAAGCCCCCTTCAAGATTCGTATTCAGGTATTGAGCAAACATCACTGACATTATTTTTGGATTAGCATAGGAAATATATACCGACTCGCGGTGGAGGTCAATGTCAACAGTGCGTGTTTTTAATGTCTGAACAATTTGCCTCCAAAATCTTGTTCGTTATCTCCCGATCAATTACCGCTAGCATTCGGGCATCTTGCGACCCAAGATTGAGATGAGGTGTGAACACTATCTGCACTGACAGCGGTCATAGCGGCGTAAAAATCGTGCGGAGGGAACCTTCACTCATGAGCAGCGGTGTAAAACCCTATGAGACAATTCGCTCCGATGGATAGTGTTGCGCTGACGTCCCACCGGACCAGCAGATATTCAACTCGAGAACATCTTAAAGTTTCCATCTAGGGCGGACCCTCAGGCTTTGCACGTCGGGGCTTAATGGTAATATGAGGTACGATTTAGTCGAATGGTTAAAGACCGTGACCGTGATATGCGCAACAATTCCCTCTGATACCCACTCATCGGGGTGGATTCTGAACACAGTCTGCATAAGTCTCAACCCATGGACGGGGAACTGTTACGAAATATGCAGGGGTCCGATTAGTCCCAGGGTGAGTCTTCCCTTACCGATCTCCACCGTGTTCCATGAGTCGCCGGTGTTTGATTACTGTCTATAGGCCTTACCGTCGTTACTGAGATTTATGGGCGGGGACGTTCGACTGCACTTTCAATTGGCAGAATTCCGTTAAATAAGGACGCAGTTGTCCGCGCACTTCATACCGTTGAGAAAGCAATACATTTTCTTGACACTCCCGGCATGTCGTCATATAGTACCGTCTAGCATTCTGCTAGCTCAAAAGCTCTCTGGCACCGGCATGTGTGACGTATCGAAAGAACAGCACTACAGCAGGCGAGTAGCTCCGGGCTACTTTGTTGCACAGCTACATGCAGTGGTGGTAACTTCGATTGATCCCGGCTCTAGGACTGAGCTTTAGCGAGTCCCTACCCGGCAAGTTCGCCTGATCCTGTCTTGGATGAACTTGGGCGGGCTCTGGCGGGTTGTTAGATC"

# 输出: ["AAAAACCCCC", "CCCCCAAAAA"]


sol = Solution()
print('ret:',sol.findRepeatedDnaSequences(s))
# print(sol.change_int_to_DNA_str(20))





