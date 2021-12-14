import sys
from math import ceil

with open(sys.argv[1]) as file:
    values = file.read().splitlines()

def get_rating(nums, i, co2):
        if len(nums) == 1:
            return nums[0]
        
        else:
            ones = sum([num[i]=='1' for num in nums]) #number of ones in the column being considered
            
            comparator = '0'

            if (co2==True and ones < ceil(len(nums)/2)) or (co2==False and ones >= ceil(len(nums)/2)) :
                comparator = '1'

            nums = [num for num in nums if num[i]==comparator] #filter the list

            return get_rating(nums,i+1,co2)


o2 = get_rating(values,0, co2=False)
co2 = get_rating(values,0, co2=True)

print(int(o2,2)*int(co2,2))






