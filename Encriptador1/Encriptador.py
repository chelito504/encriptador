from Crypto.Cipher import AES
from Crypto import Random
import shutil
key = "AED"
class EncriptadorDeArchivos :
    
    def __init__(self):
        pass
    
    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encriptar(self, mensaje, clave, key_size=256):
        mensaje = self.pad(mensaje)
        nos = Random.new().read(AES.block_size)
        cifrador = AES.new(clave, AES.MODE_CBC, nos)
        return nos + cifrador.encrypt(mensaje)

    def desencriptar(self, encriptado, clave):
        nos = encriptado[:AES.block_size]
        cifrador = AES.new(clave, AES.MODE_CBC, nos)
        text = cifrador.decrypt(encriptado[AES.block_size:])
        return text.rstrip(b"\0")

    def encriptador(self, archivo, clave):
        try:
            with open(archivo, 'rb') as ac:
                text = ac.read()
                enc = self.encriptar(text, clave)
            with open(archivo + ".enc", 'wb') as ac:
                ac.write(enc)
            print "archivo encriptado"
        except Exception as variable:
            print "El archivo no existe"

    def desencriptador(self, archivo, clave):
        if ".enc" in archivo:
            try:
                with open(archivo.strip("u"), 'rb') as ad:
                    ct = ad.read()
                    dec = self.desencriptar(ct, clave)
                with open("dec." + archivo[:-4], 'wb') as ad:
                    ad.write(dec)
                print "archivo desencriptado"
            except Exception as variable:
                print "El archivo no existe"
        elif "dec" in archivo:
            print "El archivo ya fue desencriptado"
        else:
            print "El archivo ingresado no ha sido encriptado"

