import re

def tokenize(text):
    pattern = re.compile(r'on|off|=|[+\-]?\d+', re.IGNORECASE)
    return [m.group() for m in pattern.finditer(text)]

def main():
    file = open('input.txt', 'r')
    soma = 0
    estado = True
    
    for line in file:
        buffer = line.strip()
        for token in tokenize(buffer):
            if token.lower() == "on":
                estado = True
            elif token.lower() == "off":
                estado = False
            elif token == '=':
                print(soma)
            elif estado:
                soma += int(token)

if __name__ == "__main__":
    main()
