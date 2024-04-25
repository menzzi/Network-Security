from Crypto.Cipher import DES  # DES 암호화를 위한 DES 모듈
from Crypto.Random import get_random_bytes  # 임의의 랜덤 키를 생성하기 위한 함수
from Crypto.Util.Padding import pad, unpad # 데이터 패딩 :  DES는 고정된 블록 크기를 필요

def generate_des_key():

    key = get_random_bytes(8) # 8바이트 키 생성
    adjusted_key = key[:7] + bytes([key[7] & 0xFE]) # 8번째 바이트의 상위 1비트를 제거하여 56비트로 조정(DES : 56비트 키 사용)
    return adjusted_key
def encrypt_message(message, key): # message를 key를 사용하여 DES 암호화 알고리즘으로 암호화
    cipher = DES.new(key, DES.MODE_ECB) # DES 알고리즘을 사용하여 새로운 DES 객체를 생성. key : DES 암호화에 사용될 키, DES.MODE_ECB : DES의 동작 모드
    padded_message = pad(message.encode(), DES.block_size) # 암호화 하기전 블록 크기에 맞게 메세지 패딩
    encrypted_message = cipher.encrypt(padded_message) #  DES 암호화 알고리즘을 사용하여 패딩된 메시지를 암호화
    return encrypted_message # 암호화된 메세지 반환

def decrypt_message(encrypted_message, key): #key를 사용하여 암호화된 메세지 복호화
    cipher = DES.new(key, DES.MODE_ECB) # DES 객체를 생성
    decrypted_message = cipher.decrypt(encrypted_message) # DES 알고리즘을 사용하여 ECB 모드로 복호화
    unpadded_message = unpad(decrypted_message, DES.block_size) # 암호화때 추가한 패딩을 제거
    return unpadded_message.decode() # 복호화된 메시지를 디코딩하여 문자열로 변환 후 반환

if __name__ == "__main__":
    # 56비트 키 생성
    key = generate_des_key()

    # 암호화할 메시지
    message = "Hello, this is a DES Algorithm"

    # 메시지 암호화
    encrypted_message = encrypt_message(message, key)
    print("Encrypted message:", encrypted_message)

    # 암호화된 메시지 복호화
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted message:", decrypted_message)
