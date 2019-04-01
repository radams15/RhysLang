from rply.token import BaseBox

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class Eval(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class Expression(BaseBox):
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

        print(left, right, operator)

    def eval(self):
        if self.operator.gettokentype() == "/":
            return Div(self.left, self.right)
        elif self.operator.gettokentype() == "*":
            return Mul(self.left, self.right)
        elif self.operator.gettokentype() == "+":
            return Sum(self.left, self.right)
        elif self.operator.gettokentype() == "-":
            return Sub(self.left, self.right)


class String(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        val = self.value[1:-1]
        return val


class Operation(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class BinaryOp(Operation):
    pass


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Puts(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

