class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    record.append(int(record[-2]) + int(record[-1]))
                    print(f"+ {record}")
                case "C":
                    record.pop()
                    print(f"C {record}")
                
                case "D":
                    record.append(int(record[-1]) * 2)
                    print(f"D {record}")

                case _ :
                    record.append(int(operations[i]))
                    print(f"other {record}")

        res = 0
        for i in range(len(record)):
            res += int(record[i])
            print(res)
        return res