class Symbol:
    def __init__(self, char):
        self.char = char
    
    def display(self, x, y):
        print(f"Symbol '{self.char}' on position ({x}, {y})")

class SymbolFactory:
    _symbols = {}
    
    @classmethod
    def get_symbol(cls, char):
        if char not in cls._symbols:
            cls._symbols[char] = Symbol(char)
        return cls._symbols[char]

symbols_good = []
factory = SymbolFactory

for i in range(5):
    symbol = factory.get_symbol('A')  
    symbols_good.append((symbol, i, 0))

for symbol, x, y in symbols_good:
    symbol.display(x, y)

print(f"Created objects: {len(factory._symbols)}")
