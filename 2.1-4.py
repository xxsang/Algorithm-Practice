# Sum of two binary digits

def binary_sum(bin_a, bin_b):
    bin_c = bin(bin_a+bin_b)
    return bin_c

# Test the code
bin_a = 0b0001
bin_b = 0b101010
print binary_sum(bin_a, bin_b)

