# Two pointer method plus third loop variable

def threeSum(nums):
        """
        3 number adds to 0
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        # targetsum = 0
        new_list = []
        # list_new_list = []
        # first looping variable (fix) on 0 element
        # and apply two sum on rest
        for i in range(n-2):
                
                left = i+1
                right = n-1
                while left < right:
                        sum = nums[i] + nums[left] + nums[right]
                        print(f"{sum}")
                        if sum == 0:
                                new_list.append([nums[i], nums[left],nums[right]])
                                break
                        elif sum < 0:
                                left +=1
                        else:
                                right -=1
        return new_list
                
def test_threeSum():
        assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]

# print(threeSum([-1,0,1,2,-1,-4]))
          