from antlr4 import *
from xml_compilerLexer import xml_compilerLexer
from xml_compilerParser import xml_compilerParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    input_stream = FileStream('example.expr')
    # else:
    # input_stream = InputStream(sys.stdin.readline())

    lexer = xml_compilerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = xml_compilerParser(token_stream)
    tree = parser.prog()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    visitor = MyVisitor()
    visitor.visit(tree)