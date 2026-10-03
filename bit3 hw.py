secret_code = int(input("Enter the secret code: "))
access_key = int(input("Enter the access key: "))

print("\n--- Binary Values ---")
print("Secret Code :", bin(secret_code))
print("Access Key  :", bin(access_key))

matching_bits = secret_code & access_key
print("\nMatching Bits (AND):", bin(matching_bits))

combined_bits = secret_code | access_key
print("Combined Bits (OR):", bin(combined_bits))

different_bits = secret_code ^ access_key
print("Different Bits (XOR):", bin(different_bits))

flipped_bits = ~secret_code
print("Flipped Secret Code:", flipped_bits)

print("\nLeft Shift Secret Code by 1 :", secret_code << 1)
print("Right Shift Secret Code by 1:", secret_code >> 1)

bit_count = bin(secret_code).count("1")
print("\nNumber of ON bits in Secret Code:", bit_count)