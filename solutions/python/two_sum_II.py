class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            added = numbers[l] + numbers[r]
            if added == target:
                return [l+1, r+1]
            elif added > target:
                r -= 1
            else:
                l += 1
