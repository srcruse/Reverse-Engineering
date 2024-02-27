# Homework 4
## Crackme 1
First, I ran FLOSS on the file using the command `floss -n 10 --only static -- easy_crackme_1` to search for static strings of length 10 or more.

![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw4_crackme1.png)

Just above the prompt for the password, you'll notice a line that says `picklecucumberl337`. This seemed like a reasonable password to me, so I ran the crackme and tried it, and the password was correct.

## Crackme 2
For the second crackme, I decided to try the same method as the first; I ran the command `floss -n 10 --only static -- easy_crackme_2` and found a similarly reasonable password in `artificialtree`:

![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw4_crackme2.png)

Entering this password into the crackme worked, so the FLOSS method was once again successful.

## Crackme 3
Analyzing this Crackme using Ghidra, I first noticed two suspicious variables: `FIRST_PASSWORD1` and `FIRST_PASSWORD2`. Investigating the first revealed it to be `strawberry` fairly easily:

![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw4_crackme3-1.png)

but the second password pointed to a memory location. Following that memory location led me to `kiwi`:

![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw4_crackme3-2.png)

Next, the program concatenates a previously-established null variable (labelled `zero` in the screenshot above) and our first password, `strawberry`, storing it in the former. Next, that same `zero` variable is concatenated with the second password, `kiwi`; this creates a full password of `strawberrykiwi`

### All Crackmes Solved
![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw4_crackmes_solved.png)

## Control Flow 1
After iterating through the file using Ghidra, I determined the following rules had to be satisfied:
- the password must be at least 16 characters long
- password[0] = 'A'
- password[1] = '6'
- password[3] = '2'
- password[7] = '%'
- password[15] = '*'
### Keygen
Using the rules discovered, I wrote this Python script to generate a randomized key:
```
import random
import string
import sys

def gen(n):
	return ''.join(random.choices(string.ascii_letters, k=n)
	
key = 'A602' + gen(3) + '%' + gen(7) + '*'
sys.stdout.write(key)
sys.exit(0)
```
Next, I wrote a bash script to call my Python script and then call the control flow executable using the result as an argument:

```
#! /bin/sh
KEY=`python3 cf1.py`
./control_flow_1 $KEY
```


## Control Flow 2
The rules I determined for this were:
- this password must be 16 or more characters long
- password[6] = 'Y'
- password[8] = '#'
- password[10] = 'A'
- password[11] = '*'
- password[13] = '6'

### Keygen
As the key generation rules in this challenge were very similar to the previous one, I re-used my Python and bash scripts with minor changes to produce another key generator:

```
import random
import string
import sys

def gen(n):
	return ''.join(random.choices(string.ascii_letters, k=n)
	
key = gen(6) + 'Y0#0A*06' + gen(2)
sys.stdout.write(key)
sys.exit(0)
```

```
#! /bin/sh
KEY=`python3 cf2.py`
./control_flow_2 $KEY
```

## Control Flow 3
To succeed, a password must meet the following criteria:
- password length must be exactly 16 characters
- the integer value of password[1] + password[3] - password[5] must equal password[6]; this means that either all 4 can be the same value, indices 1 and 5 can be equal while indices 3 and 6 are equal, or any other solution that fits the rule.
- password[6] and password[7], when exclusive or-ed against each other, must be less than 0x3; this means either the same character or only off by one of the last two bits.
- password[10] must be the same as password[12]
- when exclusive or-ing password[8] and password[7], the result must be equal to or greater than 0x4.
- password[8] and password[9] may not match
- when password[12], password[8], and password[9] are exclusive or-ed, the result may not be the same as whether password[10] is less than 0x3. 
