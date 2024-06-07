import math
import statistics

# Defining the functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def sqrt(a):
    return math.sqrt(a)

def percentage(a, b):
    return (a / b) * 100

def exp(a, b):
    return a ** b

def mod(a, b):
    return a % b

def factorial(a):
    return math.factorial(a)

def log(a, base):
    return math.log(a, base)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def abs_val(a):
    return abs(a)

def floor_val(a):
    return math.floor(a)

def ceil_val(a):
    return math.ceil(a)

def asin(a):
    return math.degrees(math.asin(a))

def acos(a):
    return math.degrees(math.acos(a))

def atan(a):
    return math.degrees(math.atan(a))

def sinh(a):
    return math.sinh(a)

def cosh(a):
    return math.cosh(a)

def tanh(a):
    return math.tanh(a)

def asinh(a):
    return math.asinh(a)

def acosh(a):
    return math.acosh(a)

def atanh(a):
    return math.atanh(a)

def log2(a):
    return math.log2(a)

def power_of_10(a):
    return 10 ** a

def gcd(a, b):
    return math.gcd(a, b)

def cbrt(a):
    return a ** (1 / 3)

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def nth_root(a, n):
    return a ** (1 / n)

def power_of_2(a):
    return 2 ** a

def power_of_e(a):
    return math.exp(a)

def gamma(a):
    return math.gamma(a)

def erf(a):
    return math.erf(a)

def erfc(a):
    return math.erfc(a)

def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

def bitwise_xor(a, b):
    return a ^ b

def bitwise_not(a):
    return ~a

def shift_left(a, n):
    return a << n

def shift_right(a, n):
    return a >> n

def real_part(a):
    return a.real

def imag_part(a):
    return a.imag

def magnitude(a):
    return abs(a)

def phase(a):
    return math.phase(a)

def conjugate(a):
    return a.conjugate()

def mean(numbers):
    return statistics.mean(numbers)

def median(numbers):
    return statistics.median(numbers)

def mode(numbers):
    return statistics.mode(numbers)

def stdev(numbers):
    return statistics.stdev(numbers)

def variance(numbers):
    return statistics.variance(numbers)

# Displaying the options
print('Select Option:')
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Percentage")
print("7. Exponentiation")
print("8. Modulus")
print("9. Factorial")
print("10. Logarithm")
print("11. Sine")
print("12. Cosine")
print("13. Tangent")
print("14. Absolute Value")
print("15. Floor")
print("16. Ceiling")
print("17. Inverse Sine")
print("18. Inverse Cosine")
print("19. Inverse Tangent")
print("20. Hyperbolic Sine")
print("21. Hyperbolic Cosine")
print("22. Hyperbolic Tangent")
print("23. Inverse Hyperbolic Sine")
print("24. Inverse Hyperbolic Cosine")
print("25. Inverse Hyperbolic Tangent")
print("26. Logarithm Base 2")
print("27. Power of 10")
print("28. Greatest Common Divisor")
print("29. Cube Root")
print("30. Square")
print("31. Cube")
print("32. Nth Root")
print("33. Power of 2")
print("34. Power of E")
print("35. Gamma Function")
print("36. Error Function")
print("37. Complementary Error Function")
print("38. Bitwise AND")
print("39. Bitwise OR")
print("40. Bitwise XOR")
print("41. Bitwise NOT")
print("42. Shift Left")
print("43. Shift Right")
print("44. Real Part of Complex Number")
print("45. Imaginary Part of Complex Number")
print("46. Magnitude of Complex Number")
print("47. Phase of Complex Number")
print("48. Conjugate of Complex Number")
print("49. Mean")
print("50. Median")
print("51. Mode")
print("52. Standard Deviation")
print("53. Variance")

# Taking input from user
choice = int(input("Enter a Choice 1-53: "))

if choice in [1, 2, 3, 4, 6, 7, 8, 28, 32, 38, 39, 40, 42, 43]:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
elif choice in [17, 18, 19, 20, 21, 22, 23, 24, 25]:
    num = float(input("Enter the Value (-1 to 1): "))
elif choice in [30, 31, 33, 34, 35, 36, 37]:
    num = float(input("Enter the Number: "))
elif choice in [9, 5]:
    num = int(input("Enter the Number: "))
elif choice in [49, 50, 51, 52, 53]:
    numbers = list(map(float, input("Enter the Numbers (separated by spaces): ").split()))

if choice == 1:
    print(f'Addition of {num1} and {num2} is {add(num1, num2)}')
elif choice == 2:
    print(f'Subtraction of {num1} and {num2} is {sub(num1, num2)}')
elif choice == 3:
    print(f'Multiplication of {num1} and {num2} is {mul(num1, num2)}')
elif choice == 4:
    print(f'Division of {num1} and {num2} is {div(num1, num2)}')
elif choice == 5:
    print(f'Square Root of {num} is {sqrt(num)}')
elif choice == 6:
    print(f'Percentage of {num1} relative to {num2} is {percentage(num1, num2)}%')
elif choice == 7:
    print(f'Exponentiation of {num1} to the power of {num2} is {exp(num1, num2)}')
