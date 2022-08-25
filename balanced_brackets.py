#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.


open_list = ["[","{","("] 
close_list = ["]","}",")"] 


def isBalanced(brackets):
    listBrackets = [] 
    for item in brackets: 
        if item in open_list: 
            listBrackets.append(item) 
        elif item in close_list: 
            pos = close_list.index(item) 
            if ((len(listBrackets) > 0) and
                (open_list[pos] == listBrackets[len(listBrackets)-1])): 
                listBrackets.pop() 
            else: 
                return "NO"
    if len(listBrackets) == 0: 
        return "YES"
    else: 
        return "NO"


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
