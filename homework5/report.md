# Homework 5
## Ransomware 1
This first ransomware decrypts by taking each byte of the encrypted text and performing exclusive or against the character `4`, seen in line 46 below:

![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw5_rw1.png)

My decryption does the same and holds a hex representation of the character `4` to be compared against every character in the input file, then writes the ASCII representation of 
the result into the output file.

## Ransomware 2
This program works similarly to the first; instead of performing the exclusive or against a single character, the input file is broken into 4-character segments and then 
exclusive or-ed against the string '1337', or `leet` in line 60 of the screenshot below.

![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw5_rw2.png)


## Ransomware 3
Similar to the previous program, the file being decrypted is sectioned into 6-character strings before being exclusive or-ed against a key (line 68). However, in this case 
the key needed to be found. 

![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw5_rw3.png)

The location at `key` was empty, while `HIDDEN_KEY` contained the string `S4W4S64`. The function `restore_key` revealed that `HIDDEN_KEY` would have one subtracted from 
each of the characters, leading to `R3V3R53`, and this result was stored in the `key` variable. This was confirmed when running the ransomware and providing the correct 
password, `delicious`.
