# Encryption System

This project is a continuation of my "Caesar Cipher UI" project.

When I finished my first Caesar Cipher code, I realized how unuseful the deciphering function can be. It is true that it is really interesting how it works, but, what if you dont know the fixed number?

Caesar's cipher uses a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet. A Caesar cipher with a shift of 1 would encode an A as a B, an M as an N, and a Z as an A, and so on.

The best idea that came to my mind was to shift each word through every number (this code is limited to 20 as it is an example and it can be modificable) and compare the result of the shifting with an English dictionary of 50.000 words. When the code found a match, it would be added to the "finaltext" string.

I included 2 English dictionaries, the first one with the 1000 most common English words, and the second one with 58110 words.

Apart from encoding messages, the code can also decode messages knowing the fixed number of positions the letters switch.

I made the UI with tkinter.
