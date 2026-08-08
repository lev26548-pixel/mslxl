import os

ALPHABET = " еаониртслвкмпдгыьбузчйжшхэюцщфъщёЕАОНИРТСЛВКМПДГЫЬБУЗЧЙЖШХЭЮЦЩФЪЩЁabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?-+=()<>[]{}囗\"'\\/;:%_@*&^$#|`~"
CHAR_TO_BIN = {char: f"{i:07b}" for i, char in enumerate(ALPHABET)}
BIN_TO_CHAR = {f"{i:07b}": char for i, char in enumerate(ALPHABET)}

def compress(text, output_path):
    text_with_stop = text + "囗"
    
    bit_string = "".join(CHAR_TO_BIN.get(char, CHAR_TO_BIN[" "]) for char in text_with_stop)
    padding = (8 - (len(bit_string) % 8)) % 8
    if padding: bit_string += "0" * padding
    byte_list = bytearray(int(bit_string[i:i+8], 2) for i in range(0, len(bit_string), 8))
    with open(output_path, "wb") as f:
        f.write(bytes(byte_list))

def decompress(file_path):
    with open(file_path, "rb") as f:
        bit_string = "".join(f"{b:08b}" for b in f.read())
    decoded_text = ""
    for i in range(0, len(bit_string), 7):
        chunk = bit_string[i:i+7]
        if len(chunk) < 7: break
        if chunk in BIN_TO_CHAR:
            char = BIN_TO_CHAR[chunk]
            if char == "囗": 
                break
            decoded_text += char
    return decoded_text
    
