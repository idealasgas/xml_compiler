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

    def visitAttr_assignment(self, ctx):
        value = {}
        value[str(ctx.ID()[1])] = str(ctx.ID()[2])
        self.memory[str(ctx.ID()[0])] = value

    # root.set("hello", "Huhu")
    def visitAppend_atr(self, ctx):
        tag = self.memory[str(ctx.ID()[0])]
        attribute = self.memory[str(ctx.ID()[1])]
        tag.set(list(attribute.keys())[0], list(attribute.values())[0])
