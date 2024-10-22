def power_series(x, n):
  """Calculates the power series of x^n using a for loop.

  Args:
    x: The base number.
    n: The exponent.

  Returns:
    The calculated power series.
  """

  result = 1
  for i in range(1, n + 1):
    result *= x

  return result

# Get input from the user
x = float(input("Enter the base number: "))
n = int(input("Enter the exponent: "))

# Calculate the power series
power = power_series(x, n)

# Print the result
print(f"{x}^{n} = {power}")