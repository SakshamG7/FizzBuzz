# Sets up the variables/conditions for the FizzBuzz program
foo = (3, 5, 7)
bar = ("Fizz", "Buzz", "Bazz")

# Loops through the numbers 1 to 100 and prints the output
for i in range(1, 101):
    output = "" # Resets the output variable
    for j in range(len(foo)): # Loops through the conditions
        if i % foo[j] == 0: # If condition is met, add the output to the output variable
            output += bar[j]
    print(i, output)
