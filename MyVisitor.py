from lxml import etree
from xml_compilerVisitor import xml_compilerVisitor
from xml_compilerParser import xml_compilerParser

class MyVisitor(xml_compilerVisitor):
    def __init__(self):
        self.memory = {}
        self.file = open("file.py", "w+")
        self.file.write("from lxml import etree\n")
        self.indentation_counter = 0
        self.body_of_function = False

    # root = etree.Element('root')
    def visitTag_assignment(self, ctx):
        value = etree.Element(str(ctx.ID()[1]))
        self.memory[str(ctx.ID()[0])] = value
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "{} = etree.Element('{}')\n".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    def visitAttr_assignment(self, ctx):
        value = {}
        value[str(ctx.ID()[1])] = str(ctx.ID()[2])
        self.memory[str(ctx.ID()[0])] = value

    # root.set("hello", "Huhu")
    def visitAppend_atr(self, ctx):
        # tag = self.memory[str(ctx.ID()[0])]
        attribute = self.memory[str(ctx.ID()[1])]
        # tag.set(list(attribute.keys())[0], list(attribute.values())[0])
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "{}.set(\"{}\", \"{}\")\n".format(str(ctx.ID()[0]), list(attribute.keys())[0], list(attribute.values())[0]))
        print('опа')

    # child.text = 'some text'
    def visitAdd_text(self, ctx):
        # tag = self.memory[str(ctx.ID()[0])]
        # tag.text = str(ctx.ID()[1])
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "{}.text = '{}'\n".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    # root.append(child)
    def visitAppend_tag(self, ctx):
        # parent = self.memory[str(ctx.ID()[0])]
        # child = self.memory[str(ctx.ID()[1])]
        # parent.append(child)
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "{}.append({})\n".format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    # TODO нужно контролировать количество пробелов во второй строчке
    def visitGen_file(self, ctx):
        # filename = str(ctx.ID()[1]) + ".xml"
        # root = self.memory[str(ctx.ID()[0])]
        # with open(filename, 'wb') as doc:
        #     doc.write(etree.tostring(root, pretty_print = True))
        self.file.write("with open(\"{}\", 'wb') as doc:\n    doc.write(etree.tostring({}, pretty_print = True))\n".format(str(ctx.ID()[1]) + ".xml", str(ctx.ID()[0])))

    def visitParse_file(self, ctx):
        filename = str(ctx.FILENAME())
        root = str(ctx.ID())
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "tree = etree.parse(\"{}\")\n{} = tree.getroot()\n".format(filename, root))

    def visitDeclare_array(self, ctx):
        array = str(ctx.ID())
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "{} = []\n".format(array))

    def visitSearch_tag(self, ctx):
        array = str(ctx.ID()[0])
        root = str(ctx.ID()[1])
        desired = str(ctx.ID()[2])
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "{} = {}.findall(\"{}\")\n".format(array, root, desired))

    def visitFor_cycle(self, ctx):
        item = ctx.begin_for().ID()[0].getText()
        array = ctx.begin_for().ID()[1].getText()
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "for {} in {}:\n".format(item, array))
        self.indentation_counter += 1
        self.visitChildren(ctx)

    def visitEnd(self, ctx):
        self.indentation_counter -= 1
        print(str(self.indentation_counter) + 'end of function')
        # if type(ctx.parentCtx) == xml_compilerParser.Function_declarationContext:
        #     self.body_of_function = False
        #     self.indentation_counter -= 1

    def visitFunction_declaration(self, ctx):
        function_name = ctx.begin_function().ID()[0]
        arguments = map(lambda x: x.getText(), list(ctx.begin_function().ID()))
        arguments = list(arguments)
        arguments.pop(0)
        arguments_line = ', '.join(arguments)
        self.body_of_function = True
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "def {}({}):\n".format(function_name, arguments_line))
        self.indentation_counter += 1
        self.visitChildren(ctx)

    def visitFunction_call(self, ctx):
        function_name = ctx.ID()[0]
        arguments = map(lambda x: x.getText(), list(ctx.ID()))
        arguments = list(arguments)
        arguments.pop(0)
        arguments_line = ', '.join(arguments)
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "{}({})".format(function_name, arguments_line))







        # попробовать getText вместо str()

