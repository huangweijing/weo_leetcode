class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        tga = q / p
        m = 1
        while True:
            n = tga * m
            if n == int(n):
                n_mod_2 = n % 2
                m_mod_2 = m % 2
                if n_mod_2 == 0 and m_mod_2 == 1:
                    return 0
                elif n_mod_2 == 1 and m_mod_2 == 1:
                    return 1
                elif n_mod_2 == 1 and m_mod_2 == 0:
                    return 2
            m += 1

r = Solution().mirrorReflection(3, 1)
print(r)



