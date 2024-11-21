import hashlib
rainbow_table = {}
for i in range(1000000):
    bstr = bytes(str(i), "utf-8")
    s = hashlib.md5(bstr).hexdigest()
    rainbow_table[s] = i
s1 = "021bbc7ee20b71134d53e20206bd6feb"
s2 = "e10adc3949ba59abbe56e057f20f883e"
s3 = "655d03ed12927aada3d5bd1f90f06eb7"
print(f"{s1} 对应的明文是：{rainbow_table[s1]}")
print(f"{s2} 对应的明文是：{rainbow_table[s2]}")
print(f"{s3} 对应的明文是：{rainbow_table[s3]}")