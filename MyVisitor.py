from lxml import etree
from xml_compilerVisitor import xml_compilerVisitor
from xml_compilerParser import xml_compilerParser

class MyVisitor(xml_compilerVisitor):
    def __init__(self):
        self.memory = {}
        self.file = open("file.py", "w+")
        self.file.write("from lxml import etree\n")

    # root = etree.Element('root')
    def visitTag_assignment(self, ctx):
        value = etree.Element(str(ctx.ID()[1]))
        self.memory[str(ctx.ID()[0])] = value
        self.file.write("{} = etree.Element('{}')\n".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    def visitAttr_assignment(self, ctx):
        value = {}
        value[str(ctx.ID()[1])] = str(ctx.ID()[2])
        self.memory[str(ctx.ID()[0])] = value

    # root.set("hello", "Huhu")
    def visitAppend_atr(self, ctx):
        # tag = self.memory[str(ctx.ID()[0])]
        attribute = self.memory[str(ctx.ID()[1])]
        # tag.set(list(attribute.keys())[0], list(attribute.values())[0])
        self.file.write("{}.set(\"{}\", \"{}\")\n".format(str(ctx.ID()[0]), list(attribute.keys())[0], list(attribute.values())[0]))

    # child.text = 'some text'
    def visitAdd_text(self, ctx):
        # tag = self.memory[str(ctx.ID()[0])]
        # tag.text = str(ctx.ID()[1])
        self.file.write("{}.text = '{}'\n".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    # root.append(child)
    def visitAppend_tag(self, ctx):
        # parent = self.memory[str(ctx.ID()[0])]
        # child = self.memory[str(ctx.ID()[1])]
        # parent.append(child)
        self.file.write("{}.append({})\n".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    def visitGen_file(self, ctx):
        # filename = str(ctx.ID()[1]) + ".xml"
        # root = self.memory[str(ctx.ID()[0])]
        # with open(filename, 'wb') as doc:
        #     doc.write(etree.tostring(root, pretty_print = True))
        self.file.write("with open(\"{}\", 'wb') as doc:\n    doc.write(etree.tostring({}, pretty_print = True))\n".format(str(ctx.ID()[1]) + ".xml", str(ctx.ID()[0])))

    def visitParse_file(self, ctx):
        filename = str(ctx.FILENAME())
        root = str(ctx.ID())
        self.file.write("tree = etree.parse(\"{}\")\n{} = tree.getroot()\n".format(filename, root))

    def visitDeclare_array(self, ctx):
        array = str(ctx.ID())
        self.file.write("{} = []\n".format(array))

    def visitSearch_tag(self, ctx):
        array = str(ctx.ID()[0])
        root = str(ctx.ID()[1])
        desired = str(ctx.ID()[2])
        self.file.write("{} = {}.findall(\"{}\")".format(array, root, desired))