# logic.py
`logic-program.py` can be run on its own.  
`logic-class` can be implemented into code.  
`logic.py` is a module to be put within the project folder or to be put into the equivalent of:  
`C:\Users\`[user]`\AppData\Local\Programs\Python\Python36-32\Lib`  
  
## how to use  
### using as a module    
Write `import logic` in your code.  
You will be able to use it by itself.  
For example:  
```python
>>> import logic
>>> logic.AND(1, 1)
True
```  
You can also use it as a condition:  
```python
>>> if logic.AND(1, 1):
	print("yah, true")
else:
	print("nah, false")

nah, false
``` 
### what you can do with this  
The module contains the `AND`, `OR`, `NOT`, `NOR`, `NAND`, `XOR` and `XNOR` gates.  
To use it just type:  
`logic.`[gate]`(`[0/1]`, `[0/1]`)`  
  
### other functions are:  
`logic.ver()` - current version  
`logic.help()` - shows how to use the gates  
`logic.license()` - shows the MIT license in use  
  
## future plans
I am planning on uploading it to the PythonPackageIndex (PyPI) so it can be easily installed with `pip install logic.py`
