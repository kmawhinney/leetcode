class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # If in left-sorted portion
            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # If in right-sorted portion
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
