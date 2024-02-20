# Homework 1
## Code Block
The assembly instructions for my shellcode (minus the header, function prologue/epilogue for brevity):
```
push %rbp
mov %rsp, %rbp
xor %rax, %rax
push %rax
push $0x68732f2f
push $0x6e69622f
mov %rsp, %rdi
xor %rsi, %rsi
xor %rdx, %rdx
mov $0x3b, %al
syscall
leave
ret
```
My shellcode was 33 bytes long, and the hex representation is:
`55 48 89 e5 48 31 c0 50 68 2f 2f 73 68 68 2f 62 69 6e 48 89 e7 48 31 f6 48 31 d2 b0 3b 0f 05 c9 c3`
## Explanation
First, the `xor` instruction applied to the RAX register against itself zeroes out all the bits in the register.
This value is pushed to the stack, followed by the string "/bin//sh" in reverse-bit order ("hs//" in one instruction, followed by "nib/"). 
Reversing the string accounts for a little-endian system, and pushing RAX before this allows me to have a null-terminated
string when the stack pointer is moved into RDI. RDI denotes the first argument of the execve instruction, and in this case the pathname of the executable to be run.
Next, both the RSI and RDX registers are zeroed out in the same way as RDI -- these represent the next two arguments of execve, which can be pointers to null in this case.
The `mov` instruction to place the value 0x3b into the AL register loads the RAX register with the opcode for execve.
Finally, the `syscall` instruction prompts the operating system to replace the currently-running terminal with /bin//sh.

To avoid having any null bytes in my shellcode, I first opted for using the `xor` instruction to zero out any registers that needed to be cleared. 
Next, to avoid the null byte generated by loading "/bin/sh\0" into the stack, I pushed the empty RAX terminal into the stack before the string, and replaced the null character
with an extra slash, so "/bin//sh" is summoned instead. Finally, instead of addressing RAX as a whole when loading 0x3b to serve as the opcode, I specified the register AL,
which is the least-significant byte of the RAX. Because that register was previously zeroed out, this allowed the correct value to load into the register without the
null bytes which would be generated had I addressed RAX as a whole.