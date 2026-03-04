import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = ''
    is_tag = False

    for char in html:
        if char == '<':
            is_tag = True

        elif char == '>':
            is_tag = False
            continue

        if not is_tag:
            clean_text += char

    lines = clean_text.splitlines()
    lines_not_empty = []

    for line in lines:
        if line.strip():
            lines_not_empty.append(line)

    clean_text = '\n'.join(lines_not_empty)

    with open(result_file, 'w', encoding='utf-8') as f:
        f.write(clean_text)


delete_html_tags('draft.html')