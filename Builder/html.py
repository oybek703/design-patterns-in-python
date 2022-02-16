text = 'hello'
parts = ['<p>', text, '</p>']
print(''.join(parts))

words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f' <li>{w}</li>')
parts.append('<ul>')
print('\n'.join(parts))