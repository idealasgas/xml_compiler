# Generated from D:/Документы/универ/ЯПИС/xml-compiler\xml_compiler.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .xml_compilerParser import xml_compilerParser
else:
    from xml_compilerParser import xml_compilerParser

# This class defines a complete listener for a parse tree produced by xml_compilerParser.
class xml_compilerListener(ParseTreeListener):

    # Enter a parse tree produced by xml_compilerParser#prog.
    def enterProg(self, ctx:xml_compilerParser.ProgContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#prog.
    def exitProg(self, ctx:xml_compilerParser.ProgContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#tag_assignment.
    def enterTag_assignment(self, ctx:xml_compilerParser.Tag_assignmentContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#tag_assignment.
    def exitTag_assignment(self, ctx:xml_compilerParser.Tag_assignmentContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#attr_assignment.
    def enterAttr_assignment(self, ctx:xml_compilerParser.Attr_assignmentContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#attr_assignment.
    def exitAttr_assignment(self, ctx:xml_compilerParser.Attr_assignmentContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#gen_file.
    def enterGen_file(self, ctx:xml_compilerParser.Gen_fileContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#gen_file.
    def exitGen_file(self, ctx:xml_compilerParser.Gen_fileContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#parse_file.
    def enterParse_file(self, ctx:xml_compilerParser.Parse_fileContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#parse_file.
    def exitParse_file(self, ctx:xml_compilerParser.Parse_fileContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#add_text.
    def enterAdd_text(self, ctx:xml_compilerParser.Add_textContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#add_text.
    def exitAdd_text(self, ctx:xml_compilerParser.Add_textContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#append_tag.
    def enterAppend_tag(self, ctx:xml_compilerParser.Append_tagContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#append_tag.
    def exitAppend_tag(self, ctx:xml_compilerParser.Append_tagContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#append_atr.
    def enterAppend_atr(self, ctx:xml_compilerParser.Append_atrContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#append_atr.
    def exitAppend_atr(self, ctx:xml_compilerParser.Append_atrContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#remove_tag.
    def enterRemove_tag(self, ctx:xml_compilerParser.Remove_tagContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#remove_tag.
    def exitRemove_tag(self, ctx:xml_compilerParser.Remove_tagContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#remove_atr.
    def enterRemove_atr(self, ctx:xml_compilerParser.Remove_atrContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#remove_atr.
    def exitRemove_atr(self, ctx:xml_compilerParser.Remove_atrContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#declare_array.
    def enterDeclare_array(self, ctx:xml_compilerParser.Declare_arrayContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#declare_array.
    def exitDeclare_array(self, ctx:xml_compilerParser.Declare_arrayContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#search_tag.
    def enterSearch_tag(self, ctx:xml_compilerParser.Search_tagContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#search_tag.
    def exitSearch_tag(self, ctx:xml_compilerParser.Search_tagContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#for_cycle.
    def enterFor_cycle(self, ctx:xml_compilerParser.For_cycleContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#for_cycle.
    def exitFor_cycle(self, ctx:xml_compilerParser.For_cycleContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#function_declaration.
    def enterFunction_declaration(self, ctx:xml_compilerParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#function_declaration.
    def exitFunction_declaration(self, ctx:xml_compilerParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#function_call.
    def enterFunction_call(self, ctx:xml_compilerParser.Function_callContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#function_call.
    def exitFunction_call(self, ctx:xml_compilerParser.Function_callContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#if_declaration.
    def enterIf_declaration(self, ctx:xml_compilerParser.If_declarationContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#if_declaration.
    def exitIf_declaration(self, ctx:xml_compilerParser.If_declarationContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#assign_new_value.
    def enterAssign_new_value(self, ctx:xml_compilerParser.Assign_new_valueContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#assign_new_value.
    def exitAssign_new_value(self, ctx:xml_compilerParser.Assign_new_valueContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#comment_fun.
    def enterComment_fun(self, ctx:xml_compilerParser.Comment_funContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#comment_fun.
    def exitComment_fun(self, ctx:xml_compilerParser.Comment_funContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#print.
    def enterPrint(self, ctx:xml_compilerParser.PrintContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#print.
    def exitPrint(self, ctx:xml_compilerParser.PrintContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#access_name.
    def enterAccess_name(self, ctx:xml_compilerParser.Access_nameContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#access_name.
    def exitAccess_name(self, ctx:xml_compilerParser.Access_nameContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#access_text.
    def enterAccess_text(self, ctx:xml_compilerParser.Access_textContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#access_text.
    def exitAccess_text(self, ctx:xml_compilerParser.Access_textContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#access_value.
    def enterAccess_value(self, ctx:xml_compilerParser.Access_valueContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#access_value.
    def exitAccess_value(self, ctx:xml_compilerParser.Access_valueContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#print_statement.
    def enterPrint_statement(self, ctx:xml_compilerParser.Print_statementContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#print_statement.
    def exitPrint_statement(self, ctx:xml_compilerParser.Print_statementContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#begin_for.
    def enterBegin_for(self, ctx:xml_compilerParser.Begin_forContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#begin_for.
    def exitBegin_for(self, ctx:xml_compilerParser.Begin_forContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#end.
    def enterEnd(self, ctx:xml_compilerParser.EndContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#end.
    def exitEnd(self, ctx:xml_compilerParser.EndContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#datatype.
    def enterDatatype(self, ctx:xml_compilerParser.DatatypeContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#datatype.
    def exitDatatype(self, ctx:xml_compilerParser.DatatypeContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#begin_function.
    def enterBegin_function(self, ctx:xml_compilerParser.Begin_functionContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#begin_function.
    def exitBegin_function(self, ctx:xml_compilerParser.Begin_functionContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#begin_if.
    def enterBegin_if(self, ctx:xml_compilerParser.Begin_ifContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#begin_if.
    def exitBegin_if(self, ctx:xml_compilerParser.Begin_ifContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#comparison.
    def enterComparison(self, ctx:xml_compilerParser.ComparisonContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#comparison.
    def exitComparison(self, ctx:xml_compilerParser.ComparisonContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#else_thing.
    def enterElse_thing(self, ctx:xml_compilerParser.Else_thingContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#else_thing.
    def exitElse_thing(self, ctx:xml_compilerParser.Else_thingContext):
        pass


    # Enter a parse tree produced by xml_compilerParser#comment.
    def enterComment(self, ctx:xml_compilerParser.CommentContext):
        pass

    # Exit a parse tree produced by xml_compilerParser#comment.
    def exitComment(self, ctx:xml_compilerParser.CommentContext):
        pass



del xml_compilerParser