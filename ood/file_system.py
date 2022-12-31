from datetime import datetime

class Entry:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.accessed_at = datetime.now()

    def get_size(self):
        raise NotImplementedError

    def get_full_path(self):
        if self.parent is None: return self.name
        else: return self.parent.get_full_path() + '/' + self.name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def delete(self):
        if self.parent is None: return False
        else: self.parent.remove_entry(self)

    def __str__(self):
        return self.name

class File(Entry):
    def __init__(self, name):
        super().__init__(name)
        self.content = None
        self.size = 0
    
    def get_size(self):
        return self.size

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content
        self.size = len(self.content.encode('utf-8'))

class Directory(Entry):
    def __init__(self, name):
        super().__init__(name)
        self.contents = []      # list of files or directories

    def get_size(self):
        size = 0
        for entry in self.contents:
            size += entry.get_size()
        return size

    def get_number_of_files(self):
        count = 0
        for entry in self.contents:
            if isinstance(entry, Directory):
                count += entry.get_number_of_files()
            count += 1
        return count

    def dir(self, level = 0):
        if level == 0: print('-' * 10)
        contents = []
        for entry in self.contents:
            contents.append('  ' * level + str(entry))
            if isinstance(entry, Directory):
                contents.append(entry.dir(level + 1))
        return '\n'.join(contents)

    @staticmethod
    def dir2(root, level = 0):
        if level == 0: print('-' * 10)
        print('  ' * level + root.name)
        if isinstance(root, File): return 
        for entry in root.contents:
            Directory.dir2(entry, level + 1)

    def add_entry(self, entry):
        old_parent = entry.get_parent()
        if old_parent:
            old_parent.remove_entry(entry)
        entry.set_parent(self)
        self.contents.append(entry)

    def remove_entry(self, entry):
        self.contents.remove(entry)
        entry.set_parent(None)

root = Directory('.')

file1 = File('file 1')
file2 = File('file 2')
derek = Directory('derek')
root.add_entry(derek)
root.add_entry(file1)
root.add_entry(file2)

f1 = File('myfile 1')
f2 = File('myfile 2')
f3 = File('myfile 3')
project = Directory('project')
derek.add_entry(f1)
derek.add_entry(project)
derek.add_entry(f2)
derek.add_entry(f3)

p1 = File('program1')
p2 = File('program2')
project.add_entry(p1)
project.add_entry(p2)

print(file1.get_full_path())
print(derek.get_full_path())
print(f1.get_full_path())
print(project.get_full_path())
print(p1.get_full_path())
print(root.get_number_of_files())

p1.set_content("hello world")
p2.set_content("To be or not to be")
print(p1.get_name(), p1.get_size())
print(p2.get_name(), p2.get_size())
print(project.get_name(), project.get_size())

print(root.dir())

print(p2.get_full_path())
root.add_entry(p2)
print(p2.get_full_path())
print(project.get_name(), project.get_size())

print(root.dir())
Directory.dir2(root)
