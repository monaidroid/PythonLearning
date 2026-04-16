# Run with python forLoop.Py
# For loop using Range funciton
# The range() function genrates a sequence of numbers, which can be used in a for loop to iterate a specific number of times.
for i in range(6):
    print ("Hello, world!") # Output : Hello, world! (printed 6 times)

print("\n\n") # output : print two new blank lines 
# 
names : list[str] = ["Alice", "Bob", "CHarlie", "David", "Eve", "Frank", "Grace"]
for name in names:
    print(f"Hello, {name}!") # Output : Hello, Alice!, Hello,Bob! and so on  

print("\n")
# The range() function can also take two arguments, start and stop, to generate a sequence of numbers within a specific range.
# Multiple lines of code can be executed within the loop by using indentation.
for j in range(1,11) :
    print(j) # Output : 1,2,3,4,5,6,7,8,9,10
    total = j+1
    print(f'Total {j} + 1 is:\t {total}') # Output: 2,3,4,5,6,7,8,9,10,11