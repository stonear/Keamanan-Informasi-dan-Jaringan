from operator import xor

def encrypt(plaintext, key):
    # jika panjang teks dibagi 4 tidak habis (32 bit), ditambah spasi di belakang
    if (len(plaintext) % 4) != 0:
        for i in range(0, 4 - (len(plaintext) % 4)):
            plaintext += " "
    plaintext.split()

    # konversi ke ord
    plaintext = to_ord(plaintext)
    key = to_ord(key)

    # K0 dan K1
    K0 = [None] * 4
    K1 = [None] * 4
    for i in range(0, 4):
        K0[i] = key[i]
        K1[i] = key[i + 4]

    # insialisasi
    chipertext = [None] * len(plaintext)
    count_block = len(plaintext) / 4

    # P XOR K0
    index = 0
    for i in range(0, count_block):
        for j in range(0, 4):
            chipertext[index] = xor(plaintext[index], K0[j])
            index += 1

    # ADD dengan K1 kemudian MOD 256
    index = 0
    for i in range(0, count_block):
        for j in range(0, 4):
            chipertext[index] = chipertext[index] + K1[j]
            chipertext[index] = chipertext[index] % 256
            index += 1

    # ubah dari ord ke chr
    chipertext = to_chr(chipertext)

    return "".join(chipertext)

def decrypt(chipertext, key):
    # konversi ke ord
    chipertext = to_ord(chipertext)
    key = to_ord(key)

    # K0 dan K1
    K0 = [None] * 4
    K1 = [None] * 4
    for i in range(0, 4):
        K0[i] = key[i]
        K1[i] = key[i + 4]

    # insialisasi
    plaintext = [None] * len(chipertext)
    count_block = len(chipertext) / 4

    # C ADD -K1
    index = 0
    for i in range(0, count_block):
        for j in range(0, 4):
            plaintext[index] = chipertext[index] - K1[j]
            index += 1

    # XOR dengan K0
    index = 0
    for i in range(0, count_block):
        for j in range(0, 4):
            plaintext[index] = xor(plaintext[index], K0[j])
            index += 1

    # ubah dari ord ke chr
    plaintext = to_chr(plaintext)

    return "".join(plaintext)

def to_ord(text):
    temp = [None] * len(text)
    for i in range(0, len(text)):
        temp[i] = ord(text[i])
    return temp

def to_chr(text):
    temp = [None] * len(text)
    for i in range(0,len(text)):
        temp[i] = chr(text[i])
    return temp

# buatlah fungsi encrypt dan decrypt dengan menggunakan bahasa python untuk melakukan enkripsi dan dekripsi sesuai dengan soal nomor 1
# gunakan fungsi encrypt dan decrypt tersebut untuk memproteksi string apa saja dengan minimal panjang 500 karakter
# Tunjukkan dalam demo di kelas

key = "keystone"
plaintext = raw_input("Input text: ")

chipertext = encrypt(plaintext, key)
print "chipertext: " + chipertext
print decrypt(chipertext, key)
