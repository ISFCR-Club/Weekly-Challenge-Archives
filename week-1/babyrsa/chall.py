from Crypto.Util.number import (
  getPrime,
  bytes_to_long,
  GCD
)

def get_good_prime (e, nbits):
  while True:
    p = getPrime(nbits)
    if GCD(p - 1, e) == 1:
      return p

flag = b'isfcr{qu4dr4t1c_3quation5_f0r_th333_w1n}'
# flag = b'isfcr{fake_flag_of_same_length_xxxxxxxx}'

assert(len(flag) == 40)

flag1 = flag[00:20]
flag2 = flag[20:40]

e = 65537
nbits = 512

p1 = get_good_prime(e, nbits)
q1 = get_good_prime(e, nbits)
p2 = get_good_prime(e, nbits)
q2 = get_good_prime(e, nbits)

n1 = p1 * q1
n2 = p2 * q2
c1 = pow(bytes_to_long(flag1), e, n1)
c2 = pow(bytes_to_long(flag2), e, n2)

with open('cipher.txt', 'w') as file:
  print("e =", e, file = file)
  print("n1 =", n1, file = file)
  print("n2 =", n2, file = file)
  print("c1 =", c1, file = file)
  print("c2 =", c2, file = file)
  print("p1 + q1 =", p1 + q1, file = file)
  print("p2 - q2 =", p2 - q2, file = file)
