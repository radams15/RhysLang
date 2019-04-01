from rply import ParserGenerator
from ast import *


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ["NUMBER",
             "STRING",
             "PUTS",
             "EVAL",
             "FUNCTION",
             "(",
             ")",
             "{",
             "}",
             ";",
             "+",
             "-",
             "*",
             "/",
             ],

            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV'])
            ]
        )

    def parse(self):
        @self.pg.production('puts : PUTS ( expression ) ;')
        def puts(p):
            return Puts(p[2])


        @self.pg.production('program : statement_full')
        def program_statement(p):
            return Program(p[0])

        @self.pg.production('statement_full : statement ;')
        def statement_full(p):
            return p[0]

        @self.pg.production('statement : expression')
        def statement_expr(p):
            return p[0]


        @self.pg.production('eval : EVAL ( expression ) ;')
        def evaluate(p):
            return Eval(p[2])

        @self.pg.production('function : FUNCTION ')
        def function(p):
            return Puts(p[2])

        @self.pg.production('expression : expression + expression')
        @self.pg.production('expression : expression - expression')
        @self.pg.production('expression : expression * expression')
        @self.pg.production('expression : expression / expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            if operator.gettokentype() == "DIV":
                return Div(left, right)
            elif operator.gettokentype() == "MUL":
                return Mul(left, right)
            elif operator.gettokentype() == "SUM":
                return Sum(left, right)
            elif operator.gettokentype() == "SUB":
                return Sub(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('expression : STRING')
        def string(p):
            return String(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()