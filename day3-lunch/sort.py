#!/usr/bin/env python

import random

# # generate a random list of numbers
# nums = []
#
# for i in xrange(4):
#     r = random.randint(1,100)
#     nums.append(r)
#
# print nums
#
# # sort the list
# nums.sort()

nums = range(0, 100, 10)
print nums

key =  86

# for i in xrange(len(nums)): # for i,v in enumerate(nums): is equivalent here
#     v = nums[i]
#     print "scanning: the %dth number is %d." % (i, v)
#     if (v == key):
#         print "Found %d at position %d." % (key, i)
        
#### BINARY SEARCH ####
lo = 0
hi = len(nums)
while (lo <= hi):
    mid = (lo + hi) / 2
    print "checking in the range [%d,%d]. Middle at position [%d]=%d." % (lo, hi, mid, nums[mid])
    if nums[mid] == key:
        print "I found the key, %d, at position %d." % (key, mid)
        break
    elif nums[mid] > key:
        hi = mid
    elif nums[mid] < key:
        lo = mid + 1