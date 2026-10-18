import lexer, ast

while True:
    user_input = input("minlang > ")

    user_list = lexer.scan(user_input)
    tokens = lexer.get_token(user_list)
    lexer.print_token(tokens)
    AST = ast.get_AST(tokens)

    ast.print_node(AST)
    # AST[1].print_tree()
    AST = []