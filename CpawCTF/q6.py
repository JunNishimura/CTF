import re

text = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"

def decode_caesar_cipher(t):
    if not re.match('[a-zA-Z]', t):
        return t
    if re.match('[a-z]', t):
        if ord(t) - 3 < ord('a'):
            diff = ord(t) - 3 - ord('a') + 1
            return chr(ord('z') - diff)
        return chr(ord(t) - 3)
    if ord(t) - 3 < ord('A'):
        diff = ord(t) - 3 - ord('A') + 1
        return chr(ord('Z') - diff)
    return chr(ord(t) - 3)

new_text = ""
for t in text:
    new_text += decode_caesar_cipher(t)
print(new_text)
