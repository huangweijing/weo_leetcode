from typing import List
from collections import deque

class DirectedGraph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]

class AlgorithmGetPathToBFS:
    def __init__(self, g: DirectedGraph):
        self.graph = g
        self.searched_mark = [False] * self.graph.get_vertex_count()
        self.edge_to = [None] * self.graph.get_vertex_count()
        self.cost_to = [501] * self.graph.get_vertex_count()
        self.path_list = list[list[int]]()

    def bfs(self, start_vertex: int, end_vertex: int) -> list[list[int]]:
        vertex_list = set[int]()
        self.searched_mark[start_vertex] = True
        vertex_list.add(start_vertex)
        while len(vertex_list) > 0:
            new_vertex_list = set[int]()
            vertex_to_mark = set[int]()
            # print(vertex_list)
            while len(vertex_list) > 0:
                vertex = vertex_list.pop()
                # if self.searched_mark[vertex]:
                #     continue
                adj_vertex_list = self.graph.get_adjacent_vertex(vertex)
                # print(f"vertex={vertex}")
                for adj_vertex in adj_vertex_list:
                    if self.searched_mark[adj_vertex]:
                        continue
                    vertex_to_mark.add(adj_vertex)
                    # print(f"adj_vertex={adj_vertex}, self.cost_to[adj_vertex]={self.cost_to[adj_vertex]}, self.edge_to[vertex]={self.edge_to[vertex]}")
                    if self.edge_to[adj_vertex] is None:
                        self.edge_to[adj_vertex] = set[int]()
                    self.edge_to[adj_vertex].add(vertex)
                    new_vertex_list.add(adj_vertex)

            # print(vertex_to_mark)
            for vertex in vertex_to_mark:
                self.searched_mark[vertex] = True

            vertex_list = new_vertex_list

        result = self.make_path(start_vertex, end_vertex)
        return result

    def make_path(self, start_vertex:int , vertex:int) -> list[list[int]]:
        if start_vertex == vertex:
            return [[start_vertex]]

        pre_vertex_set = self.edge_to[vertex]
        if pre_vertex_set is None:
            return None
        result = list[list[int]]()
        for pre_v in pre_vertex_set:
            path_list = self.make_path(start_vertex, pre_v)
            if path_list is None:
                continue
            for path in path_list:
                path.append(vertex)
                result.append(path)
        return result


    def get_path_to(self, start_vertex: int, end_vertex: int) -> list[list[int]]:
        ## dfs
        # self.dfs(start_vertex, end_vertex, [start_vertex])
        # result = list[list[int]]()
        # shortest_path = 501
        # for path in self.path_list:
        #     if len(path) < shortest_path:
        #         shortest_path = len(path)
        #         result.clear()
        #     if len(path) == shortest_path:
        #         result.append(path)
        # return result
        return self.bfs(start_vertex, end_vertex)

        # return self.path_list

class Solution:
    def is_adjacent(self, word1: str, word2: str) -> bool:
        diff = False
        for i, ch in enumerate(word1):
            if ch != word2[i]:
                if diff:
                    return False
                else:
                    diff = True
        if not diff:
            return False
        else:
            return True

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        # wordList.append(endWord)
        word_idx_dict = dict[str, int]()
        for idx, word in enumerate(wordList):
            word_idx_dict[word] = idx
        graph = DirectedGraph(len(wordList))
        for idx, word1 in enumerate(wordList):
            for idx2, word2 in enumerate(wordList):
                if idx != idx2:
                    if self.is_adjacent(word1, word2):
                        graph.add_edge(idx, idx2)
        begin_idx = word_idx_dict[beginWord]
        if endWord not in word_idx_dict:
            return []
        end_idx = word_idx_dict[endWord]

        # print(f"isAdjacent: {graph.get_adjacent_vertex(word_idx_dict['hot'])}")
        alg = AlgorithmGetPathToBFS(graph)
        path_list = alg.get_path_to(begin_idx, end_idx)
        result = list[list[str]]()
        if path_list is not None:
            for path in path_list:
                result.append(list(map(wordList.__getitem__, path)))
        return result

# beginWord = "aaaaa"
# endWord = "ggggg"
# wordList = ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]
#
# r = Solution().findLadders(beginWord, endWord, wordList)
# print(r)
beginWord = "hot"
endWord = "dog"
wordList = ["hot", "dog"]
r = Solution().findLadders(beginWord, endWord, wordList)
print(r)

# "hot"
# "dog"
# ["hot","dog"]