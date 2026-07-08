class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == '+':
                sumElem = int(stack[-1]) + int(stack[-2])
                stack.append(sumElem)
            elif operations[i] == 'D':
                doubledElem = 2 * int(stack[-1])
                stack.append(doubledElem)
            elif operations[i] == 'C':
                stack.pop()
            else:
                stack.append(int(operations[i]))
        return sum(stack)

        