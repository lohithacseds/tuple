//
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
//
n = int(input())
my_tuple = tuple(int(input()) for _ in range(n))
print(sum(my_tuple))  
