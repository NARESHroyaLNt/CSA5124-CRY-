import hashlib 
str = "GeeksforGeeks"
result = hashlib.md5(str.encode())
print("The hexadecimal equivalent of MD5 is : ") 
print(result.hexdigest())
