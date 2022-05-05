'''
Daily Problem 4
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

n = int(input("length of list: "))

l=[]

for k in range(n):
    l+=[int(input("Enter a number: "))]

l.sort()

temp = False
m = 0

for i in range(len(l)-1):
    if l[i] +1 != l[i+1]:
        m = l[i]+1
        temp = True

if temp==False:
    m = l[-1]+1

print(m)
