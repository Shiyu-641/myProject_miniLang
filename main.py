import lexer

while True:
    user_input = input("minlang > ")

    user_list = lexer.scan(user_input)
    tokens = lexer.get_token(user_list)
    lexer.print_token(tokens)
