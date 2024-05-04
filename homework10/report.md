# Homework 10
## Design
After initially using the starter code given to us to begin interacting with the pizza ELF, I caused the program to seg fault with an overly large input and built the `print_stack` 
function which, after the program has faulted, looks at the addresses surrounding the stack pointer to find my input -- in this case, a series of 0s, or 0x30 -- and the shellcode
which preceded it. After finding the right size of buffer for the program, I used the relative address for `main` to see if I could get the program to, instead of returning to the 
previous stack frame, start the program over again. When I was able to successfully re-start the program, I set about trying to find the correct offset for the beginning of my shellcode.

## Code Explanation
My program uses the `pwntools` Python extension to execute a buffer overflow attack on the `pizza` program. First, it enters the program, sending normal responses for the first two 
prompts, and then send instructions for opening a shell, followed by a buffer made of `0`s that pads the input until the instruction pointer register, where it adds the address for 
the beginning of the shellcode. 
