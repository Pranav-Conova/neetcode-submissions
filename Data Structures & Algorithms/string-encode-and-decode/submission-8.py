import ast
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = {}
        for i, string in enumerate(strs):
            result[i] = string
        return str(result)
    def decode(self, s: str) -> List[str]:
        result_dict = ast.literal_eval(s)
        return [n for _, n in result_dict.items()]
