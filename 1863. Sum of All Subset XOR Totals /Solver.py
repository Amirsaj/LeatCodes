class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        ghasem1 = 0
        for i in range(2 ** len(nums)):
            # print('=====')
            # print(i)
            mola = []
            adad = 0
            hamin = str(bin(i)).split('b')[1]
            # print(hamin)
            ghasem = 0
            for j in hamin[::-1]:
                if j == '1':
                    ghasem = ghasem ^ int(nums[adad])
                    print('hale', ghasem, int(nums[adad]), ghasem ^ int(nums[adad]))
                    mola.append(nums[adad])

                adad = adad + 1
            ghasem1 += ghasem
        return ghasem1

