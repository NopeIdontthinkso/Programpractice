# sample input
# 5 -5
# 1 -10 5 6 9
# print two numbers in the list if the sum to s
# if they don't then print 'none'

line1 = input()
list1=line1.split()
n = int(list1[0])
s = int(list1[1])
list2 = input()
list2=list2.split()
nums = []
for i in list2:
    nums.append(int(i))

print(nums)