def encypt_func(txt, s):  
    result = ""  
  
   
    for i in range(len(txt)):  
        char = txt[i]   
  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65) 
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result   
txt = str(input("enter message:")) 
s = int(input("enter key:"))

print("Shift pattern : " + str(s))  
print("encrypted message: " + encypt_func(txt, s))
print("decrypted message : " + txt)
