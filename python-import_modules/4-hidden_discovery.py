import dis
import marshal

def hidden_discovery(filepath):
    with open(filepath, 'rb') as f:
        magic = f.read(4)
        moddate = f.read(4)
        code = marshal.load(f)

    for i in dis.get_instructions(code):
        if i.argrepr.startswith("'") and not i.argrepr.startswith("'_"):
            print(i.argrepr.strip("'"))

if __name__ == '__main__':
    hidden_discovery("hidden_4.pyc")
