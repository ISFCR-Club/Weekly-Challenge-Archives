from Crypto.Util.number import *
import random
import socket

host = 'localhost'
port = 9999

modulus = 0xc4f8862619343f912fecded3b8d26a4d2eaded138a1510a20fda7fce9b3512bcd4a1117a7f91ed4fbf805ecd0e93bd851d7fc59581408a1d0551ec708112d26c25cbb1f9c8a249e96cb6898365c01ee14d3c4e231e98d733ac256cbf0343c76d03b5a5bdc97244c3b0bc2158a9bfc6c52f1ce128a60ad79c36d9285ffb75c7d1
base = 101
private_key = random.randint(2, modulus - 1)
public_key = pow(base, private_key, modulus)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

sock.send(f'Modulus: {hex(modulus)}\n'.encode())
sock.send(f'Base: {hex(base)}\n'.encode())
sock.send(f'Alice Private Key: {hex(private_key)}\n'.encode())
sock.send(f'Alice Public Key: {hex(public_key)}\n'.encode())

print(sock.recv(4096).decode())
