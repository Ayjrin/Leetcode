class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    record.append(int(record[i-2]) + int(record[i-1]))
                case "C":
                    record.pop()
                case "D":
                    record.append(int(record[-1]) * 2)
                case _ :
                    record.append(int(operations[i]))

        res = 0
        for i in range(len(record)):
            res += int(record[i])

        return res