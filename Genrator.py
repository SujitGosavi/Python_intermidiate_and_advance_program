def gen(num):
    for n in range(num):
        yield n


gen_obj = gen(500)

for i in range(10):
    print(next(gen_obj))
