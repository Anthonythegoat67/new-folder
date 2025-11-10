# Encoded messages
message1 = "HWeolrllod!"
message2 = "acebdfg"
message3 = "gnimmargorP nohtyP"

# Decode using string slicing
decoded1 = message1[::2] + message1[1::2]
decoded2 = message2[::2]  # take every 2nd character starting from index 0
decoded3 = message3[::-1]  # reverse the string

# Print results
print("Decoded Message 1:", decoded1)
print("Decoded Message 2:", decoded2)
print("Decoded Message 3:", decoded3)
