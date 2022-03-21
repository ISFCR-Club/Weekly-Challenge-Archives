from Crypto.Util.number import (
  getPrime,
  bytes_to_long,
  GCD
)

from sympy import nextprime

def get_good_prime (e, nbits):
  while True:
    p = getPrime(nbits)
    if GCD(p - 1, e) == 1:
      return p

flag = b'isfcr{5kr1p7_k1dd13s_u53_RsaCtfTool_f0r_th3_w1n}'
# flag = b'isfcr{fake_flag_of_same_length_xxxxxxxxxxxxxxxx}'

assert(len(flag) == 48)

flag1 = bytes_to_long(flag[00:12])
flag2 = bytes_to_long(flag[12:24])
flag3 = bytes_to_long(flag[24:36])
flag4 = bytes_to_long(flag[36:48])

e1 = 65537
nbits1 = 64
p1 = get_good_prime(e1, nbits1)
q1 = get_good_prime(e1, nbits1)
n1 = p1 * q1

e2 = 3
nbits2 = 512
p2 = get_good_prime(e2, nbits2)
q2 = get_good_prime(e2, nbits2)
n2 = p2 * q2

e3 = 0x10001
nbits3 = 512
# p3 = get_good_prime(e3, nbits3)
# q3 = nextprime(p3)
# n3 was generated using the above two statements
n3 = 0xa1e86e00a95a9e288edd528f247cff49e835708d88c22bc99b9f6f18635abb4c5cf5d7b433687e18dafac46e5b63ed3bb2b57cb700fd33cbdcfe2b97f97b42b3ec473cb87aeadc1855121a1af3a4eabca2ba31fbf7ad3fdc3830b79f92945dbf3117d114673f5d272cee06121cfdee2e4e3681c3020e4db3813ead46a9230a65

e4 = 0x0285f8d4fe29ce11605edf221868937c1b70ae376e34d67f9bb78c29a2d79ca46a60ea02a70fdb40e805b5d854255968b2b1f043963dcd61714ce4fc5c70ecc4d756ad1685d661db39d15a801d1c382ed97a048f0f85d909c811691d3ffe262eb70ccd1fa7dba1aa79139f21c14b3dfe95340491cff3a5a6ae9604329578db9f5bcc192e16aa62f687a8038e60c01518f8ccaa0befe569dadae8e49310a7a3c3bddcf637fc82e5340bef4105b533b6a531895650b2efa337d94c7a76447767b5129a04bcf3cd95bb60f6bfd1a12658530124ad8c6fd71652b8e0eb482fcc475043b410dfc4fe5fbc6bda08ca61244284a4ab5b311bc669df0c753526a79c1a57
n4 = 0x2aeb637f6152afd4fb3a2dd165aec9d5b45e70d2b82e78a353f7a1751859d196f56cb6d11700195f1069a73d9e5710950b814229ab4c5549383c2c87e0cd97f904748a1302400dc76b42591da17dabaf946aaaf1640f1327af16be45b8830603947a9c3309ca4d6cc9f1a2bcfdacf285fbc2f730e515ae1d93591ccd98f5c4674ec4a5859264700f700a4f4dcf7c3c35bbc579f6ebf80da33c6c11f68655092bbe670d5225b8e571d596fe426db59a6a05aaf77b3917448b2cfbcb3bd647b46772b13133fc68ffabcb3752372b949a3704b8596df4a44f085393ee2bf80f8f393719ed94ab348852f6a5e0c493efa32da5bf601063a033beaf73ba47d8205db

ciphertext1 = pow(flag1, e1, n1)
ciphertext2 = pow(flag2, e2, n2)
ciphertext3 = pow(flag3, e3, n3)
ciphertext4 = pow(flag4, e4, n4)

keys = [
  (n1, e1, ciphertext1),
  (n2, e2, ciphertext2),
  (n3, e3, ciphertext3),
  (n4, e4, ciphertext4),
]

with open('cipher.txt', 'w') as file:
  for index, key in enumerate(keys, start = 1):
    print(f'n{index} =', key[0], file = file)
    print(f'e{index} =', key[1], file = file)
    print(f'c{index} =', key[2], file = file)
    print(file = file)
