# link: https://leetcode.com/problems/running-sum-of-1d-array/
nums = [1,2,3,4]
solution = []
pointer = 0
# output [1,2,6,10]
# explaination [1,1+2,1+2+3,1+2+3+4]
for i in nums:
    pointer += i
    solution.append(pointer)
print(solution)
