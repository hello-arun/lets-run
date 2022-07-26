from numpy import fft
fft_a = fft.fft([9, -10, 7, 6, 0, 0, 0, 0])
fft_b = fft.fft([-5, 4, 0, -2, 0, 0, 0, 0])

mul = [a*b for a, b in zip(fft_a, fft_b)]

ifft_ab = fft.ifft(mul)

print(ifft_ab)
