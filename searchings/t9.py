# preprocess word list with hash table
def t9_hashtable(words, code):
    map = build_map(words)
    return map[code]

def build_map(words):
    map = {}
    table = coding_table()
    for word in words:
        c = encode(word, table)
        if c not in map:
            map[c] = []
        map[c].append(word)
    return map

def coding_table():
    table = {}
    code = ord('a')
    for i in range(2, 10):
        table[code] = str(i)
        table[code + 1] = str(i)
        table[code + 2] = str(i)
        code += 3
        if i == 7 or i == 9:
            table[code] = str(i)
            code += 1
    return table

def encode(word, table):
    codes = []
    for c in word.lower():
        codes.append(table[ord(c)])
    return ''.join(codes)

# preprocess word list with trie
def t9_trie(words, code):
    trie = T9Trie(words)
    return trie.search(code)

class T9Trie:
    def __init__(self, words):
        self.root = T9Node()
        self.encoder = self.coding_table()
        self.build(words)

    def coding_table(self):
        table = {}
        code = ord('a')
        for i in range(2, 10):
            table[code] = i
            table[code + 1] = i
            table[code + 2] = i
            code += 3
            if i == 7 or i == 9:
                table[code] = i
                code += 1
        return table

    def build(self, words):
        for word in words:
            self.add(word.lower())

    def add(self, word):
        self._add(self.root, word, 0)

    def _add(self, node, word, d):
        if node is None:
            node = T9Node()
        if d == len(word):
            node.words.append(word)
            return node
        c = self.encoder[ord(word[d])]
        node.next[c] = self._add(node.next[c], word, d + 1)
        return node
        
    def search(self, code):
        return self._search(self.root, code, 0)

    def _search(self, node, code, d):
        if node is None:
            return None
        if d == len(code):
            return node.words
        c = int(code[d])
        return self._search(node.next[c], code, d + 1)

class T9Node:
    def __init__(self):
        self.words = []
        self.next = [None] * 10

# one time process
# time: O(4^n), where n is length of code 
def t9_once_hashset(words, code):
    wordset = set(map(str.lower, words))
    decoder = decoding_table()
    results = []
    _t9(code, decoder, 0, [], results, wordset)
    return results

def _t9(code, decoder, index, prefix, results, wordset):
    if index == len(code):
        candidate = ''.join(prefix)
        if candidate in wordset:
            results.append(candidate)
        return
    for char in decoder[int(code[index])]:
        prefix.append(char)
        _t9(code, decoder, index + 1, prefix, results, wordset)
        prefix.pop()

def decoding_table():
    decoder = [[] for _ in range(10)]
    code = ord('a')
    for i in range(2, 10):
        decoder[i].append(chr(code))
        decoder[i].append(chr(code + 1))
        decoder[i].append(chr(code + 2))
        code += 3
        if i == 7 or i == 9:
            decoder[i].append(chr(code))
            code += 1
    return decoder

# one time process
def t9_once_trie(words, code):
    trie = WordTrie(words)
    return trie.search(code)

class WordTrie:
    def __init__(self, words):
        self.root = CharNode()
        self.decoder = self.decoding_table()
        self.build(words)

    def decoding_table(self):
        table = [[] for _ in range(10)]
        code = ord('a')
        for i in range(2, 10):
            table[i].append(chr(code))
            table[i].append(chr(code + 1))
            table[i].append(chr(code + 2))
            code += 3
            if i == 7 or i == 9:
                table[i].append(chr(code))
                code += 1
        return table

    def build(self, words):
        for word in words:
            self.add(word.lower())

    def add(self, word):
        self._add(self.root, word, 0)

    def _add(self, node, word, d):
        if node is None:
            node = CharNode()
        if d == len(word):
            node.word = word
            return node
        c = ord(word[d]) - ord('a')
        node.next[c] = self._add(node.next[c], word, d + 1)
        return node

    def search(self, code):
        results = []
        self._search(self.root, code, 0, results)
        return results

    def _search(self, node, code, index, results):
        if node is None:
            return
        if index == len(code):
            if node.word is not None:
                results.append(node.word)
            return
        # map from digit to letters
        letters = self.decoder[int(code[index])]
        if letters:
            for letter in letters:
                c = ord(letter) - ord('a')
                self._search(node.next[c], code, index + 1, results)


class CharNode:
    def __init__(self):
        self.word = None
        self.next = [None] * 26

def load_words(path):
    words = []
    with open(path) as f:
        for line in f:
            words.append(line.rstrip('\n').lower())
    return words

words = load_words('data/words.txt')
print(t9_hashtable(words, '8733'))
print(t9_trie(words, '8733'))
print(t9_once_hashset(words, '8733'))
print(t9_once_trie(words, '8733'))
