# Author: Jiarou Deng dpj5243@psu.edu
# Collaborator: Aaron Hester amh7806@psu.edu
# Collaborator: Kyle Chen kvc5823@psu.edu
# Collaborator: Livia Moore lmm6882@psu.edu
# Section: 010R
# Breakout: 11

# Calculate the sum of 1+2+3+... + n by recursive function
def sum_n(n):
  l=0;c=0
  if l <= "n":
    c= c+l
    l= (l+1)
  return c

# Print string s one in a new line n times by recursive function
def print_n(s,n):
 d=0
 if d <= "n":
  print(f"{s}\n")

def run():
 n= float(input("Enter an int: "))
 print(f"sum is {sum_n(n)}.")   
 g= input("Enter a string: ")
 print_n(g,n)

if __name__ == "__main__":
 run()