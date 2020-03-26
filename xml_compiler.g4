grammar xml_compiler;
// @actionName {...}

prog : statement+;

FOR : 'for';
IF : 'if';
IN : 'in';
TAG : 'node';
ATTR : 'attr';
NAME : 'name';
TEXT : 'text';
NODES : 'nodes';
ATTRS : 'attrs';
GEN : 'generate';
PRINT : 'print';
VALUE : 'value';
PARSE : 'parse';
ARRAY : 'array';
AT : '@';
ID : [a-z]+;
FILENAME : [a-zA-Z|~.]+;
STRING : '"' (.)*? '"';
NEWLINE : '\r'? '\n' ;
ASGN : '=';
APND_ATR : '<';
APND_TAG : '<<';
RMV_ATR : '>';
RMV_TAG : '>>';
ROOT : '!';
INT : [0-9]+;
SEMICOLON : ';';
QT : '"';
O_BKT : '(';
C_BKT : ')';
SPC : ' ';
COMMA : ',';
ARROW : '->';
DOT : '.';
CURLY_O_BKT : '{';
CURLY_C_BKT : '}';
HASHTAG : '#';

statement: SPC* TAG SPC ID O_BKT STRING C_BKT SEMICOLON NEWLINE # tag_assignment
          | SPC* ATTR SPC ID O_BKT STRING COMMA SPC STRING C_BKT SEMICOLON NEWLINE # attr_assignment
          | SPC* GEN O_BKT ID COMMA SPC STRING C_BKT SEMICOLON NEWLINE # gen_file
          | SPC* PARSE O_BKT ID COMMA SPC QT FILENAME QT C_BKT SEMICOLON NEWLINE # parse_file
          | SPC* ID SPC ASGN SPC STRING SEMICOLON NEWLINE # add_text
          | SPC* ID SPC APND_TAG SPC ID SEMICOLON NEWLINE # append_tag
          | SPC* ID SPC APND_ATR SPC ID SEMICOLON NEWLINE # append_atr
          | SPC* ID SPC RMV_TAG SPC ID SEMICOLON NEWLINE # remove_tag
          | SPC* ID SPC RMV_ATR SPC ID SEMICOLON NEWLINE # remove_atr
          | SPC* ARRAY SPC ID SEMICOLON NEWLINE # declare_array
          | SPC* ID SPC ASGN SPC ID AT ID SEMICOLON NEWLINE # search_tag
          | begin_for statement+ end # for_cycle
          | begin_function statement+ end # function_declaration
          | ID O_BKT (ID(COMMA SPC ID)*)* C_BKT SEMICOLON NEWLINE # function_call
          | begin_if statement+ end # if_declaration
          | access_info SPC ASGN SPC STRING SEMICOLON NEWLINE # assign_new_value;

access_info: ID ARROW NAME # access_name
            | ID ARROW TEXT # access_text
            | ID ARROW VALUE # access_value;
            //| ID ARROW NODES # access_nodes
            //| ID ARROW ATTRS # access_attrs

print_statement: PRINT O_BKT access_info C_BKT SEMICOLON NEWLINE;

begin_for: SPC* FOR SPC O_BKT ID SPC IN SPC ID C_BKT SPC CURLY_O_BKT NEWLINE;
end: SPC* CURLY_C_BKT NEWLINE;
datatype: TAG | ATTR | ARRAY | 'int';
begin_function: SPC* ID O_BKT (datatype SPC ID (COMMA SPC datatype SPC ID)*)* C_BKT SPC CURLY_O_BKT NEWLINE;
begin_if: IF SPC O_BKT comparison C_BKT SPC CURLY_O_BKT NEWLINE;
comparison: access_info SPC eq=('=='|'!=') SPC STRING;


//  шо делать с зарезервированными словами
// СДЕЛАТЬ КОММЕНТАРИИ
// проверить удаление аттрибутов / тегов
// сделать чтобы можно было просто написать пустую строку
// ошибки