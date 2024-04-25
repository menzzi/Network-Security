```py
import random

# 소수 판별 (입력 받은 p, q가 소수임을 판별하기 위한 함수)
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 최대공약수 계산
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 확장 유클리드 알고리즘
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

# 모듈러 역수 계산(d를 구하기 위함)
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# 소수 입력 받기
def input_prime(prompt):
    while True:
        num = int(input(prompt))
        if is_prime(num):
            return num
        else:
            print("소수를 입력해주세요") # 소수가 아니면 ‘소수를 입력해주세요’출력

# 공개키 및 개인키 생성
def generate_keypair(p, q):

# d*e를 (p-1)(q-1)로 나누었을 때 나머지가 1인 정수 d를 구한다 (확장된 유클리드 호제법 이용)
    n = p * q
    phi = (p - 1) * (q - 1)
# phi 보다 작고 phi와 서로소인 e를 구한다.
    while True: 
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
#모듈러 역수를 통해 d*e 를 phi로 나눴을 때 나머지가 1인 정수 d를 구한다.
d = modinv(e, phi) 
    return ((e, n), (d, n))

# 암호화
def encrypt(pk, plaintext):
    key, n = pk
# ord(char) 함수는 주어진 문자 char의 유니코드 코드 포인트를 반환
# key = 공개키(e), n = 모듈러 값. 각 문자의 코드 포인트를 공개키(e)로 거듭제곱한 뒤, 그 결과를 모듈러 값(n)으로 나눈 나머지를 계산
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

# 복호화(개인키와 암호화 된 메세지)
def decrypt(pk, ciphertext):
    key, n = pk
# chr 함수는 주어진 숫자에 해당하는 유니코드 문자를 반환
# 거듭제곱을 계산한 결과를 문자로 다시 변환하여 복호화
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    # 소수 입력 받기
    p = input_prime("Enter a prime number (p): ")
    q = input_prime("Enter another prime number (q): ")

    # 공개키 및 개인키 생성
    public, private = generate_keypair(p, q)
    print("Public Key:", public)
    print("Private Key:", private)

    # 사용자로부터 암호화할 메시지 입력
    message = input("Enter a message to encrypt: ")
    
    # 암호화(공개키를 사용하여 암호화)
    encrypted_msg = encrypt(public, message)
    print("Encrypted Message:", encrypted_msg)
    
    # 복호화(개인키를 사용하여 복호화)
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)
```
 

 
소수가 아닌 값 입력했을 때 ‘소수를 입력해주세요.” 출력

두 소수 p,q를 입력 받아 공개키와 개인키를 생성하고 평문을 입력 받아 암호화와 복호화하는 코드를 구현하였다. 
공개키는 <e,n> (n = p*q , e = phi 보다 작고 phi와 서로소) 이고, 개인키는<d,n> (d : d*e를 (p-1)(q-1)로 나누었을 때 나머지가 1인 정수) 이다.
