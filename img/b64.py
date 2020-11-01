import base64
f = open('75.jpg', 'rb')
ls = base64.b64encode(f.read())
f.close()
with open('75.con', 'w') as fp:
    fp.write(str(ls))
print(ls)