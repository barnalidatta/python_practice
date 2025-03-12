# Two pointer method

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Sort the array
        nums.sort()
        new_list = []
        # set pointers
        left = 0
        right = len(nums) -1

        while left < right:
                sum = nums[left] + nums[right]
                print(f"{nums[left]}, {nums[right]}")
                if sum == target:
                        new_list.extend([left,right])
                        return new_list
                elif sum < target:
                        left += 1
                else:
                        right -=1       


def test_twoSum():
       assert twoSum([2,7,11,15],9) == [0,1]
# print(twoSum([2,7,11,15],9))
