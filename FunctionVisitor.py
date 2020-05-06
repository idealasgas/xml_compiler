from lxml import etree
from xml_compilerVisitor import xml_compilerVisitor
from xml_compilerParser import xml_compilerParser

class FunctionVisitor(xml_compilerVisitor):
    def __init__(self, file):
        self.memory = {}
        self.file = file
        self.file.write("from lxml import etree\n")
        self.indentation_counter = 0
        self.body_of_function = 0

    def visitTag_assignment(self, ctx):
        if self.body_of_function:
            if str(str(ctx.ID())) in self.memory:
                print("Tag {} already exists".format(str(ctx.ID())))
            else:
                self.memory[str(ctx.ID())] = 'tag'
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "{} = etree.Element({})\n".format(str(ctx.ID()), str(ctx.STRING())))

    def visitAttr_assignment(self, ctx):
        if self.body_of_function:
            if str(ctx.ID()) in self.memory:
                print("Variable {} already exists".format(str(ctx.ID())))
            else:
                value = {}
                value[str(ctx.STRING()[0])] = str(ctx.STRING()[1])
                self.memory[str(ctx.ID())] = value

    def visitAppend_atr(self, ctx):
        if self.body_of_function:
            if (str(ctx.ID()[0]) in self.memory) and (str(ctx.ID()[1]) in self.memory):
                attribute = self.memory[str(ctx.ID()[1])]
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "{}.set({}, {})\n".format(str(ctx.ID()[0]), list(attribute.keys())[0], list(attribute.values())[0]))
            else:
                print('Undefined variables {} and/or {}'.format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    def visitAdd_text(self, ctx):
        if self.body_of_function:
            if str(ctx.ID()) in self.memory:
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "{}.text = {}\n".format(str(ctx.ID()), str(ctx.STRING())))
            else:
                print('Undefined variable {}'.format(str(ctx.ID())))

    def visitAppend_tag(self, ctx):
        if self.body_of_function:
            if (str(ctx.ID()[0]) in self.memory) and (str(ctx.ID()[1]) in self.memory):
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "{}.append({})\n".format(str(ctx.ID()[0]), str(ctx.ID()[1])))
            else:
                print('Undefined variables {} and/or {}'.format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    def visitGen_file(self, ctx):
        if self.body_of_function:
            if str(ctx.ID()) in self.memory:
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "with open('{}', 'wb') as doc:\n".format(str(ctx.STRING())[1:-1] + ".xml"))
                self.file.write(indentation + '    ' + "doc.write(etree.tostring({}, pretty_print = True))\n".format(str(ctx.ID())))
            else:
                print('Undefined variable {}'.format(str(ctx.ID())))

    def visitParse_file(self, ctx):
        if self.body_of_function:
            if str(ctx.ID()) in self.memory:
                print('Variable {} already exists'.format(str(ctx.ID())))
            else:
                filename = str(ctx.STRING())
                root = str(ctx.ID())
                self.memory[root] = 'tag'
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "tree = etree.parse({})\n".format(filename))
                self.file.write(indentation + "{} = tree.getroot()\n".format(root))

    def visitDeclare_array(self, ctx):
        if self.body_of_function:
            if str(ctx.ID()) in self.memory:
                print('Variable {} already exists'.format(str(ctx.ID())))
            else:
                self.memory[str(ctx.ID())] = 'array'
                array = str(ctx.ID())
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "{} = []\n".format(array))

    def visitSearch_tag(self, ctx):
        if self.body_of_function:
            if (str(ctx.ID()[0]) in self.memory) and (str(ctx.ID()[1]) in self.memory):
                array = str(ctx.ID()[0])
                root = str(ctx.ID()[1])
                desired = str(ctx.ID()[2])
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "{} = {}.findall(\"{}\")\n".format(array, root, desired))
            else:
                print('Undefined variable {} and/or {}'.format(str(ctx.ID()[0]), str(ctx.ID()[1])))

    def visitFor_cycle(self, ctx):
        if self.body_of_function:
            if ctx.begin_for().ID()[1].getText() in self.memory:
                item = ctx.begin_for().ID()[0].getText()
                self.memory[item] = 'iterator'
                array = ctx.begin_for().ID()[1].getText()
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "for {} in {}:\n".format(item, array))
                self.indentation_counter += 1
                self.visitChildren(ctx)
            else:
                print('Undefined variable {}'.format(ctx.begin_for().ID()[1].getText()))

    def visitEnd(self, ctx):
        if self.body_of_function:
            self.indentation_counter -= 1
            if type(ctx.parentCtx) == xml_compilerParser.Function_declarationContext:
                self.body_of_function = False

    def visitFunction_declaration(self, ctx):
        self.body_of_function = True
        function_name = ctx.begin_function().ID()[0]
        self.memory[function_name] = 'function'
        arguments = map(lambda x: x.getText(), list(ctx.begin_function().ID()))
        arguments = list(arguments)
        for argument in arguments:
            self.memory[argument] = 'function parameter'
        arguments.pop(0)
        arguments_line = ', '.join(arguments)
        self.body_of_function = True
        indentation = "    " * self.indentation_counter
        self.file.write(indentation + "def {}({}):\n".format(function_name, arguments_line))
        self.indentation_counter += 1
        self.visitChildren(ctx)

    def visitFunction_call(self, ctx):
        if self.body_of_function:
            if str(ctx.ID()[0]) in self.memory:
                function_name = str(ctx.ID()[0])
                arguments = map(lambda x: x.getText(), list(ctx.ID()))
                arguments = list(arguments)
                for argument in arguments:
                    if not(argument in self.memory):
                        print('Undefined variable {}'.format(argument))
                arguments.pop(0)
                arguments_line = ', '.join(arguments)
                indentation = "    " * self.indentation_counter
                self.file.write(indentation + "{}({})\n".format(function_name, arguments_line))
            else:
                print('Undefined variable {}'.format(str(ctx.ID()[0])))

    def visitAccess_name(self, ctx):
        if self.body_of_function:
            if ctx.ID().getText() in self.memory:
                tag = ctx.ID().getText()
                self.file.write("{}.tag".format(tag))
            else:
                print('Undefined variable {}'.format(ctx.ID().getText()))

    def visitAccess_text(self, ctx):
        if self.body_of_function:
            if ctx.ID().getText() in self.memory:
                tag = ctx.ID().getText()
                self.file.write("{}.text".format(tag))
            else:
                print('Undefined variable {}'.format(ctx.ID().getText()))

    def visitAssign_new_value(self, ctx):
        if self.body_of_function:
            if not type(ctx.parentCtx) == xml_compilerParser.ComparisonContext:
                indentation = "    " * self.indentation_counter
                self.file.write(indentation)
            self.visitChildren(ctx)
            string = ctx.STRING().getText()

            self.file.write(" = {}\n".format(string))

    def visitBegin_if(self, ctx):
        if self.body_of_function:
            self.file.write("if ")
            self.indentation_counter += 1
            self.visitChildren(ctx)
            self.file.write(":\n")

    def visitComparison(self, ctx):
        if self.body_of_function:
            self.visitChildren(ctx)
            eq = ctx.EQ().getText()
            string = ctx.STRING()
            self.file.write(" {} {}".format(eq, string))

    def visitElse_thing(self, ctx):
        if self.body_of_function:
            indentation = "    " * (self.indentation_counter - 1)
            self.file.write(indentation + "else:\n")
            self.visitChildren(ctx)
