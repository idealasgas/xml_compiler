# Main syntax
## Tag Assignment
```
node root("document");
```
This will result in
```xml
<document></document>
```
## Attribute Assignment
```
attr privet("dela", "normalno");
```
After appending attribute privet to any tag will result in
```xml
<document dela="normalno"></document>
```
## Add text to tag
```
node child("child");
child = "fine";
```
Makes XML like this
```xml
<child>fine</child>
```
## Append tag
```
root << child;
```
Appends child to root like this
```xml
<document>
  <child></child>
</document>
```
## Append attribute
```
root < privet;
```
```xml
<document dela="normalno"></document>
```
## Generate XML File
```
generate(root, "filename");
```
This will create filename.xml  with root-node in it.
## Parse XML File
```
parse(root, "filename.xml");
```
This function will parse filename.xml into root node.
## Search for Tag
Firstly we need to declare array like this.
```
array drinks;
```
And then search for any tag like this.
```
drinks = root@drink;
```
In this case we are looking for `<drink>` tags inside root tag.
# Acts Like Real Language Things
## Loop
You can loop through your array like this.
```
for (drink in drinks) {
  drink < temperatureattr;
}
```
## if-else Statements
```
node tag("fruit");
if (tag->name == "fruit") {
    tag->name = "kiwi";
} else {
    tag->name = "ne";
}
```
## Function Declaration and Calls
You can declare your function anywhere in document.
```
node document("document");
function(document);
function(node tag) {
  attr attribute("lol", "kek");
  tag < attribute;
}
```
