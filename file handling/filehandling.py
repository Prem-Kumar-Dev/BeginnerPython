f=open("D:/VSCODE/PythonOld/file handling/read.txt","a")
f.write("Hello World")
f=f.encode()
f=open("D:/VSCODE/PythonOld/file handling/read.txt","r")
print(f.read())