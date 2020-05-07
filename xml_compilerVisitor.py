# Generated from D:/Документы/универ/ЯПИС/xml-compiler\xml_compiler.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .xml_compilerParser import xml_compilerParser
else:
    from xml_compilerParser import xml_compilerParser

# This class defines a complete generic visitor for a parse tree produced by xml_compilerParser.

class xml_compilerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by xml_compilerParser#prog.
    def visitProg(self, ctx:xml_compilerParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#tag_assignment.
    def visitTag_assignment(self, ctx:xml_compilerParser.Tag_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#attr_assignment.
    def visitAttr_assignment(self, ctx:xml_compilerParser.Attr_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#gen_file.
    def visitGen_file(self, ctx:xml_compilerParser.Gen_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#parse_file.
    def visitParse_file(self, ctx:xml_compilerParser.Parse_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#add_text.
    def visitAdd_text(self, ctx:xml_compilerParser.Add_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#append_tag.
    def visitAppend_tag(self, ctx:xml_compilerParser.Append_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#append_atr.
    def visitAppend_atr(self, ctx:xml_compilerParser.Append_atrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#remove_tag.
    def visitRemove_tag(self, ctx:xml_compilerParser.Remove_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#remove_atr.
    def visitRemove_atr(self, ctx:xml_compilerParser.Remove_atrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#declare_array.
    def visitDeclare_array(self, ctx:xml_compilerParser.Declare_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#search_tag.
    def visitSearch_tag(self, ctx:xml_compilerParser.Search_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#for_cycle.
    def visitFor_cycle(self, ctx:xml_compilerParser.For_cycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#function_declaration.
    def visitFunction_declaration(self, ctx:xml_compilerParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#function_call.
    def visitFunction_call(self, ctx:xml_compilerParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#if_declaration.
    def visitIf_declaration(self, ctx:xml_compilerParser.If_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#assign_new_value.
    def visitAssign_new_value(self, ctx:xml_compilerParser.Assign_new_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#comment_fun.
    def visitComment_fun(self, ctx:xml_compilerParser.Comment_funContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#print.
    def visitPrint(self, ctx:xml_compilerParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#access_name.
    def visitAccess_name(self, ctx:xml_compilerParser.Access_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#access_text.
    def visitAccess_text(self, ctx:xml_compilerParser.Access_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#access_value.
    def visitAccess_value(self, ctx:xml_compilerParser.Access_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#print_statement.
    def visitPrint_statement(self, ctx:xml_compilerParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#begin_for.
    def visitBegin_for(self, ctx:xml_compilerParser.Begin_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#end.
    def visitEnd(self, ctx:xml_compilerParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#datatype.
    def visitDatatype(self, ctx:xml_compilerParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#begin_function.
    def visitBegin_function(self, ctx:xml_compilerParser.Begin_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#begin_if.
    def visitBegin_if(self, ctx:xml_compilerParser.Begin_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#comparison.
    def visitComparison(self, ctx:xml_compilerParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#else_thing.
    def visitElse_thing(self, ctx:xml_compilerParser.Else_thingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by xml_compilerParser#comment.
    def visitComment(self, ctx:xml_compilerParser.CommentContext):
        return self.visitChildren(ctx)



del xml_compilerParser