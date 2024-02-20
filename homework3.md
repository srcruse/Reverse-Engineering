# Homework 3
## Assembly Review
1. Machine code is the binary representation of instructions ready for a machine to execute, and is not human-readable. Assembly is a low-level programming language that can be translated into machine code much more 
easily than a higher-level language, but is readable/writable by humans.
2. Because of the `pushq` instruction, a quadword (8 bytes, or 64 bits) is pushed onto the stack. Thus, the value pointed to by RSP will be decremented by that amount, and the new value will be memory address `0x0000000000127064`.
3. A stack frame "is a section of the stack dedicated to a particular function call," per [NordVPN](https://nordvpn.com/cybersecurity/glossary/stack-frame/). 
Beyond space allocated for use by the function like local variables, the stack frame will also contain information like where to go in memory to return to the calling function, and registers which need to be restored at that time.
4. The data segment will contain both global and static variables.
5. The heap is used for dynamically allocated memory.
6. The code segment, also known as the text segment, will contain the executable instructions.
7. The 'inc' instruction takes one operand, the name of either a register or a memory location, and increments (adds one to) the value it holds.
8. After a `div` instruction, the remainder is placed in the `rdx` register.
9. `jz`, short for "jump if zero", will jump to the specified location if the zero flag is set.
10. The `jne` instruction, or "jump if not equal" will jump if the zero flag is not set.
11. The `mov` instruction takes two arguments and, in AT&T syntax, moves the contents of the first argument into the second. 
12. The `TF` flag is a bit inside the `EFLAGS` register which represents the trap flag; if it is set, it will raise an exception after the next instruction.
13. If an attacker gains control of the `RIP` register, they could redirect the instruction pointer to execute the instruction at any memory location of their choosing.
14. `ax` is the accumulator register, and it sees use in arithmetic operations. It is the lower 16 bits of the `rax` register.
15. `xor rax, rax` will execute the "exclusive or" instruction on the contents of the `rax` register, and then store the result in `rax` -- that is to say, it will set the contents of the register to 0, as anything exclusive or against itself will be 0.
16. The `leave` instruction tears down the stack frame for the current function in preparation for leaving the current function. It  reverses the function prologue by moving the current value of the base pointer into the stack pointer, and then popping into the base pointer. 
17. `retn`, or "return near" is equivalent to `pop rip`.
18. Stack overflow describes when the stack pointer exceeds the space allocated for the stack. Stack overflow can be caused by overly large stack variables and excessive recursion, among other causes.
19. Segmentation faults occur when a program attempts to access memory outside of what is allowed. Causes can include attempting to write to read-only memory, or accessing an array beyond what has been allocated for it (depending on certain factors, this may not always cause a segfault).
20. The `RSI` register is named such because it contains the Source Index register, while the DI in `RDI` stands for Destination Index. These represent pointers to the source and destination, respectively, in stream operations.

## Crackme
#### File open in IDA:
![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/hw3_ida.png)
#### File open in Ghidra:
![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/hw3_ghidra.png)

Solving this crackme was as simple as visiting the function `validate_key`, which takes one parameter, and then returns a boolean reflecting whether that parameter is a multiple of 1223 with the line: `return param_1 % 1223 == 0;`

Because I already knew that the `main` function's purpose was to gather user input and then pass that input as a parameter to the `validate_key` function and then either pass or fail depending on the value of the boolean, 
I knew that the solution would be to pass in a number that was a multiple of 1223. 
![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/hw3_crackme.png)

I found Ghidra significantly easier to use than IDA; my experience is likely biased because we reviewed the use of Ghidra in class, but I feel I would have had an easier time using Ghidra even if I was left to my own devices
on both programs. 
