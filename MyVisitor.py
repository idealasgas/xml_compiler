from lxml import etree
from xml_compilerVisitor import xml_compilerVisitor
from xml_compilerParser import xml_compilerParser

class MyVisitor(xml_compilerVisitor):
    def __init__(self):
        self.memory = {}

    # root = etree.Element('root')
    def visitTag_assignment(self, ctx):
        value = etree.Element(str(ctx.ID()[1]))
        self.memory[str(ctx.ID()[0])] = value
