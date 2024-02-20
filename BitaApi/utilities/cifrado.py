import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad,pad

class AESCipher(object):

    def __init__(self):
        self.bs = AES.block_size
        self.iv = b'8080808080801234'
        self.key = b'8080808080801234'

    def encrypt(self, raw):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(pad(raw.encode(),AES.block_size))).decode('utf-8')

    def decrypt(self, enc):
        try:
            enc = base64.b64decode(enc)
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            return unpad(cipher.decrypt(enc),AES.block_size).decode('utf-8')
        except:
            return ""

    def validate(self, psw1, psw2):
        psw1_decrypted = self.decrypt(psw1)
        psw2_decrypted = self.decrypt(psw2)
        return psw1_decrypted == psw2_decrypted
    
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]