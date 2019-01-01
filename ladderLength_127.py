# 127. 单词接龙
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:
#
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。



#一样的算法，C++能过，python超时，歧视？
'''
class Solution {
public:
    bool


connect(const
std::string & word1, const
std::string & word2)
{
    int
cnt = 0;
for (int i = 0; i < word1.length();
i + +)
{
if (word1[i] != word2[i])
cnt + +;
}
return cnt == 1;
}
void
construct_graph(std::string & beginWord,
std::vector < std::string > & wordList,
std::map < std::string, std::vector < std::string >> & graph)
{
wordList.push_back(beginWord);
for (int i = 0; i < wordList.size();i++)
{
    graph[wordList[i]] = std::vector < std::string > ();
}
for (int i=0; i < wordList.size();i++)
{
for (int j = i+1; j < wordList.size();j++)
{
if (connect(wordList[i], wordList[j]))
{
graph[wordList[i]].push_back(wordList[j]);
graph[wordList[j]].push_back(wordList[i]);
}
}
}
}
int
BFS_graph(std::string & beginWord, std::string & endWord,
std::map < std::string, std::vector < std::string >> & graph)
{
std::queue < std::pair < std::string, int >> Q;
std::set < std::string > visit;
Q.push(std::make_pair(beginWord, 1));
visit.insert(beginWord);
while (!Q.empty())
{
    std:: string
node = Q.front().first;
int
step = Q.front().second;
Q.pop();
if (node == endWord)
return step;
const
std::vector < std::string > & neighbors = graph[node];
for (int i = 0; i < neighbors.size();i++)
{
if (visit.find(neighbors[i]) == visit.end())
{
    Q.push(std:: make_pair(neighbors[i], step + 1));
visit.insert(neighbors[i]);
}
}

}
return 0;

}
int
ladderLength(string
beginWord, string
endWord, vector < string > & wordList) {
std::map < std::string, std::vector < std::string >> graph;
construct_graph(beginWord, wordList, graph);
return BFS_graph(beginWord, endWord, graph);
}
};
'''

import time
# import collections
from collections import defaultdict
from collections import deque

