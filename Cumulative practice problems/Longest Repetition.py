# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return lst[0]
    max = 0
    times = 1
    elem = lst[0]
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1]:
            if times > max:
                max = times
                elem = lst[i-1]
            times = 1
        else:
          times = times + 1
    if times > max:
      max = times
      elem = lst[i-1]  
    return elem


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

