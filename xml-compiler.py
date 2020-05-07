from antlr4 import *
from xml_compilerLexer import xml_compilerLexer
from xml_compilerParser import xml_compilerParser
from MyVisitor import MyVisitor
from FunctionVisitor import FunctionVisitor
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        input_stream = FileStream(filename)

        lexer = xml_compilerLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = xml_compilerParser(token_stream)
        tree = parser.prog()

        file = open('file.py', 'w+')
        function_visitor = FunctionVisitor(file)
        function_visitor.visit(tree)
        visitor = MyVisitor(file)
        visitor.visit(tree)
        file.close()
    else:
        print('Provide filename')