class Solution:
    def is_connect(self,word1,word2):
        # print(word1,word2)
        # if len(word1) != len(word2):
        #     return False
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        return cnt == 1
    def bfs_search_v1(self,beginWord,endWord,neighbors_map):#这种一次拿一堆的方式超时了，做另一种对比，看是否同样超时
        print(neighbors_map)
        step = 0
        visited = []
        queue = deque()
        queue.append(beginWord)
        visited.append(beginWord)
        while(queue):
            step += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:##可做的小优化，push之前就检查，如果是end就返回，step相应处理一下
                    return step
                for w in neighbors_map[word]:
                    if w not in visited:
                        if w == endWord:
                            return step + 1
                        queue.append(w)
                        visited.append(w)
        return 0
    def bfs_search_v2(self,beginWord,endWord,neighbors_map):#一样是超时....是因为visit不是一个set吗？这个find算遍历？
        # print(neighbors_map)
        visited = []
        queue = deque()
        queue.append((beginWord,1))
        visited.append(beginWord)
        while(queue):
            node = queue.popleft()
            word = node[0]
            step = node[1]
            # print('word:',word)

            if word == endWord:##可做的小优化，push之前就检查，如果是end就返回，step相应处理一下
                return step
            for w in neighbors_map[word]:
                # print('w:',w)
                if w not in visited:
                    if w == endWord:
                        return step + 1
                    queue.append((w,step+1))
                    visited.append(w)
        return 0
    def bfs_search(self,beginWord,endWord,neighbors_map):
        visited = set()
        queue = deque()
        queue.append((beginWord,1))
        visited.add(beginWord)
        while(queue):
            node = queue.popleft()
            word = node[0]
            step = node[1]
            if word == endWord:##可做的小优化，push之前就检查，如果是end就返回，step相应处理一下
                return step
            for w in neighbors_map[word]:
                if w not in visited:
                    if w == endWord:
                        return step + 1
                    queue.append((w,step+1))
                    visited.add(w)
            # print(visited)
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        # 建立邻接表，然后宽搜或者深搜
        neighbors_map = defaultdict(list)
        wordList.append(beginWord)#起点也要丢进去，这样才知道起点出发怎么走,不需要把end也丢进去的原因是，题目要求，字典里没有，就找不到
        begin = time.time()
        # cnt = 0
        for i in range(len(wordList)):#建立邻接表错了，两层不应该用同样的遍历，有重复的，但是理论上，复杂度都是N^2？
            for j in range(i+1,len(wordList)):

                #实测，和is_connect函数调用也无关。
                #2800次的4字符比较，也就这个时间：0.0012848377227783203
                if self.is_connect(wordList[i],wordList[j]):
                    neighbors_map[wordList[i]].append(wordList[j])#并且应该双向建立
                    neighbors_map[wordList[j]].append(wordList[i])
                    # print(neighbors_map)
        end = time.time()
        print('spend:',end-begin)#spend: 7.581710815429688e-05          #spend: 2.8866970539093018!!!慢的根源！！！
        print('length:',len(wordList))#length: 2856#就算是这样，复杂度级别也是N方，只不过是N^2/2
        # print('cnt:',cnt)#cnt: 4076940!!400万次遍历，每一次都把两个字符串逐个字母对比，没问题吗？
        return self.bfs_search(beginWord,endWord,neighbors_map)




    def bfs_search_with_list(self,beginWord,endWord,neighbors_map,neighbors_list):
        visited = set()
        queue = deque()
        queue.append((beginWord,1))
        visited.add(beginWord)
        while(queue):
            node = queue.popleft()
            word = node[0]
            step = node[1]
            if word == endWord:##可做的小优化，push之前就检查，如果是end就返回，step相应处理一下
                return step
            for w in neighbors_list[neighbors_map[word]]:
                if w not in visited:
                    if w == endWord:
                        return step + 1
                    queue.append((w,step+1))
                    visited.add(w)
            # print(visited)
        return 0

    # defaultdict不背这锅,手动建立映射，依然没改进
    def ladderLength_with_list(self, beginWord, endWord, wordList):
        # 建立邻接表，然后宽搜或者深搜
        neighbors_map = {}
        wordList.append(beginWord)#起点也要丢进去，这样才知道起点出发怎么走,不需要把end也丢进去的原因是，题目要求，字典里没有，就找不到
        begin = time.time()
        # cnt = 0
        neighbors_list = []
        for i in range(len(wordList)):
            neighbors_map[wordList[i]] = i#index
            neighbors_list.append([])
        # print(neighbors_list)

        for i in range(len(wordList)):#建立邻接表错了，两层不应该用同样的遍历，有重复的，但是理论上，复杂度都是N^2？
            for j in range(i+1,len(wordList)):

                #实测，和is_connect函数调用也无关。
                #2800次的4字符比较，也就这个时间：0.0012848377227783203
                if self.is_connect(wordList[i],wordList[j]):
                    neighbors_list[i].append(wordList[j])
                    neighbors_list[j].append(wordList[i])
        print(neighbors_map)
        print(neighbors_list)
        end = time.time()
        print('spend:',end-begin)#spend: 7.581710815429688e-05          #spend: 2.8866970539093018!!!慢的根源！！！
        # print('length:',len(wordList))#length: 2856#你看，这就验证了我说的，就算是这样，复杂度级别也是N方，只不过是N^2/2,实测不影响：0.008553504943847656
        # print('cnt:',cnt)#cnt: 4076940!!400万次遍历，每一次都把两个字符串逐个字母对比，没问题吗？
        return self.bfs_search_with_list(beginWord,endWord,neighbors_map,neighbors_list)






#写这么多代码还超时，人家随随便便做字母变化都能过


# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         wordset = set(wordList)
#         if endWord not in wordset:
#             return 0
#         visited = set([beginWord])
#         chrs = [chr(ord('a') + i) for i in range(26)]
#         bfs = collections.deque([beginWord])
#         res = 1
#         while bfs:
#             len_bfs = len(bfs)
#             for _ in range(len_bfs):
#                 origin = bfs.popleft()
#                 for i in range(len(origin)):
#                     originlist = list(origin)
#                     for c in chrs:
#                         originlist[i] = c
#                         transword = "".join(originlist)
#                         if transword not in visited:
#                             if transword == endWord:
#                                 return res + 1
#                             elif transword in wordset:
#                                 bfs.append(transword)
#                                 visited.add(transword)
#             res += 1
#         return 0

