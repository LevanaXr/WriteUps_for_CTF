** EKOPARTY CTF Rev75 RrEeGgEeXx


* 依旧是一个.NET程序，在.NET Reflector中加载，看到两个关键函数，main和check_regex
<br>
![picture1](img/EKOCTF/re/re75/1.png)
<br>
<br>

* 查看main函数，关键信息为if语句
![picture1](img/EKOCTF/re/re75/2.png)
<br>
<br>

* 细看一下if语句，尤其是其中的条件，正则表达式regex

```
if (((check_regex("^.{40}$", input) && check_regex(@"\w{3}\{.*\}", input)) && (check_regex("_s.*e_", input) && check_regex(@"\{o{2}O{2}o{2}", input))) && (check_regex(@"O{2}o{2}O{2}\}", input) && check_regex("sup3r_r3g3x_challenge", input)))
    {
        Console.WriteLine("Welcome master");
    }
```

