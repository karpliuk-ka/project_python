# Project Encryption
 
You can use **Cipher.py** for decoding and encoding files with one of ciphers: *Caesar*, *Vigenere* or *Vernam*. Also you can use auto-decoding of Caesar Cipher based on methods of frequency analysis.
 
# Usage
 
To start program open terminal in folder with "Cipher.py" file. Start program with `./Cipher.py`. To choose working mode use flags: 
1. (NOT NECESSARY) **-n**, **--name** to choose name of cipher that will be used. You can write name in any case, for example ``Vigenere``, ``vigenere`` and ``ViGENerE`` will be considered as ``vigenere``. If you won't write anything will be used *Caesar* with *shift*=0.
    * If you had choose "caesar", enter *cipher shift* with flag **-s** or **--shift**, for example: `./Cipher.py -n Caesar -s 1` 
    * If you had choose "vigenere", enter *code word* with flags **-w** or **--word**, for example: `./Cipher.py -n Vigenere -w word`
    * If you had choose "vernam", if you want to use *code word* enter it with **-w** or **--word** flag, else if you want to use *set of bits*, enter it with **-b** or **--bit** flag, for example: `./Cipher.py -n Vernam -w QWERTYU` or `./Cipher.py -n Vernam -b 10100101`
    * If you want to use auto decoding of Caesar cipher, use `-n auto_caesar`
2. (NOT NECESSARY) **-o <action>**, **--operation <action>** to chose operation with your text: *decoding* or *encoding*. Instead of **<action>** you need to write **decoding** or **encoding**. If you won't write anything will be used **encoding** mode. For example: `./Cipher.py -n Caesar -s 10 -o decoding`
#### ATTENTION! Auto-decoding of Caesar Cipher has only decoding mode.
3. (NOT NECESSARY) **-l <name>**, **-language <name>** to choose language of your text. Instead of **<name>** use **rus** for *russian language* and **eng** for *english* language. If you won't write anything, will be used **english** language. For example: `./Cipher.py -o encoding -l rus`
4. (NECESSARY) **-f <path>**, **--file <path>** to give full address to your text file. You don't need to write "**<**" and "**>**".
5. (NOT NECESSARY) **a <path>**, **--answer <path>** to give full address to file where answer will be written. The existence of the answer-file is not necessary. If you won't write anything will be created file "**answer.txt**".
###
If you want to read this text again use flag **-t** or **--tutorial**
