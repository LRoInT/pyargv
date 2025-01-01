# PyArgv

[中文](./README_cn.md)

PyArgv is a Python command-line parser that defines command-line arguments and parameter subarguments via dict.

## Use

```Python
rules={
    "person":{
        "s":"p", # Short arguments
        "l":"person", # Long argument
        "i":True, # Receive input 
        "sub":{
            "age":{
                "s":"a",
                "l":"age",
                "i":True
            },
            "die":{
                "s":"d",
                "l":"die",
                "i":False # Don't receive input 
            }
        }
    }
}
```

This defines a parameter called person, which has a short parameter `-p` and a long parameter `--person`, and it will take arguments. It has a subparameter `age`, it has a short parameter `-a` and a long parameter `--age`, and it will take arguments. It also has a subparameter `die`, it has a short parameter `-d` and a long parameter `--die`, it won't take arguments.

After that, you can create an ArgvParser object and pass in rules to make it parse command-line arguments:

```Python
if __name__ == "__main__":
    parser = pyargv.ArgvParser(rules)

    print(parser.parse(sys.argv[1:]))
```

Command line arguments are then passed in and parsed

```Shell
python test.py a -p ming -a 18 -d
```

Or

```Shell
python test.py a --person ming --age 18 --die
```

The above two inputs give the same result, which is:

```Python
({'nokey': ['a'], 'person': {'nokey': ['ming'], 'age': {'nokey': ['18']}, 'die': True}}, [], False)
```

In this tuple, the first dict indicates the parsed parameter.

Each `nokey` key under `dict` indicates a parameter that is not entered for a subparameter. For example,`a` does not have aparameter name before it, so `a` is under `nokey` key. In `person`, `ming` is not entered for a subparameter, so it is under`nokey`.

The other keys represent subparameters. In person, age and die are subparameters.
For parameters that do not accept input, the value is set to `True` when present, e.g.`die` in `person`, so `die` has a valueof `True`.
