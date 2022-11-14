# Cipher System

This project is a continuation of my "Caesar Cipher UI" project.

When I finished my first Caesar Cipher code, I realized how unuseful the deciphering function can be. It is true that it is really interesting how it works, but, what if you dont know the fixed number?

Caesar's cipher uses a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet. A Caesar cipher with a shift of 1 would encode an A as a B, an M as an N, and a Z as an A, and so on.

The best idea that came to my mind was to shift each word through every number (this code is limited to 27 as it is an example and it can be modificable) and compare the result of the shifting with an English dictionary. 

To reduce the memory usage, I divided the original txt file containing the English dictionary by word length, so it takes into account the original word's length. Therefore, if "hello" has 5 letters, it will be compared with the words 5 letters long in the dictionary.

This deciphering/ciphering technique, is entirely based in the position of the letters in the ASCII alphabet. Due to this, words as "hi" or "no" can be found as the same (the letters are next to each other in the alphabet). When the code finds a match, it will be added to the "possiblewords" list. In case there are more than one matches, a dropdown list will be displayed for the user to choose the word that "fits" the most in the sentence.

After ciphering a string, the result will be automatically copied into the clipboard.

This code is optimized for an 58110 English dictionary. When ciphering, every character not included in the ASCII alphabet, will stay the same. It also takes into account wether letters and capitalized or not.

I made the UI with tkinter.