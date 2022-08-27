from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        exp_train = 0
        eng_train = 0
        for i in range(len(energy)):
            if initialEnergy + eng_train <= energy[i]:
                eng_train += energy[i] + 1 - (initialEnergy + eng_train)
            initialEnergy -= energy[i]
        # print(eng_train)

        for i in range(len(experience)):
            if initialExperience + exp_train <= experience[i]:
                exp_train += experience[i] + 1 - (initialExperience + exp_train)
            initialExperience += experience[i]
        # print(exp_train)

        return exp_train + eng_train

initialEnergy = 5
initialExperience = 3
energy = [1,4,3,2]
experience = [2,6,3,1]

r = Solution().minNumberOfHours(initialEnergy, initialExperience, energy, experience)
print(r)