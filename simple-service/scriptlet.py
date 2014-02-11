#"import math\ndef fib(n):\n\tif n == 1:\n\t\treturn 1" +
#"\n\tif n==0:\n\t\treturn 0\n\telse:\n\t\treturn fib(n-1)" +
#" + fib(n-2)\n\ndef execute(dict):\n\tprint fib(dict[\"nested\"][\"k\"])\nprint math.sin(30)";
import math


def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


def execute(dict):
    print fib(dict["nested"]["k"])
    print math.sin(30)
