import keyword

key_word= ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

a = input("请输入关键词：")

if a in key_word:
    print("你输入的",a,"是关键词")
else:
    print("你输入的",a,"不是关键词。")
    print("关键词列表如下：\n",key_word)