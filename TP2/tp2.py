import re

def main():
    file = open('test.md', 'r')
    output = open('output.html', 'w')

    for line in file:
        buffer = line.strip()


        if buffer == "":
            output.write("\n")  # Preserve blank lines in the output
            continue

        size = len(buffer)

        buffer = convert_tags(buffer)

        if size == 0:
            continue

        if buffer[0] == '#':
            print('hash tag')
            buffer = funcHashTag(buffer)
            output.write(buffer + '\n')
        elif buffer.startswith('> '):
            print('block quote')
            buffer = funcBlock(buffer)
            output.write(buffer + '\n')
        elif buffer[0].isdigit() and buffer[1] == '.' and buffer[2] == ' ':
            print('order list')
            buffer = funcOrderedList(buffer)
            output.write(buffer + '\n')
        elif buffer.startswith('- '):
            print('unorder list')
            buffer = funcUnorderedList(buffer)
            output.write(buffer + '\n')
        elif buffer[:3] == "---":
            print('horizontal rule')
            buffer = funcHorizontalRule()
            output.write(buffer + '\n')
        else:
            print('plain text')
            output.write(buffer + '\n')

    file.close()
    output.close()

def funcHashTag(buffer):
    while buffer[0] == '#':
        buffer = buffer[1:]
    return f"<h>{buffer.strip()}</h>"

def funcBlock(buffer):
    buffer = buffer[2:]
    return f"<blockquote>{buffer.strip()}</blockquote>"

def funcOrderedList(buffer):
    return f"<ol><li>{buffer[3:].strip()}</li></ol>"

def funcUnorderedList(buffer):
    return f"<ul><li>{buffer[2:].strip()}</li></ul>"

def funcHorizontalRule():
    return "<hr>"

def convert_tags(text):
    bold_pattern = r'\*\*(.*?)\*\*'
    italic_pattern = r'\*(.*?)\*'
    code_pattern = r'`(.*?)`'
    image_pattern = r'!\[(.*?)\]\((.*?)\)'
    link_pattern = r'\[(.*?)\]\((.*?)\)'

    text = re.sub(bold_pattern, r'<b>\1</b>', text)
    text = re.sub(italic_pattern, r'<i>\1</i>', text)
    text = re.sub(code_pattern, r'<code>\1</code>', text)
    text = re.sub(image_pattern, r'<img src="\2" alt="\1"/>', text)
    text = re.sub(link_pattern, r'<a href="\2">\1</a>', text)

    return text

if __name__ == "__main__":
    main()
