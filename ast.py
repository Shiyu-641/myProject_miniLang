class ASTNode:
    def __init__(node, token, left, right):
        node.token = token
        node.left = left
        node.right = right

    def say(self):
        if self.right == None:
            right = None
        else:
            right = self.right.token.value
        if self.left == None:
            left = None
        else:
            left = self.left.token.value

        print(f"{self.token.value}, left: {left}, right: {right}")

    def print_tree(self, level=0, branch="ROOT"):
        print("    " * level + f"{branch}: {self.token.name} ({self.token.value})")

        if self.left is not None:
            self.left.print_tree(level + 1, "LEFT")

        if self.right is not None:
            self.right.print_tree(level + 1, "RIGHT")     

operator0 = ["PLUS", "MINUS"]
operator1 = ["MULTIPLY", "DIVIDE"]
operator_name = ["PLUS", "MINUS", "MULTIPLY", "DIVIDE"]

def get_root(last, now):
    if last.token.name in operator0 and now.token.name in operator1:
        root = last
    elif last.token.name in operator1 and now.token.name in operator0:
        root = now
    elif (last.token.name in operator0 and now.token.name in operator0) or (last.token.name in operator1 and now.token.name in operator1):
        root = now
    return root

def get_numAST(tokens):
    numAST = []
    for token in tokens:
        if token.name == "NUMBER":
            numNode = ASTNode(token, None, None)
            numAST.append(numNode)
    return numAST

def get_AST(tokens):
    root = None
    AST = []
    numAST = get_numAST(tokens)
    last_root = None
    now_root = None
    num_num = 0
    num_operator = 0

    # 创建新节点
    len_token = len(tokens)
    i = 0
    while i < len_token:
        # 每一个新传进来的节点首先都应该创建新节点
        node = ASTNode(tokens[i], None, None)
        
    # 链接新节点
        # 构建最小子树
        
        if tokens[i].name == "NUMBER":
            num_num += 1

        if tokens[i].name in operator_name:
            num_operator += 1
            node.left = numAST[num_num - 1]
            node.right = numAST[num_num]

            if num_operator != 1:
            # 链接根节点
                # 找到新根节点
                now_root = get_root(last_root, node) 
                # 链接
                if now_root == last_root:
                    now_root.right = node
                elif now_root == node:
                    now_root.left = last_root
                #更新节点信息
                last_root = now_root
            else:
                last_root = node

        AST.append(node)
        i += 1

    return AST

def print_node(AST):
    if not AST:
        print("AST is empty")
        return

    # # 暂时假设 AST[1] 是根节点
    # AST[1].print_tree()

    for e in AST:
        e.say()


    