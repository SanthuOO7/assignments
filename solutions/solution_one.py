'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def sum_of_integers(ar, j, k):
    l = len(ar)
    for i in range(1, l):
        ar[i] = ar[i] + ar[i-1]
    if j > 0:
        print(ar[k] - ar[j-1])
    else:
        print(ar[k])

no_of_testcases = int(input())
for i in range(no_of_testcases):
    arr_length = int(input())
    in_arr = input()
    in_arr = in_arr.split(" ")
    in_arr = [int(st) for st in in_arr]
    no_of_queries = int(input())
    for q in range(no_of_queries):
        indexes = input()
        indexes = indexes.split(" ")
        indexes = [int(ind) for ind in indexes]
        l_index = indexes[0]
        r_index = indexes[1]
        arr = in_arr[:]
        sum_of_integers(arr, l_index-1, r_index-1)
        
