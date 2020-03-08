from lxml import etree
from xml_compilerVisitor import xml_compilerVisitor
from xml_compilerParser import xml_compilerParser

class MyVisitor(xml_compilerVisitor):
    def __init__(self):
        self.memory = {}
        self.file = '';

    # root = etree.Element('root')
    def visitTag_assignment(self, ctx):
        value = etree.Element(str(ctx.ID()[1]))
        self.memory[str(ctx.ID()[0])] = value
        print("{} = etree.Element('{}')".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    def visitAttr_assignment(self, ctx):
        value = {}
        value[str(ctx.ID()[1])] = str(ctx.ID()[2])
        self.memory[str(ctx.ID()[0])] = value

    # root.set("hello", "Huhu")
    def visitAppend_atr(self, ctx):
        tag = self.memory[str(ctx.ID()[0])]
        attribute = self.memory[str(ctx.ID()[1])]
        tag.set(list(attribute.keys())[0], list(attribute.values())[0])
        print("{}.set(\"{}\", \"{}\")".format(str(ctx.ID()[0]), list(attribute.keys())[0], list(attribute.values())[0]))

    # child.text = 'some text'
    def visitAdd_text(self, ctx):
        tag = self.memory[str(ctx.ID()[0])]
        tag.text = str(ctx.ID()[1])
        print("{}.text = '{}'".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    # root.append(child)
    def visitAppend_tag(self, ctx):
        parent = self.memory[str(ctx.ID()[0])]
        child = self.memory[str(ctx.ID()[1])]
        parent.append(child)
        print("{}.append({})".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    def visitGen_file(self, ctx):
        filename = str(ctx.ID()[1]) + ".xml"
        root = self.memory[str(ctx.ID()[0])]
        with open(filename, 'wb') as doc:
            doc.write(etree.tostring(root, pretty_print = True))
        # print("filename = \"{}\" + \".xml\"\nroot = {}")
