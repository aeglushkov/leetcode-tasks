class Solution:
    # Solution 1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = dict()
        for i in range(len(numbers)):
            get = ans.get(numbers[i])
            if get is not None:
                return [get + 1, i + 1]
            ans[target - numbers[i]] = i
            
    # Solution 2
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     first = 0
    #     second = 1
    #     while first < len(numbers) - 1:
    #         sum_ = numbers[first] + numbers[second]
    #         if sum_ == target:
    #             return [first + 1, second + 1]
    #         elif (sum_ > target) or (second + 1 == len(numbers)):
    #             first += 1
    #             second = first + 1
    #         elif numbers[first] == numbers[second]:
    #             first = second
    #             second += 1
    #         else:
    #             second += 1
