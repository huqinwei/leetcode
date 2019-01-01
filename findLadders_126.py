

# 126. 单词接龙
#给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:
#
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: []
#
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。


#其实就是127的变形，改一下就行了。之前用的是队列，前边popleft就没了。现在改成用个list，只是移动指针，并不抛弃访问过的点，这样就保存了全部信息。
#然后就用前驱下标往回找就能找到路径，因为这里用了visited做互斥，所以一个点只有一个前驱，不会有多个，这是能如此实现的前提!!!!!!!!!也是自己凭空思考不容易挖掘的点#
#题目也变了，什么叫所有最短？是刚好有几个一样短的时候这几个都返回？all shortest!!!
#我觉得还是用我第一种while内嵌for循环来做，这个结束条件好做，取出的时候，设定条件，但是当前for循环可以运行到结束。
# 用他这种结构也可以，也设立结束标记，然后设立结束step，再pop出来的step如果超了就结束。
# 原来的visit并不能用！！！！visit其实还是会阻碍形成所有路径，所以“所有最短路径”就成了伪命题。
# 比如A指向B和C，B和C都指向D。那么从A到D其实两个路径，但是visit会导致只有一条路径。
#所以前边想的利用visit互斥，只有一个前驱那个想法就不对了
#但是你可以每次走到终点都单独存一份，这样一个D指向C，一个D指向B，就都回去了



#todo  把下边127的代码改了
# import collections
from collections import defaultdict
from collections import deque

class Solution:
    def is_connect(self,word1,word2):
        print(word1,word2)
        if len(word1) != len(word2):
            return False
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
        # print(neighbors_map)
        visited = set()
        queue = deque()
        queue.append((beginWord,1))
        visited.add(beginWord)
        while(queue):
            node = queue.popleft()
            word = node[0]
            step = node[1]
            # print('word:',word)

            if word == endWord:##可做的小优化，push之前就检查，如果是end就返回，step相应处理一下
                return step
            for w in neighbors_map[word]:
                # print('w:',w)
                # if visited[]
                if w not in visited:
                    if w == endWord:
                        return step + 1
                    queue.append((w,step+1))
                    visited.add(w)
            print(visited)
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        # 建立邻接表，然后宽搜或者深搜
        neighbors_map = defaultdict(list)
        wordList.append(beginWord)#起点也要丢进去，这样才知道起点出发怎么走,不需要把end也丢进去的原因是，题目要求，字典里没有，就找不到
        for i in range(len(wordList)):#建立邻接表错了，两层不应该用同样的遍历，有重复的，但是理论上，复杂度都是N^2？
            for j in range(i+1,len(wordList)):
                if self.is_connect(wordList[i],wordList[j]):
                    neighbors_map[wordList[i]].append(wordList[j])#并且应该双向建立
                    neighbors_map[wordList[j]].append(wordList[i])
                    print(neighbors_map)

        return self.bfs_search(beginWord,endWord,neighbors_map)


# 双向广搜？不过面试暂时不会用到。
# 双向广搜的优势又在哪？

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

