##人家这么简单的代码都能通过。,就是走迷宫法
#就是直接用字母表来改单词，比如一个单词长度4，就从4*26个枚举中筛选，在wordlist，还不是自己，就成功
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         wordset = set(wordList)
#         bfs = collections.deque()
#         bfs.append((beginWord, 1))
#         while bfs:
#             word, length = bfs.popleft()
#             if word == endWord:
#                 return length
#             for i in range(len(word)):
#                 for c in "abcdefghijklmnopqrstuvwxyz":
#                     newWord = word[:i] + c + word[i + 1:]
#                     if newWord in wordset and newWord != word:
#                         wordset.remove(newWord)
#                         bfs.append((newWord, length + 1))
#         return 0
#
#
# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         wl = len(beginWord)
#         begin_set, end_set = {beginWord}, {endWord}
#         wordList = set(wordList)
#         if endWord not in wordList:
#             return 0
#         i = 1
#         while begin_set and end_set:
#             i += 1
#             if len(begin_set) > len(end_set):
#                 begin_set, end_set = end_set, begin_set
#
#             nextLst = set()
#             for word in begin_set:
#                 for j in range(wl):
#                     for k in range(26):
#                         nextWord = word[:j] + chr(k+97) + word[j+1:]
#                         if nextWord in end_set:
#                             return i
#                         if nextWord in wordList:
#                             nextLst.add(nextWord)
#                             wordList.remove(nextWord)
#             begin_set = nextLst
#         return 0



# 双向广搜？不过面试暂时不会用到。
# 双向广搜的优势又在哪？
#如果要写双向广搜，要怎么办？两个队列，每个队列拿出整层来对比？

# 示例 1:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5


