class DDD:
    def __init__(self):
        self.text = ""

    def add_word(self, word):
        self.text += word

    def get_text(self):
        return self.text

    def save(self):
        return Memento(self.text)
    
    def restore(self, memento):
        self.text = memento.get_saved_text()

    
class Memento:
    def __init__(self, text):
        self._text = text

    def get_saved_text(self):
        return self._text
    
class History:
    def __init__(self):
        self._history = []
    
    def save(self, memento):
        self._history.append(memento)

    def undo(self):
        if self._history:
            return self._history.pop()
        return None
    

ddd = DDD()
history = History()

ddd.add_word("Hello, ")
history.save(ddd.save())

ddd.add_word("world!")
history.save(ddd.save()) 

ddd.add_word("How are you?")
print("Now:", ddd.get_text())

ddd.restore(history.undo())
print("After undo:", ddd.get_text())

ddd.restore(history.undo())
print("After second undo:", ddd.get_text())