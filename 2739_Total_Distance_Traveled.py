class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        fuel_used = 0
        while mainTank > 0:
            mainTank -= 1
            fuel_used += 1
            distance += 10
            if fuel_used % 5 == 0:
                if additionalTank >= 1:
                    mainTank += 1
                    additionalTank -= 1
        return distance
