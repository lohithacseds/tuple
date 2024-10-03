//
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
//
n = int(input())
my_tuple = tuple(int(input()) for _ in range(n))
print(max(my_tuple))  
