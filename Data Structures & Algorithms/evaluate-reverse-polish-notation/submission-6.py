class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "/", "-", "*"])
        s = []
        if len(tokens)==1:
            return int(tokens[0])

        for i in tokens:
            if i in operators:
                n1 = s.pop()
                n2 = s.pop()
                if i == "+":
                    s.append(n2 + n1)
                elif i == "-":
                    s.append(n2 - n1)
                elif i == "*":
                    s.append(n2 * n1)
                elif i == "/":
                    s.append(int(n2 / n1))
            else:
                s.append(int(i))

        return s[0]
