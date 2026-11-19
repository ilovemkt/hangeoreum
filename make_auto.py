# index.html을 고친 뒤 이 파일을 실행하면 자동재생판(auto/index.html)도 똑같이 맞춰져요.
import os
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'index.html'), encoding='utf-8').read()
s = s.replace('<head>', '<head>\n<base href="../">\n<script>window.AUTO_PLAY = true;</script>', 1)
s = s.replace('<title>되어가는 교사의 걸음, 마음, 이음</title>', '<title>되어가는 교사의 걸음, 마음, 이음 (자동)</title>')
os.makedirs(os.path.join(here, 'auto'), exist_ok=True)
open(os.path.join(here, 'auto', 'index.html'), 'w', encoding='utf-8').write(s)
