grammar xml_compiler;
// @actionName {...}

prog : statement+;

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


statement: TAG SPC ID O_BKT QT ID QT C_BKT SEMICOLON NEWLINE # tag_assignment
          | ATTR SPC ID O_BKT QT ID QT COMMA SPC QT ID QT C_BKT SEMICOLON NEWLINE # attr_assignment
          | GEN O_BKT ID COMMA SPC QT ID QT C_BKT SEMICOLON NEWLINE # gen_file
          | PARSE O_BKT ID COMMA SPC QT FILENAME QT C_BKT SEMICOLON NEWLINE # parse_file
          | ID SPC ASGN SPC QT ID QT SEMICOLON NEWLINE # add_text
          | ID SPC APND_TAG SPC ID SEMICOLON NEWLINE # append_tag
          | ID SPC APND_ATR SPC ID SEMICOLON NEWLINE # append_atr
          | ID SPC RMV_TAG SPC ID SEMICOLON NEWLINE # remove_tag
          | ID SPC RMV_ATR SPC ID SEMICOLON NEWLINE # remove_atr
          | ARRAY SPC ID SEMICOLON NEWLINE # declare_array;

access_info: ID ARROW NAME # access_name
            | ID ARROW TEXT # access_text
            | ID ARROW NODES # access_nodes
            | ID ARROW ATTRS # access_attrs
            | ID DOT NAME # access_name_of_attr
            | ID DOT VALUE # access_value;

print_statement: PRINT O_BKT access_info C_BKT SEMICOLON NEWLINE;

search: ID SPC ASGN ID AT ID SEMICOLON NEWLINE # search_tag;

//  шо делать с зарезервированными словами




