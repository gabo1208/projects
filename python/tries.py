class TrieNode:
    val = ''
    conections = {}
    isEnd = False

    def __init__(self, val):
        self.val = val
        self.conections = {}


class Trie:
    root = None

    def __init__(self):
        self.root = TrieNode('')

    def addWord(self, s):
        current = self.root
        for c in s:
            if not c in current.conections:
                current.conections[c] = TrieNode(c)
            current = current.conections[c]

        current.isEnd = True

    def findPrefix(self, p):
        current = self.root
        for c in p:
            if not c in current.conections:
                return None
            current = current.conections[c]
        return current

    def findWord(self, w):
        aux = self.findPrefix(w)
        return w and aux and aux.isEnd


t = Trie()
t.addWord('hey')
print(t.findWord('he'))
