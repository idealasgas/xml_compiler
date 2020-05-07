# XML Compiler
Welcome! I present you world's first compiler from non-existing language into Python written by me.
## Run
```bash
git clone git@github.com:idealasgas/xml_compiler.git
cd xml_compiler
please_compile.bat file
```
`file` is the name of file you want to compile.
## Main syntax
### Tag Assignment
```
node root("document");
```
This will result in
```xml
<document></document>
```
### Attribute Assignment
```
attr privet("dela", "normalno");
```
After appending attribute privet to any tag will result in
```xml
<document dela="normalno"></document>
```
### Add Text to Tag
```
node child("child");
child = "fine";
```
Makes XML like this
```xml
<child>fine</child>
```
### Append Tag
```
root << child;
```
Appends child to root like this
```xml
<document>
  <child></child>
</document>
```
### Append Attribute
```
root < privet;
```
```xml
<document dela="normalno"></document>
```
### Remove Tag
```
node root("document");
array bad;
bad = root@bad;
for (tag in bad) {
  root >> tag;
}
```
Code above will find all `<bad></bad>` tags and remove them from root.
### Remove Attribute
```
root > privet;
```
Removes privet-attribute from root-node.
### Generate XML File
```
generate(root, "filename");
```
This will create filename.xml  with root-node in it.
### Parse XML File
```
parse(root, "filename.xml");
```
This function will parse filename.xml into root node.
### Search for Tag
Firstly we need to declare array like this.
```
array drinks;
```
And then search for any tag like this.
```
drinks = root@drink;
```
In this case we are looking for `<drink>` tags inside root tag.
## Acts Like Real Language Things
### Loop
You can loop through your array like this.
```
for (drink in drinks) {
  drink < temperatureattr;
}
```
### if-else Statements
```
node tag("fruit");
if (tag->name == "fruit") {
    tag->name = "kiwi";
} else {
    tag->name = "ne";
}
```
### Function Declaration and Calls
You can declare your function anywhere in document.
```
node document("document");
function(document);
function(node tag) {
  attr attribute("lol", "kek");
  tag < attribute;
}
```
### Print
Works like this.
```
node document("document");
document = "AaAaAaAaA";
print(document->text);
```
By the way `document->text` reveals content of document tag, `document->name` reveals name of tag.
### Comments
Ruby-style comments like this.
```ruby
# хорошего дня!
```
