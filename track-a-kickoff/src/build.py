import json, sys
D = sys.argv[1]; out = sys.argv[2]; log = sys.argv[3] if len(sys.argv) > 3 else ''
data = json.load(open(D + '/slides.json', encoding='utf-8'))
shell = open(D + '/shell.html', encoding='utf-8').read()
wrap = lambda arr: ''.join(f'<div class="frame">{s}</div>' for s in arr)
logh = open(log, encoding='utf-8').read() if log else ''
open(out, 'w', encoding='utf-8').write(
    shell.replace('{{STUDY}}', wrap(data['study'])).replace('{{BRIEF}}', wrap(data['brief'])).replace('{{BRIEF2}}', wrap(data.get('brief2', []))).replace('{{LOG}}', logh))
print('built', out)