elif choice == 8:
    print(f'Modulus of {num1} by {num2} is {mod(num1, num2)}')
elif choice == 9:
    print(f'Factorial of {num} is {factorial(num)}')
elif choice == 10:
    base = float(input("Enter the Logarithm Base: "))
    print(f'Logarithm of {num} with base {base} is {log(num, base)}')
elif choice == 11:
    print(f'Sine of {num} degrees is {sin(num)}')
elif choice == 12:
    print(f'Cosine of {num} degrees is {cos(num)}')
elif choice == 13:
    print(f'Tangent of {num} degrees is {tan(num)}')
elif choice == 14:
    print(f'Absolute value of {num} is {abs_val(num)}')
elif choice == 15:
    print(f'Floor value of {num} is {floor_val(num)}')
elif choice == 16:
    print(f'Ceiling value of {num} is {ceil_val(num)}')
elif choice == 17:
    print(f'Inverse Sine of {num} is {asin(num)} degrees')
elif choice == 18:
    print(f'Inverse Cosine of {num} is {acos(num)} degrees')
elif choice == 19:
    print(f'Inverse Tangent of {num} is {atan(num)} degrees')
elif choice == 20:
    print(f'Hyperbolic Sine of {num} is {sinh(num)}')
elif choice == 21:
    print(f'Hyperbolic Cosine of {num} is {cosh(num)}')
elif choice == 22:
    print(f'Hyperbolic Tangent of {num} is {tanh(num)}')
elif choice == 23:
    print(f'Inverse Hyperbolic Sine of {num} is {asinh(num)}')
elif choice == 24:
    print(f'Inverse Hyperbolic Cosine of {num} is {acosh(num)}')
elif choice == 25:
    print(f'Inverse Hyperbolic Tangent of {num} is {atanh(num)}')
elif choice == 26:
    print(f'Logarithm base 2 of {num} is {log2(num)}')
elif choice == 27:
    print(f'10 raised to the power of {num} is {power_of_10(num)}')
elif choice == 28:
    print(f'Greatest common divisor of {num1} and {num2} is {gcd(num1, num2)}')
elif choice == 29:
    print(f'Cube root of {num} is {cbrt(num)}')
elif choice == 30:
    print(f'Square of {num} is {square(num)}')
elif choice == 31:
    print(f'Cube of {num} is {cube(num)}')
elif choice == 32:
    n = float(input("Enter the Root Value: "))
    print(f'The {n}th root of {num} is {nth_root(num, n)}')
elif choice == 33:
    print(f'2 raised to the power of {num} is {power_of_2(num)}')
elif choice == 34:
    print(f'e raised to the power of {num} is {power_of_e(num)}')
elif choice == 35:
    print(f'Gamma function of {num} is {gamma(num)}')
elif choice == 36:
    print(f'Error function of {num} is {erf(num)}')
elif choice == 37:
    print(f'Complementary error function of {num} is {erfc(num)}')
elif choice == 38:
    print(f'Bitwise AND of {num1} and {num2} is {bitwise_and(num1, num2)}')
elif choice == 39:
    print(f'Bitwise OR of {num1} and {num2} is {bitwise_or(num1, num2)}')
elif choice == 40:
    print(f'Bitwise XOR of {num1} and {num2} is {bitwise_xor(num1, num2)}')
elif choice == 41:
    print(f'Bitwise NOT of {num1} is {bitwise_not(num1)}')
elif choice == 42:
    n = int(input("Enter the number of shifts: "))
    print(f'Shift left of {num1} by {n} positions is {shift_left(num1, n)}')
elif choice == 43:
    n = int(input("Enter the number of shifts: "))
    print(f'Shift right of {num1} by {n} positions is {shift_right(num1, n)}')
elif choice == 44:
    complex_num = complex(input("Enter a complex number (a+bj): "))
    print(f'Real part of {complex_num} is {real_part(complex_num)}')
elif choice == 45:
    complex_num = complex(input("Enter a complex number (a+bj): "))
    print(f'Imaginary part of {complex_num} is {imag_part(complex_num)}')
elif choice == 46:
    complex_num = complex(input("Enter a complex number (a+bj): "))
    print(f'Magnitude of {complex_num} is {magnitude(complex_num)}')
elif choice == 47:
    complex_num = complex(input("Enter a complex number (a+bj): "))
    print(f'Phase of {complex_num} is {phase(complex_num)}')
elif choice == 48:
    complex_num = complex(input("Enter a complex number (a+bj): "))
    print(f'Conjugate of {complex_num} is {conjugate(complex_num)}')
elif choice == 49:
    print(f'Mean of {numbers} is {mean(numbers)}')
elif choice == 50:
    print(f'Median of {numbers} is {median(numbers)}')
elif choice == 51:
    print(f'Mode of {numbers} is {mode(numbers)}')
elif choice == 52:
    print(f'Standard deviation of {numbers} is {stdev(numbers)}')
elif choice == 53:
    print(f'Variance of {numbers} is {variance(numbers)}')
else:
    print("INVALID CHOICE!!!")
