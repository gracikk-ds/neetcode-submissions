class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        counter: list[int] = []
        for string in strs:
            counter.append(str(len(string)))
        counter_str = ",".join(counter)
        counter_str += "#"
        counter_str += "".join(strs)
        return counter_str
        
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        counter_str, real_strings = s.split("#", 1)
        counter = counter_str.split(",")
        decoded_strings = []
        start_idx = 0
        for sep in counter:
            end_idx = start_idx + int(sep)
            decoded_strings.append(real_strings[start_idx: end_idx])
            start_idx += int(sep)
        return decoded_strings
        
