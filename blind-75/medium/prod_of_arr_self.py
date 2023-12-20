class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def get_prod(lst):
            prod = 1

            for i in lst:
                if i != 0:
                    prod *= i
            return prod
        
        answer = []
        total_sum = get_prod(nums)

        if 0 in nums:
            if nums.count(0) == 1:
                return [0 if i != 0 else total_sum for i in nums]
            else:
                return [0 for _ in nums]

        for i in range(len(nums)):
            if nums[i] != 0:
                total = total_sum / nums[i]
                answer.append(int(total))
            else:
                answer.append(int(total_sum))
        

        return answer
