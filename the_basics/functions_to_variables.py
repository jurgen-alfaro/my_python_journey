def hello():
    print("Hello")
    
print(hello) # <function hello at 0x000001A198F504A0>
hi = hello
print(hi) # <function hello at 0x000001A198F504A0>
hello()
hi()

say = print
say("Whoa! I can't believe this works! :O")