import numpy as np

# using numpy
arr = np.array([1, 15, 100, 256, 8755], dtype=np.int16)
swap_bytes_arr = arr.byteswap(inplace=True)


# using bitwise operators
def swap_bytes(n: int) -> int:
    return ((n & 0xFF) << 8) | (n >> 8)


assert swap_bytes(1) == swap_bytes_arr[0]
assert swap_bytes(15) == swap_bytes_arr[1]
assert swap_bytes(100) == swap_bytes_arr[2]
assert swap_bytes(256) == swap_bytes_arr[3]
assert swap_bytes(8755) == swap_bytes_arr[4]
