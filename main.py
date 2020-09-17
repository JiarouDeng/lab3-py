# Author: Jiarou Deng dpj5243@psu.edu
# Collaborator: Aaron Hester amh7806@psu.edu
# Collaborator: Kyle Chen kvc5823@psu.edu
# Collaborator: Livia Moore lmm6882@psu.edu
# Section: 010R
# Breakout: 11

# Calculate the sum of 1+2+3+... + n by recursive function
def sum_n(n):
  if n>0:
    return n+ sum_n(n-1)
  else:
    return n

# Print string s one in a new line n times by recursive function
def print_n(s,n):
  if n>0:
    print(f"{s}")
    print_n(s,n-1)
  

def run():
 n= int(input("Enter an int: "))
 print(f"sum is {sum_n(n)}.")   
 g= input("Enter a string: ")
 print_n(g,n)

if __name__ == "__main__":
 run()