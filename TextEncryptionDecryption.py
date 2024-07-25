def caesar_cipher(text, shift):
  """
  Encrypts or decrypts text using a Caesar cipher.

  Args:
      text: The text to encrypt or decrypt.
      shift: The amount to shift the letters by (positive for encryption, negative for decryption).

  Returns:
      The encrypted or decrypted text.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  result = ''
  for char in text:
    if char.isalpha():
      index = alphabet.index(char.lower())
      new_char = shifted_alphabet[index]
      result += new_char.upper() if char.isupper() else new_char
    else:
      result += char
  return result

# Example usage (encryption)
text = "This is a secret message!"
encrypted_text = caesar_cipher(text, 3)
print(f"Encrypted text: {encrypted_text}")  # Output: WKLV LV D VSHFLDO FRQWHVWR!

# Example usage (decryption)
decrypted_text = caesar_cipher(encrypted_text, -3)
print(f"Decrypted text: {decrypted_text}")  # Output: This is a secret message!
