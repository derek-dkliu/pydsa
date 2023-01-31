class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'{self.name}="{self.value}"'

class Element(Attribute):
    def __init__(self, name, value = ''):
        super().__init__(name, value)
        self.attributes = []
        self.children = []

    def set_text(self, value):
        self.value = value

    def add_attribute(self, name, value):
        self.attributes.append(Attribute(name, value))
        
    def add_child(self, child):
        self.children.append(child)

    def get_attributes(self):
        return self.attributes

    def get_children(self):
        return self.children

    def __str__(self):
        tagname = self.name
        attributes = ''
        if self.attributes:
            attributes = ' ' + ' '.join(map(str, self.attributes))
        content = ''
        if self.children:
            content = '\t' + '\n\t'.join(map(str, self.children))
            if self.value:
                content += '\n\t' + self.value
        else:
            content = self.value
        lines = []
        lines.append(f"<{tagname}{attributes}>")
        lines.append(content)
        lines.append(f"</{tagname}>")
        sep = '\n' if self.children else ''
        return sep.join(lines)

class XmlEncoder:
    code = 1
    END = '0'
    
    @staticmethod
    def encode(element):
        return XmlEncoder.encodeElem(element)

    @staticmethod
    def encodeElem(element):
        sb = []
        sb.append(str(XmlEncoder.code))
        XmlEncoder.code += 1
        attrs = element.get_attributes()
        sb.append(XmlEncoder.encodeAttr(attrs))
        sb.append(XmlEncoder.END)
        for child in element.get_children():
            sb.append(XmlEncoder.encodeElem(child))
        if element.value:
            sb.append(str(element.value))
        sb.append(XmlEncoder.END)
        return ' '.join(sb)

    @staticmethod
    def encodeAttr(attrs):
        sb = []
        for i, attr in enumerate(attrs):
            sb.append(str(XmlEncoder.code + i) + ' ' + str(attr.value))
        XmlEncoder.code += len(attrs)
        return ' '.join(sb)


family = Element('family')
family.add_attribute('lastName', 'Smith')
family.add_attribute('state', 'NSW')
person = Element('person')
person.add_attribute('firstName', 'John')
person.set_text('Some Message')
family.add_child(person)
print(family)

print(XmlEncoder.encode(family))