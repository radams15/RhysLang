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
        @self.pg.production('puts : PUTS  expression ;')
        def puts(p):
            print(p)
            return Puts(p[1])

        @self.pg.production('program : expression')
        def program(p):
            return p[0]


        @self.pg.production('eval : EVAL ( expression ) ;')
        def evaluate(p):
            return Eval(p[2])

        @self.pg.production('expression : expression + expression')
        @self.pg.production('expression : expression - expression')
        @self.pg.production('expression : expression * expression')
        @self.pg.production('expression : expression / expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            return Eval(Expression(left, right, operator).eval())

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