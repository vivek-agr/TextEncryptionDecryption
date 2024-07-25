Caesar Cipher is a simple but useful encryption technique that shifts each letter in the plaintext by a certain number of positions down the alphabet. For example, with a shift of 3, "A" would become "D", "B" would become "E", and so on.



How it works:

Define a function caesar_cipher that takes two arguments: text (the text to encrypt or decrypt) and shift (the amount to shift the letters).
Create an alphabet string containing all lowercase letters.
Create a shifted alphabet string by shifting the original alphabet by the specified amount. For example, with a shift of 3, the shifted alphabet would be "defghijklmnopqrstuvwxyzabc".
Initialize an empty result string.
Iterate over each character in the text:
If the character is a letter (isalpha()):
Find the index of the lowercase version of the character in the alphabet string.
Use the index to lookup the corresponding character in the shifted alphabet string.
Add the uppercase or lowercase version of the new character to the result string, depending on the case of the original character.
Otherwise, simply add the character to the result string.
Return the result string.
The example usage shows how to encrypt the text "This is a secret message!" with a shift of 3 and then decrypt the encrypted text back to the original message.

This is a basic Caesar Cipher implementation. There are some ways to improve it:

Handle uppercase and lowercase letters more consistently.
Add punctuation support.
Make the shift value a user input.
Implement other Caesar Cipher variations, such as ROT13 (shift of 13).