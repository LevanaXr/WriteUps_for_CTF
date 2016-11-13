## EKOPARTY CTF  PWN25 Ultrababy

* Ok, frankly I admit this problem is quite easy, but there are still many new things in it. As the strat of my binary study, it fits me well.

* Firstly, it is a ELF object, so I run it in Kali. The result is like the fllowing picture.</br>
  Enhen, try more. Then easy to know it is about Stack Smashing.<br>
  So, at the point of transiation range from 23bytes-25bytes, the srack overflows.<br> 
  Now that we have known what it is about, the following path may be much smoother:)
  [picture1]
  
*  Then, I load it to IDA64. Wow, so many functions. <br>
   However, what we really care are only the Main(), Bye(), Flag(), Read().<br>
   Let us see, Flag()[strar at 0X00000000000007f3] is so close to Bye()[strar at 0X00000000000007e0].
   [picture2]
   [picture3]
   
*  Maybe Assembly language is troublesome for many newcomers. So I convert is to ultrababy.c.<br>
   Yes, the C program is easier to understand, let's we start from it. But I will also figure the assembly out, which it is clearer in a long term.<br>
   [picture4]
   
#### Version C
[picture5]

* Then look back Picture1, we will know the buffer is 24bytes【!!why it's not 23 bytes? I will explain later】<br>
  At once the input is over 24bytes, it will overflow to the memory of V_4, which originally stores the start address of Function Bye().<br>
  If we make the overflow accurately to the memory of V_4 and accurately the start address of Function Flag() replace the start address of Function Bye(). WE WILL　SUCCESS!
  
