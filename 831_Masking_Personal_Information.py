class Solution:
    def maskPII(self, s: str) -> str:
        if s.find("@") > -1:
            # mask an email
            s = s.lower()
            at_idx = s.find("@")
            left_part = s[:at_idx]
            right_part = s[at_idx + 1:]
            return f"{left_part[0]}*****{left_part[-1]}@{right_part}"
        else:
            # mask a phone number
            s = s.replace("+", "").replace("-", "").replace("(", "")\
                .replace(")", "").replace(" ", "")
            local_part = s[-10:]
            country_cd = s[:-10]
            new_cd = "+" + "*" * len(country_cd) + "-" if len(country_cd) > 0 else ""
            new_local = f"***-***-{local_part[-4:]}"
            return f"{new_cd}{new_local}"
        
    