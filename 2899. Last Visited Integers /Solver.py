class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        lastint = []
        numberbback = -1
        doros = []
        aya = 0
        for i in words:
            if i == 'prev':
                aya += 1
                if len(lastint) >= aya and not len(lastint) == 0:
                    doros.append(int(lastint[numberbback]))
                else:
                    doros.append(-1)
                numberbback -= 1
            else:
                numberbback = -1
                aya = 0
                lastint.append(i)
        return doros
