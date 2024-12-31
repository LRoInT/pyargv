# PyArgv

PyArgv是一个Python命令行命令解析器, 它可以通过`dict`定义命令行参数和参数的子参数. 并以`dict`的形式返回.

## 使用

首先需要写出你需要解析的参数规则, 例如:

```Python
rules={
    "person":{
        "s":"p", # 短参数
        "l":"person", # 长参数
        "i":True, # 接收输入
        "sub":{
            "age":{
                "s":"a",
                "l":"age",
                "i":True
            },
            "die":{
                "s":"d",
                "l":"die",
                "i":False # 不接收输入
            }
        }
    }
}
```

这定义了一个名为`person`的参数, 它有短参数`-p`和长参数`--person`, 并且会接收输入. 它有一个子参数`age`, 它有有短参数`-a`和长参数`--age`, 会接收输入. 它还有一个子参数`die`, 它有短参数`-d`和长参数`--die`, 不会接收输入.

之后, 你可以创建一个`ArgvParser`对象, 并传入规则, 使其解析命令行参数:

```Python
if __name__ == "__main__":
    parser = pyargv.ArgvParser(rules)

    print(parser.parse(sys.argv[1:]))
```

然后将命令行参数传入并解析

```Shell
python test.py a -p ming -a 18 -d
```

或

```Shell
python test.py a --person ming --age 18 --die
```

以上两种输入得到的结果相同, 为:

```Python
({'nokey': ['a'], 'person': {'nokey': ['ming'], 'age': {'nokey': ['18']}, 'die': True}}, [], False)
```

在这个`tuple`中, 第一个`dict`表示解析得到的参数.

每一个`dict`下的`nokey`键表示不为子参数输入的参数, 如`a`前没有参数名所以`a`在`nokey`键下, 在`person`中, `ming`不为子参数输入所以在`nokey`下.

其它键表示子参数, 在`person`中, `age`和`die`是它的子参数.

对于不接收输入的参数, 当出现时会将它的值设为`True`, 如`die`在`person`中, 所以`die`的值为`True`.
