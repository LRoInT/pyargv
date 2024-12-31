import sys
import pyargv

rules = {
    "person": {
        "s": "p",
        "l": "person",
        "i": True,
        "sub": {
            "age": {
                "s": "a",
                "l": "age",
                "i": True
            },
            "die": {
                "s": "d",
                "l": "die",
                "i": False
            }
        }
    }
}

if __name__ == "__main__":
    parser = pyargv.ArgvParser(rules)

    print(parser.parse(sys.argv[1:]))