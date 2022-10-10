# we will calculate product of two polynomial in this code
# using our own fft and ifft implementation
# Let's multiply
# A = 9 - 10x + 7x^2 + 6x^3
# B = -5 + 4x - 2x^3
# C = A*B = -45 + 86x - 75x^2 - 20x^3 + 44x^4 - 14x^5 - 12x^6

from main import fft, ifft, _round

a = [9, -10, 7, 6, 0, 0, 0, 0]
b = [-5, 4, 0, -2, 0, 0, 0, 0]
fft_a = fft(a)
fft_b = fft(b)

mul = [a*b for a, b in zip(fft_a, fft_b)]

# We need to divide by len(mul) in the final output
ifft_ab = ifft(mul)
ifft_ab = [i/len(mul) for i in ifft_ab]
print(f"          a : {_round(a)}")
print(f"          b : {_round(b)}")
print(f"q -> FFT(a) : {_round(fft_a)}")
print(f"r -> FFT(b) : {_round(fft_b)}")
print(f"mul ->  q*r : {_round(mul)}")
print(f"  IFFT(mul) : {_round(ifft_ab)}")

