from parser import Parser
from compiler import Compiler
from time import sleep

compiler = Compiler()

pg = Parser()
pg.parse()
parser = pg.get_parser()

sleep(0.1)

file_name = "test.chev"

if __name__ == '__main__':
    compiler.open_code(file_name)
    compiler.tokenise()

    tokens = compiler.get_tokens()

    #compiler.save_tokens("test.chevc")

    """compiler.open_tokens("test.chevc")

    tokens = compiler.get_tokens()"""

    parser.parse(tokens).eval()