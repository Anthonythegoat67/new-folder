# Slicing Decoder

# -------------------- a) --------------------
msg_a = "14#9&!!#¨%7¨&%This is Python12!@#%$&¨*(387"
decoded_a = msg_a[14:28]       # or msg_a[14:28:1]
print("Decoded A:", decoded_a)

# -------------------- b) --------------------
msg_b = "!$Y@@o* u%$ #uaarreqee$ raa@m%$a!dz¨zidmn!ag#g!"
decoded_b = msg_b[2::3]        # start at index 2, take every 3rd character
print("Decoded B:", decoded_b)

# -------------------- c) --------------------
msg_c = "3!$2%*@*&(8?ti teg uoy diDlask"
decoded_c = msg_c[26:11:-1]    # or msg_c[-5:-20:-1]
print("Decoded C:", decoded_c)
