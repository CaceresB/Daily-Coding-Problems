'''
Daily Coding Problem #1

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

n = int(input("Number of elements in the list: "))

l = []

for j in range(n):
    l+=[int(input("Enter a number: "))]

k= int(input("Does this list add up to: "))

r = False

for i in l:
    t = k-i
    if t in l and t!=i:
        r=True

print(r)