# beginWord = 'sand'
# endWord = 'acne'
# wordList = ["slit","bunk","wars","ping","viva","wynn","wows","irks","gang","pool","mock","fort","heel","send","ship","cols","alec","foal","nabs","gaze","giza","mays","dogs","karo","cums","jedi","webb","lend","mire","jose","catt","grow","toss","magi","leis","bead","kara","hoof","than","ires","baas","vein","kari","riga","oars","gags","thug","yawn","wive","view","germ","flab","july","tuck","rory","bean","feed","rhee","jeez","gobs","lath","desk","yoko","cute","zeus","thus","dims","link","dirt","mara","disc","limy","lewd","maud","duly","elsa","hart","rays","rues","camp","lack","okra","tome","math","plug","monk","orly","friz","hogs","yoda","poop","tick","plod","cloy","pees","imps","lead","pope","mall","frey","been","plea","poll","male","teak","soho","glob","bell","mary","hail","scan","yips","like","mull","kory","odor","byte","kaye","word","honk","asks","slid","hopi","toke","gore","flew","tins","mown","oise","hall","vega","sing","fool","boat","bobs","lain","soft","hard","rots","sees","apex","chan","told","woos","unit","scow","gilt","beef","jars","tyre","imus","neon","soap","dabs","rein","ovid","hose","husk","loll","asia","cope","tail","hazy","clad","lash","sags","moll","eddy","fuel","lift","flog","land","sigh","saks","sail","hook","visa","tier","maws","roeg","gila","eyes","noah","hypo","tore","eggs","rove","chap","room","wait","lurk","race","host","dada","lola","gabs","sobs","joel","keck","axed","mead","gust","laid","ends","oort","nose","peer","kept","abet","iran","mick","dead","hags","tens","gown","sick","odis","miro","bill","fawn","sumo","kilt","huge","ores","oran","flag","tost","seth","sift","poet","reds","pips","cape","togo","wale","limn","toll","ploy","inns","snag","hoes","jerk","flux","fido","zane","arab","gamy","raze","lank","hurt","rail","hind","hoot","dogy","away","pest","hoed","pose","lose","pole","alva","dino","kind","clan","dips","soup","veto","edna","damp","gush","amen","wits","pubs","fuzz","cash","pine","trod","gunk","nude","lost","rite","cory","walt","mica","cart","avow","wind","book","leon","life","bang","draw","leek","skis","dram","ripe","mine","urea","tiff","over","gale","weir","defy","norm","tull","whiz","gill","ward","crag","when","mill","firs","sans","flue","reid","ekes","jain","mutt","hems","laps","piss","pall","rowe","prey","cull","knew","size","wets","hurl","wont","suva","girt","prys","prow","warn","naps","gong","thru","livy","boar","sade","amok","vice","slat","emir","jade","karl","loyd","cerf","bess","loss","rums","lats","bode","subs","muss","maim","kits","thin","york","punt","gays","alpo","aids","drag","eras","mats","pyre","clot","step","oath","lout","wary","carp","hums","tang","pout","whip","fled","omar","such","kano","jake","stan","loop","fuss","mini","byrd","exit","fizz","lire","emil","prop","noes","awed","gift","soli","sale","gage","orin","slur","limp","saar","arks","mast","gnat","port","into","geed","pave","awls","cent","cunt","full","dint","hank","mate","coin","tars","scud","veer","coax","bops","uris","loom","shod","crib","lids","drys","fish","edit","dick","erna","else","hahs","alga","moho","wire","fora","tums","ruth","bets","duns","mold","mush","swop","ruby","bolt","nave","kite","ahem","brad","tern","nips","whew","bait","ooze","gino","yuck","drum","shoe","lobe","dusk","cult","paws","anew","dado","nook","half","lams","rich","cato","java","kemp","vain","fees","sham","auks","gish","fire","elam","salt","sour","loth","whit","yogi","shes","scam","yous","lucy","inez","geld","whig","thee","kelp","loaf","harm","tomb","ever","airs","page","laud","stun","paid","goop","cobs","judy","grab","doha","crew","item","fogs","tong","blip","vest","bran","wend","bawl","feel","jets","mixt","tell","dire","devi","milo","deng","yews","weak","mark","doug","fare","rigs","poke","hies","sian","suez","quip","kens","lass","zips","elva","brat","cosy","teri","hull","spun","russ","pupa","weed","pulp","main","grim","hone","cord","barf","olav","gaps","rote","wilt","lars","roll","balm","jana","give","eire","faun","suck","kegs","nita","weer","tush","spry","loge","nays","heir","dope","roar","peep","nags","ates","bane","seas","sign","fred","they","lien","kiev","fops","said","lawn","lind","miff","mass","trig","sins","furl","ruin","sent","cray","maya","clog","puns","silk","axis","grog","jots","dyer","mope","rand","vend","keen","chou","dose","rain","eats","sped","maui","evan","time","todd","skit","lief","sops","outs","moot","faze","biro","gook","fill","oval","skew","veil","born","slob","hyde","twin","eloy","beat","ergs","sure","kobe","eggo","hens","jive","flax","mons","dunk","yest","begs","dial","lodz","burp","pile","much","dock","rene","sago","racy","have","yalu","glow","move","peps","hods","kins","salk","hand","cons","dare","myra","sega","type","mari","pelt","hula","gulf","jugs","flay","fest","spat","toms","zeno","taps","deny","swag","afro","baud","jabs","smut","egos","lara","toes","song","fray","luis","brut","olen","mere","ruff","slum","glad","buds","silt","rued","gelt","hive","teem","ides","sink","ands","wisp","omen","lyre","yuks","curb","loam","darn","liar","pugs","pane","carl","sang","scar","zeds","claw","berg","hits","mile","lite","khan","erik","slug","loon","dena","ruse","talk","tusk","gaol","tads","beds","sock","howe","gave","snob","ahab","part","meir","jell","stir","tels","spit","hash","omit","jinx","lyra","puck","laue","beep","eros","owed","cede","brew","slue","mitt","jest","lynx","wads","gena","dank","volt","gray","pony","veld","bask","fens","argo","work","taxi","afar","boon","lube","pass","lazy","mist","blot","mach","poky","rams","sits","rend","dome","pray","duck","hers","lure","keep","gory","chat","runt","jams","lays","posy","bats","hoff","rock","keri","raul","yves","lama","ramp","vote","jody","pock","gist","sass","iago","coos","rank","lowe","vows","koch","taco","jinn","juno","rape","band","aces","goal","huck","lila","tuft","swan","blab","leda","gems","hide","tack","porn","scum","frat","plum","duds","shad","arms","pare","chin","gain","knee","foot","line","dove","vera","jays","fund","reno","skid","boys","corn","gwyn","sash","weld","ruiz","dior","jess","leaf","pars","cote","zing","scat","nice","dart","only","owls","hike","trey","whys","ding","klan","ross","barb","ants","lean","dopy","hock","tour","grip","aldo","whim","prom","rear","dins","duff","dell","loch","lava","sung","yank","thar","curl","venn","blow","pomp","heat","trap","dali","nets","seen","gash","twig","dads","emmy","rhea","navy","haws","mite","bows","alas","ives","play","soon","doll","chum","ajar","foam","call","puke","kris","wily","came","ales","reef","raid","diet","prod","prut","loot","soar","coed","celt","seam","dray","lump","jags","nods","sole","kink","peso","howl","cost","tsar","uric","sore","woes","sewn","sake","cask","caps","burl","tame","bulk","neva","from","meet","webs","spar","fuck","buoy","wept","west","dual","pica","sold","seed","gads","riff","neck","deed","rudy","drop","vale","flit","romp","peak","jape","jews","fain","dens","hugo","elba","mink","town","clam","feud","fern","dung","newt","mime","deem","inti","gigs","sosa","lope","lard","cara","smug","lego","flex","doth","paar","moon","wren","tale","kant","eels","muck","toga","zens","lops","duet","coil","gall","teal","glib","muir","ails","boer","them","rake","conn","neat","frog","trip","coma","must","mono","lira","craw","sled","wear","toby","reel","hips","nate","pump","mont","died","moss","lair","jibe","oils","pied","hobs","cads","haze","muse","cogs","figs","cues","roes","whet","boru","cozy","amos","tans","news","hake","cots","boas","tutu","wavy","pipe","typo","albs","boom","dyke","wail","woke","ware","rita","fail","slab","owes","jane","rack","hell","lags","mend","mask","hume","wane","acne","team","holy","runs","exes","dole","trim","zola","trek","puma","wacs","veep","yaps","sums","lush","tubs","most","witt","bong","rule","hear","awry","sots","nils","bash","gasp","inch","pens","fies","juts","pate","vine","zulu","this","bare","veal","josh","reek","ours","cowl","club","farm","teat","coat","dish","fore","weft","exam","vlad","floe","beak","lane","ella","warp","goth","ming","pits","rent","tito","wish","amps","says","hawk","ways","punk","nark","cagy","east","paul","bose","solo","teed","text","hews","snip","lips","emit","orgy","icon","tuna","soul","kurd","clod","calk","aunt","bake","copy","acid","duse","kiln","spec","fans","bani","irma","pads","batu","logo","pack","oder","atop","funk","gide","bede","bibs","taut","guns","dana","puff","lyme","flat","lake","june","sets","gull","hops","earn","clip","fell","kama","seal","diaz","cite","chew","cuba","bury","yard","bank","byes","apia","cree","nosh","judo","walk","tape","taro","boot","cods","lade","cong","deft","slim","jeri","rile","park","aeon","fact","slow","goff","cane","earp","tart","does","acts","hope","cant","buts","shin","dude","ergo","mode","gene","lept","chen","beta","eden","pang","saab","fang","whir","cove","perk","fads","rugs","herb","putt","nous","vane","corm","stay","bids","vela","roof","isms","sics","gone","swum","wiry","cram","rink","pert","heap","sikh","dais","cell","peel","nuke","buss","rasp","none","slut","bent","dams","serb","dork","bays","kale","cora","wake","welt","rind","trot","sloe","pity","rout","eves","fats","furs","pogo","beth","hued","edam","iamb","glee","lute","keel","airy","easy","tire","rube","bogy","sine","chop","rood","elbe","mike","garb","jill","gaul","chit","dons","bars","ride","beck","toad","make","head","suds","pike","snot","swat","peed","same","gaza","lent","gait","gael","elks","hang","nerf","rosy","shut","glop","pain","dion","deaf","hero","doer","wost","wage","wash","pats","narc","ions","dice","quay","vied","eons","case","pour","urns","reva","rags","aden","bone","rang","aura","iraq","toot","rome","hals","megs","pond","john","yeps","pawl","warm","bird","tint","jowl","gibe","come","hold","pail","wipe","bike","rips","eery","kent","hims","inks","fink","mott","ices","macy","serf","keys","tarp","cops","sods","feet","tear","benz","buys","colo","boil","sews","enos","watt","pull","brag","cork","save","mint","feat","jamb","rubs","roxy","toys","nosy","yowl","tamp","lobs","foul","doom","sown","pigs","hemp","fame","boor","cube","tops","loco","lads","eyre","alta","aged","flop","pram","lesa","sawn","plow","aral","load","lied","pled","boob","bert","rows","zits","rick","hint","dido","fist","marc","wuss","node","smog","nora","shim","glut","bale","perl","what","tort","meek","brie","bind","cake","psst","dour","jove","tree","chip","stud","thou","mobs","sows","opts","diva","perm","wise","cuds","sols","alan","mild","pure","gail","wins","offs","nile","yelp","minn","tors","tran","homy","sadr","erse","nero","scab","finn","mich","turd","then","poem","noun","oxus","brow","door","saws","eben","wart","wand","rosa","left","lina","cabs","rapt","olin","suet","kalb","mans","dawn","riel","temp","chug","peal","drew","null","hath","many","took","fond","gate","sate","leak","zany","vans","mart","hess","home","long","dirk","bile","lace","moog","axes","zone","fork","duct","rico","rife","deep","tiny","hugh","bilk","waft","swig","pans","with","kern","busy","film","lulu","king","lord","veda","tray","legs","soot","ells","wasp","hunt","earl","ouch","diem","yell","pegs","blvd","polk","soda","zorn","liza","slop","week","kill","rusk","eric","sump","haul","rims","crop","blob","face","bins","read","care","pele","ritz","beau","golf","drip","dike","stab","jibs","hove","junk","hoax","tats","fief","quad","peat","ream","hats","root","flak","grit","clap","pugh","bosh","lock","mute","crow","iced","lisa","bela","fems","oxes","vies","gybe","huff","bull","cuss","sunk","pups","fobs","turf","sect","atom","debt","sane","writ","anon","mayo","aria","seer","thor","brim","gawk","jack","jazz","menu","yolk","surf","libs","lets","bans","toil","open","aced","poor","mess","wham","fran","gina","dote","love","mood","pale","reps","ines","shot","alar","twit","site","dill","yoga","sear","vamp","abel","lieu","cuff","orbs","rose","tank","gape","guam","adar","vole","your","dean","dear","hebe","crab","hump","mole","vase","rode","dash","sera","balk","lela","inca","gaea","bush","loud","pies","aide","blew","mien","side","kerr","ring","tess","prep","rant","lugs","hobo","joke","odds","yule","aida","true","pone","lode","nona","weep","coda","elmo","skim","wink","bras","pier","bung","pets","tabs","ryan","jock","body","sofa","joey","zion","mace","kick","vile","leno","bali","fart","that","redo","ills","jogs","pent","drub","slaw","tide","lena","seep","gyps","wave","amid","fear","ties","flan","wimp","kali","shun","crap","sage","rune","logs","cain","digs","abut","obit","paps","rids","fair","hack","huns","road","caws","curt","jute","fisk","fowl","duty","holt","miss","rude","vito","baal","ural","mann","mind","belt","clem","last","musk","roam","abed","days","bore","fuze","fall","pict","dump","dies","fiat","vent","pork","eyed","docs","rive","spas","rope","ariz","tout","game","jump","blur","anti","lisp","turn","sand","food","moos","hoop","saul","arch","fury","rise","diss","hubs","burs","grid","ilks","suns","flea","soil","lung","want","nola","fins","thud","kidd","juan","heps","nape","rash","burt","bump","tots","brit","mums","bole","shah","tees","skip","limb","umps","ache","arcs","raft","halo","luce","bahs","leta","conk","duos","siva","went","peek","sulk","reap","free","dubs","lang","toto","hasp","ball","rats","nair","myst","wang","snug","nash","laos","ante","opal","tina","pore","bite","haas","myth","yugo","foci","dent","bade","pear","mods","auto","shop","etch","lyly","curs","aron","slew","tyro","sack","wade","clio","gyro","butt","icky","char","itch","halt","gals","yang","tend","pact","bees","suit","puny","hows","nina","brno","oops","lick","sons","kilo","bust","nome","mona","dull","join","hour","papa","stag","bern","wove","lull","slip","laze","roil","alto","bath","buck","alma","anus","evil","dumb","oreo","rare","near","cure","isis","hill","kyle","pace","comb","nits","flip","clop","mort","thea","wall","kiel","judd","coop","dave","very","amie","blah","flub","talc","bold","fogy","idea","prof","horn","shoo","aped","pins","helm","wees","beer","womb","clue","alba","aloe","fine","bard","limo","shaw","pint","swim","dust","indy","hale","cats","troy","wens","luke","vern","deli","both","brig","daub","sara","sued","bier","noel","olga","dupe","look","pisa","knox","murk","dame","matt","gold","jame","toge","luck","peck","tass","calf","pill","wore","wadi","thur","parr","maul","tzar","ones","lees","dark","fake","bast","zoom","here","moro","wine","bums","cows","jean","palm","fume","plop","help","tuba","leap","cans","back","avid","lice","lust","polo","dory","stew","kate","rama","coke","bled","mugs","ajax","arts","drug","pena","cody","hole","sean","deck","guts","kong","bate","pitt","como","lyle","siam","rook","baby","jigs","bret","bark","lori","reba","sups","made","buzz","gnaw","alps","clay","post","viol","dina","card","lana","doff","yups","tons","live","kids","pair","yawl","name","oven","sirs","gyms","prig","down","leos","noon","nibs","cook","safe","cobb","raja","awes","sari","nerd","fold","lots","pete","deal","bias","zeal","girl","rage","cool","gout","whey","soak","thaw","bear","wing","nagy","well","oink","sven","kurt","etna","held","wood","high","feta","twee","ford","cave","knot","tory","ibis","yaks","vets","foxy","sank","cone","pius","tall","seem","wool","flap","gird","lore","coot","mewl","sere","real","puts","sell","nuts","foil","lilt","saga","heft","dyed","goat","spew","daze","frye","adds","glen","tojo","pixy","gobi","stop","tile","hiss","shed","hahn","baku","ahas","sill","swap","also","carr","manx","lime","debs","moat","eked","bola","pods","coon","lacy","tube","minx","buff","pres","clew","gaff","flee","burn","whom","cola","fret","purl","wick","wigs","donn","guys","toni","oxen","wite","vial","spam","huts","vats","lima","core","eula","thad","peon","erie","oats","boyd","cued","olaf","tams","secs","urey","wile","penn","bred","rill","vary","sues","mail","feds","aves","code","beam","reed","neil","hark","pols","gris","gods","mesa","test","coup","heed","dora","hied","tune","doze","pews","oaks","bloc","tips","maid","goof","four","woof","silo","bray","zest","kiss","yong","file","hilt","iris","tuns","lily","ears","pant","jury","taft","data","gild","pick","kook","colt","bohr","anal","asps","babe","bach","mash","biko","bowl","huey","jilt","goes","guff","bend","nike","tami","gosh","tike","gees","urge","path","bony","jude","lynn","lois","teas","dunn","elul","bonn","moms","bugs","slay","yeah","loan","hulk","lows","damn","nell","jung","avis","mane","waco","loin","knob","tyke","anna","hire","luau","tidy","nuns","pots","quid","exec","hans","hera","hush","shag","scot","moan","wald","ursa","lorn","hunk","loft","yore","alum","mows","slog","emma","spud","rice","worn","erma","need","bags","lark","kirk","pooh","dyes","area","dime","luvs","foch","refs","cast","alit","tugs","even","role","toed","caph","nigh","sony","bide","robs","folk","daft","past","blue","flaw","sana","fits","barr","riot","dots","lamp","cock","fibs","harp","tent","hate","mali","togs","gear","tues","bass","pros","numb","emus","hare","fate","wife","mean","pink","dune","ares","dine","oily","tony","czar","spay","push","glum","till","moth","glue","dive","scad","pops","woks","andy","leah","cusp","hair","alex","vibe","bulb","boll","firm","joys","tara","cole","levy","owen","chow","rump","jail","lapp","beet","slap","kith","more","maps","bond","hick","opus","rust","wist","shat","phil","snow","lott","lora","cary","mote","rift","oust","klee","goad","pith","heep","lupe","ivan","mimi","bald","fuse","cuts","lens","leer","eyry","know","razz","tare","pals","geek","greg","teen","clef","wags","weal","each","haft","nova","waif","rate","katy","yale","dale","leas","axum","quiz","pawn","fend","capt","laws","city","chad","coal","nail","zaps","sort","loci","less","spur","note","foes","fags","gulp","snap","bogs","wrap","dane","melt","ease","felt","shea","calm","star","swam","aery","year","plan","odin","curd","mira","mops","shit","davy","apes","inky","hues","lome","bits","vila","show","best","mice","gins","next","roan","ymir","mars","oman","wild","heal","plus","erin","rave","robe","fast","hutu","aver","jodi","alms","yams","zero","revs","wean","chic","self","jeep","jobs","waxy","duel","seek","spot","raps","pimp","adan","slam","tool","morn","futz","ewes","errs","knit","rung","kans","muff","huhs","tows","lest","meal","azov","gnus","agar","sips","sway","otis","tone","tate","epic","trio","tics","fade","lear","owns","robt","weds","five","lyon","terr","arno","mama","grey","disk","sept","sire","bart","saps","whoa","turk","stow","pyle","joni","zinc","negs","task","leif","ribs","malt","nine","bunt","grin","dona","nope","hams","some","molt","smit","sacs","joan","slav","lady","base","heck","list","take","herd","will","nubs","burg","hugs","peru","coif","zoos","nick","idol","levi","grub","roth","adam","elma","tags","tote","yaws","cali","mete","lula","cubs","prim","luna","jolt","span","pita","dodo","puss","deer","term","dolt","goon","gary","yarn","aims","just","rena","tine","cyst","meld","loki","wong","were","hung","maze","arid","cars","wolf","marx","faye","eave","raga","flow","neal","lone","anne","cage","tied","tilt","soto","opel","date","buns","dorm","kane","akin","ewer","drab","thai","jeer","grad","berm","rods","saki","grus","vast","late","lint","mule","risk","labs","snit","gala","find","spin","ired","slot","oafs","lies","mews","wino","milk","bout","onus","tram","jaws","peas","cleo","seat","gums","cold","vang","dewy","hood","rush","mack","yuan","odes","boos","jami","mare","plot","swab","borg","hays","form","mesh","mani","fife","good","gram","lion","myna","moor","skin","posh","burr","rime","done","ruts","pays","stem","ting","arty","slag","iron","ayes","stub","oral","gets","chid","yens","snub","ages","wide","bail","verb","lamb","bomb","army","yoke","gels","tits","bork","mils","nary","barn","hype","odom","avon","hewn","rios","cams","tact","boss","oleo","duke","eris","gwen","elms","deon","sims","quit","nest","font","dues","yeas","zeta","bevy","gent","torn","cups","worm","baum","axon","purr","vise","grew","govs","meat","chef","rest","lame"]

