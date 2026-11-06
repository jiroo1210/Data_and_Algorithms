import math
import latexify

# The decorator tells latexify to convert this function
@latexify.function
def solve(a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

# Print the raw LaTeX string to the terminal
print(solve)