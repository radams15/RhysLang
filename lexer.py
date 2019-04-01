from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PUTS', r'puts')
        # Eval
        self.lexer.add('EVAL', r'eval')
        # Parenthesis
        self.lexer.add('(', r'\(')
        self.lexer.add(')', r'\)')
        # Semi Colon
        self.lexer.add(';', r'\;')
        # Operators
        self.lexer.add('+', r'\+')
        self.lexer.add('-', r'\-')
        self.lexer.add('*', r'\*')
        self.lexer.add('/', r'\/')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # String
        self.lexer.add('STRING', r'\".*\"')
        # Functions
        self.lexer.add('{', r'\{')
        self.lexer.add('{', r'\}')
        self.lexer.add('FUNCTION', r'fun')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()