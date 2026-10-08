import sys

class Token:
    def __init__(self, value):
        self.value = value

        if value == '+':
            self.name = "PLUS"
        elif value == '-':
            self.name = "MINUS"
        elif value == '*':
            self.name = "MULTIPLY"
        elif value == '/':
            self.name = "DIVIDE"
        elif value == '(':
            self.name = "LEFT_PAREN"
        elif value == ')':
            self.name = "RIGHT_PAREN"
        else:
            try:
                value = int(value)
            except ValueError:
                sys.exit("wrong input, bro")
            else:
                self.name = "NUMBER"             

    def say(self):
        if self.name == "NUMBER":
            print(f"{self.name}({self.value})")
        else:
            print(f"{self.name}")

opertor = ['+', '-', '*', '/', '(' ,')']

def scan(source):
    user_input = source
    input_list = []
    i = 0
    j = 0
    num_flag = 0
        
    while j < len(user_input):
        if user_input[j] == ' ':
            if num_flag == 0:
                j += 1
                i = j 
                continue

        if user_input[j].isdigit():    
            j += 1
            num_flag = 1
            if j < len(user_input):
                continue
        num_flag = 0
        if j < len(user_input) and j > i:
            input_list.append(user_input[i:j])
        elif j == len(user_input):
            input_list.append(user_input[i:])
            break

        if user_input[j] in opertor:
            input_list.append(user_input[j])

        if user_input[j].isdigit() == False and user_input[j] not in opertor and user_input[j] != ' ':
            print(f"{user_input[j]} is invaild char")
            sys.exit("Invaild input")
            
        j += 1
        i = j   

    return input_list

def get_token(input_list):
    token = []
    for e in input_list:
        token.append(Token(e))
    return token

def print_token(tokens):
    for token in tokens:
        token.say()
