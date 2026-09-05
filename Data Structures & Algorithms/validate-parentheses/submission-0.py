class Solution:
    def isValid(self, s: str) -> bool:
        #Мы заводим словарь - мэтчер для скобок: ]->[, }->{, )->(, далее заполняем стек следующим образом: append'им к input прочитанный символ - если c in bracket_dict то смотрим: input.pop == bracket_dict[c]? Если нет - return false. Если да - то просто продолжаем. Если под конец в input остались скобки - return False
        brackets_dict  = {"}":"{", "]":"[", ")":"("}
        inp = []

        for c in s:
            if c in brackets_dict.keys():
                if len(inp) == 0:
                    return False
                if not (brackets_dict[c] == inp.pop()):
                    return False
            else:
                inp.append(c)
        if len(inp) > 0:
            return False
        return True
        