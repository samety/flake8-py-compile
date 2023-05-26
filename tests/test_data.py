CODE_WITH_SYNTAX_ERROR = '''
def boo(x: Any) -> None:
    match x:
        case _:
            pass
        case int() as x:
            print('x=', x)
'''
