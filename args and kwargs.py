def args_ex(*args):
    print(type(args))
    print("Hello", args[0], "your marks is", args[1], "and your phone no is", args[2])

stuts = ['sujit', 50, 7420894778]

# args_ex(*stuts)

def kwargs_ex(**kwargs):
    print(type(kwargs))
    for key, val in kwargs.items():
        print(key, val)



stud_dict = {'sujit': 50, 'aniket': 45, 'omkar': 40, 'ganesh': 40}

# kwargs_ex(**stud_dict)

def args_kwargs_ex(normal_arg, *args, **kwargs):
    print(type(normal_arg))
    print(type(args))
    print(type(kwargs))
    print(normal_arg)
    print(args)
    for key, val in kwargs.items():
        print(key, val)

args_kwargs_ex("normal argument", *stuts, **stud_dict)