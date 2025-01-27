from typing import List

class ATM:

    def __init__(self):
        self.note_val = [20, 50, 100, 200, 500]
        self.store = [0, 0, 0, 0, 0]
        
    def deposit(self, banknotesCount: List[int]) -> None:
        for i, note in enumerate(banknotesCount):
            self.store[i] += note

    def withdraw(self, amount: int) -> List[int]:
        ret = [0, 0, 0, 0, 0]
        store = self.store.copy()
        idx = len(self.note_val) - 1
        while idx >= 0:
            while amount >= self.note_val[idx] and store[idx] > 0:
                cnt = min(store[idx], amount // self.note_val[idx])
                amount -= cnt * self.note_val[idx]
                store[idx] -= cnt
                ret[idx] += cnt
            # print(self.note_val[idx], amount)
            idx -= 1
        if amount == 0:
            self.store = store
        else:
            ret = [-1]
        return ret


data = [
# ["ATM","withdraw","deposit","deposit","deposit","deposit","deposit","deposit","withdraw","deposit","withdraw","withdraw","withdraw","withdraw","withdraw","withdraw","withdraw","withdraw","withdraw","deposit","deposit","withdraw","deposit","deposit","withdraw","deposit","deposit","deposit","deposit","deposit","withdraw","withdraw","withdraw","deposit","withdraw","withdraw","deposit","deposit","deposit","deposit","withdraw","deposit","withdraw","withdraw","deposit","deposit","withdraw","withdraw","withdraw","withdraw","withdraw","withdraw","deposit","withdraw","withdraw","deposit","withdraw","withdraw","deposit","withdraw","withdraw","deposit","withdraw","deposit","withdraw","withdraw","deposit","deposit","withdraw","deposit","withdraw","withdraw","withdraw","deposit","deposit","withdraw","withdraw","withdraw","deposit","deposit","deposit","withdraw","withdraw","withdraw","withdraw","withdraw","deposit","deposit","withdraw","withdraw","deposit"]
# , [[],[612519790],[[335778,848154,119256,88284,800761]],[[838123,734850,938357,767867,619568]],[[295545,644807,945715,235366,389410]],[[371938,643156,650866,276264,967618]],[[664440,931186,736602,608390,986995]],[[835266,327755,792986,248191,29300]],[272106650],[[427123,97369,944260,798500,523262]],[774276375],[97537035],[996467815],[641646035],[875306040],[527583655],[4020640],[205858665],[282796115],[[114141,872629,383737,520833,134076]],[[868438,293086,477931,358591,241162]],[186734200],[[257230,646928,76911,259434,442424]],[[868845,488537,420022,657569,229281]],[427402275],[[654675,636386,728985,136331,309723]],[[289998,210084,284156,264536,415559]],[[513953,975642,105349,768092,719161]],[[625716,605953,781441,363032,710089]],[[933718,411763,28886,606502,935793]],[903776210],[385312930],[147464610],[[880020,174924,768543,545233,915409]],[27188970],[927664515],[[90631,935661,920083,622910,833297]],[[336752,436746,894142,508751,54763]],[[400048,110441,629753,277098,441365]],[[240200,5471,344482,247972,755320]],[230497095],[[343447,405697,681062,693906,987571]],[875198145],[556259265],[[374368,385647,110593,667881,665376]],[[887209,823362,63784,779450,266752]],[868737680],[144845275],[383508580],[921012670],[298579885],[133180555],[[910314,607031,165,617788,138227]],[412948515],[439564120],[[128208,659666,452184,531386,6854]],[109540555],[495037185],[[612207,51305,18775,896288,695225]],[932540805],[467128975],[[80895,47225,536813,299239,605811]],[635988090],[[986063,307528,346819,437167,378711]],[220985165],[953573365],[[966153,395914,115817,71638,88534]],[[687027,594310,614797,134300,236869]],[418857735],[[306860,403144,553921,19892,194931]],[820107540],[640290840],[370152015],[[118984,931934,574313,35776,328736]],[[718988,125697,6891,679455,310540]],[263430160],[894356060],[693980375],[[706554,601584,207444,280311,569540]],[[626373,377287,326317,131202,270873]],[[376234,40174,576055,8190,867436]],[898399225],[334221705],[261678275],[67896200],[74844865],[[808395,751993,256915,407750,218915]],[[861632,761170,835281,512968,112263]],[244505],[702718995],[[473969,29870,586981,525277,55234]]]
["ATM","deposit","withdraw"]
, [[], [[3768213, 4227276, 5128041, 3022862, 3772701]], [875306040]]
]
ssa = ATM(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret, f"store={ssa.store}")
    result.append(ret)
print(result)