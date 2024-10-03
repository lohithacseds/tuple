//
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
//
my_tuple = tuple(map(int, input().split()))
sum_of_elements = 0
for num in my_tuple:
    sum_of_elements += num
print(sum_of_elements)  