sol = Solution()
print('ret:',sol.ladderLength(beginWord,endWord,wordList))
# print(sol.is_connect('hot','dot'))
# print(sol.is_connect('hot','log'))



#
# set1 = set()
# set1.add('hit')
# print('hit' in set1)
# print('hit' not in set1)









#
# #如果你写逗号，这是另一个含义
# test = 'hit',
# test2 = 'hit'
# print(type(test),test)
# print(type(test2),test2)


neighbors_map = defaultdict(list)
print(neighbors_map)
neighbors_map[1].append(2)
print(neighbors_map)
neighbors_map[2].append(3)
print(neighbors_map)



#测时间复杂度，寻找优化空间

import time
'''
set1 = set()
for i in range(1000):
    set1.add(i)

start = time.time()
if 1100 not in set1:
    pass
end = time.time()
print(end-start)
'''


#list的 not in就比set慢多了，这是遍历
l1 = []
for i in range(10000000):
    l1.append(i)
# print(l1)

start = time.time()
if 1 not in l1:
    pass
end = time.time()
print(end-start)

start = time.time()
if 110000 not in l1:
    pass
end = time.time()
print(end-start)


start = time.time()
length = len(l1)#len(),自建的，可能内部有什么机制支持了，不是遍历的，按理说不影响
end = time.time()
print(end-start)


str1 = 'abcd'
str2 = 'abcd'
start = time.time()
for j in range(2856):
    for i in range(len(str1)):
        if sol.is_connect(str1,str2):
        # if str1 == str2:
            pass
end = time.time()
print(end-start)








