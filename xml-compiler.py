from antlr4 import *
from xml_compilerLexer import xml_compilerLexer
from xml_compilerParser import xml_compilerParser
from MyVisitor import MyVisitor
from FunctionVisitor import FunctionVisitor

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    input_stream = FileStream('example6.expr')
    # else:
    # input_stream = InputStream(sys.stdin.readline())

    lexer = xml_compilerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = xml_compilerParser(token_stream)
    tree = parser.prog()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)
    file = open('file.py', 'w+')
    function_visitor = FunctionVisitor(file)
    function_visitor.visit(tree)
    visitor = MyVisitor(file)
    visitor.visit(tree)
    file.close()