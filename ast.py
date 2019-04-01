from rply.token import BaseBox


class Program(BaseBox):

    def __init__(self, statement):
        self.statements = []
        self.statements.append(statement)
        print(self.statements)

    def add_statement(self, statement):
        self.statements.insert(0, statement)

    def eval(self, env):
        # print "count: %s" % len(self.statements)
        result = None
        for statement in self.statements:
            result = statement.eval(env)
            # print result.to_string()
        return result

    def rep(self):
        result = 'Program('
        for statement in self.statements:
            result += '\n\t' + statement.rep()
        result += '\n)'
        return result

    def get_statements(self):
        return self.statements


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


class String(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value.replace("\"", "")#[1:-1]


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

