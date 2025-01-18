from typing import List

def getConcatenation(nums: List[int]) -> List[int]:
    ans = []
    for i in range(2):
        for j in nums:
            ans.append(j)

    return ans

if __name__ == '__main__':
    nums = [1, 2, 3]

    print(getConcatenation(nums))

