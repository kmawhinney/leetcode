class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = []
        tens = []
        twenties = []

        for bill in bills:
            if bill == 5:
                fives.append(5)
                continue
            elif bill == 10 and fives:
                tens.append(10)
                fives.pop()
                continue
            elif bill == 20:
                if tens and fives:
                    twenties.append(20)
                    tens.pop()
                    fives.pop()
                    continue
                elif len(fives) > 2:
                    twenties.append(20)
                    fives.pop()
                    fives.pop()
                    fives.pop()
                    continue
            return False
        return True
