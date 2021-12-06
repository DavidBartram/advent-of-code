import sys
from math import ceil

with open(sys.argv[1]) as file:
    values = file.read().splitlines()

def count_ones(nums,i):
    ones = 0
    for num in nums:
        if num[i] == '1':
            ones += 1
    return ones

def get_rating(nums, i, co2):
        if len(nums) == 1:
            return nums[0]
        
        else:
            filtered = []
            comparator = '0'
            if co2:
                comparator = '1'
            ones = count_ones(nums,i)
            if ones >= ceil(len(nums)/2):
                comparator = '1'
                if co2:
                    comparator = '0'

            for num in nums:
                if num[i] == comparator:
                    filtered.append(num)
            
            nums = filtered

            return get_rating(nums,i+1,co2)


o2 = get_rating(values,0, co2=False)
co2 = get_rating(values,0, co2=True)

print(int(o2,2)*int(co2,2))






