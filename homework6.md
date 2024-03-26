# Homework 5
## Crackme 1 Solution
To solve this crackme, I opened it in Ghidra and followed the function calls, taking notes of each set of rules I found outlined in each function. I generated a key using the following Python code:
```
import random
import string
import sys

r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

l = '0000'
while ord(l[0]) + ord(l[1]) == ord(l[2]) + ord(l[3]):
    l = ''.join(random.choices(string.ascii_lowercase, k=4))

fir = '0' + l[:2] + '0'
sec = r[:4]
thi = r[3:] + r[0]
fou = '0' + l[2:] + '0'

key = fir + '-' + sec + '-' + thi + '-' + fou

sys.stdout.write(key)
sys.exit(0)

```

and I used the following shell script to execute it:
```
#! /bin/sh

KEY=`python3 keygen.py`
./crackme05_64bit $KEY

```

### How I did it using Ghidra:
1. I opened the crackme 64-bit file using Ghidra.
2. I traversed the `main` function and noticed calls to 4 other functions: `rock`, `paper`, `scissors`, and `cracker`.
3. The first function, `rock`, verifies that the input passed is exactly 19 characters, consists of only uppercase and lowercase letters, digits, and the character '-',
4. and needs to have at least one character be an uppercase letter or a digit. I gathered this because the function traverses through the characters of the input string
5. and will call the function `bomb` if any of them fall below the ASCII value of '-', if they fall between '-' and '0', between the characters 'Z' and 'a', above 'z',
6. or if the key is not 19 characters long. 
7. Next, the `paper` function outlines two pairs of characters that need to have a particular relationship to each other, and four additional characters that must reflect
8. that relationship. Characters at the indices 8 and 10, when XORed against each other, must come to a value between 0 and 9 (inclusive); this XOR value must be represented
9. in the characters at indices 3 and 15. The same relationship is true of characters at indices 5 and 13, and the characters at indices 0 and 18 must reflect that.
10. To solve this in my keygen, I outlined that characters 8 and 10 would always be the same as each other, and that characters 5 and 13 would also be equal to each other.
11. This allowed characters 0, 3, 15, and 18 to be hard coded at '0'.
12. The `scissors` function is called next, and it places restrictions on the character pairs at indices 1 and 2, and indices 16 and 17. When the ASCII values of each pair
13. are added together, they must be larger than 171. While pairings like `A` (65) and `k` (107) are valid, I found the easiest way to fit this rule every time would be to
14. constrain each pair to only contain lowercase letters. Finally, the function checks whether each pair of characters, when added together, do not add up to the same value.
![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw6-cm1-1.png)
15. Finally, `cracker` is called, which checks that there is a hyphen ('-') after every four characters (at indices 4, 9, and 14). I was able to ascertain this because the
16. function checks whether the ASCII value of those three characters was equal to 135. 135 divided  by 3 is 45, the value of the hyphen character. Because nothing with an
17. ASCII value lower than a hyphen is a valid character, this necessitates that these characters must all be exactly hyphens. 


