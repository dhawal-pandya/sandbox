import sys
import ctypes

a = "Pandya"

print(sys.getrefcount(a))
print("sys")


def ref_count(address):
    return ctypes.c_long.from_address(address).value


x = "Dhawal"

print(ref_count(id(x)))
print("ctypes")
