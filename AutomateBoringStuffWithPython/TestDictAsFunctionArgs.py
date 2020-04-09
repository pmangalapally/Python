def func_kwargs(arg1, **kwargs):
   # print('arg1', arg1)
    for k, v in kwargs.items():
        print(k, v)

func_kwargs(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three'})
# arg1 one
# arg2 two
# arg3 three

#func_kwargs(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three', 'arg4': 'four'})
# arg1 one
# arg2 two
# arg3 three
# arg4 four

#func_kwargs(**{'arg1': 'one', 'arg3': 'three'})
# arg1 one
# arg3 three