//
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
//
n = int(input())
my_tuple = tuple(int(input()) for _ in range(n))
min_value = my_tuple[0]
for num in my_tuple:
    if num < min_value:
        min_value = num
print(min_value)  
