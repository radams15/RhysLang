from lexer import Lexer
import pickle

protocol = 0 # 4 highest

class Compiler:
    def __init__(self):
        self.lexer = Lexer().get_lexer()
        self.program_code = None
        self.tokens = None

    def open_code(self, file):
        with open(file, "r") as f:
            self.program_code = f.read()

    def open_tokens(self, file):
        with open(file, "rb") as f:
            self.tokens = pickle.loads(f.read())

    def tokenise(self):
        self.tokens = self.lexer.lex(self.program_code)

    def get_tokens(self):
        if not self.tokens:
            self.tokenise()
        return self.tokens

    def save_tokens(self, to_file):
        pickled = pickle.dumps(self.get_tokens(), protocol=protocol)
        with open(to_file, "wb") as f:
            f.write(pickled)
