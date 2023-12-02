from ensurepip import version


src = 'D2FE28'


def binToHex (binary):
    hexRaw = hex(int(binary, 2))[2:].upper()
    return hexRaw

def hexToBin (hex):
    binRaw = bin(int(hex, 16))[2:].zfill(8)
    return binRaw
    


# ===============================================================

packet = hexToBin(src)

vers = int(packet[0:3], 2)
id = int(packet[3:6], 2)

print(vers)