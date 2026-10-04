from pathlib import Path
import json
root=Path(__file__).parent
model=json.loads((root/'model.json').read_text())
payload=json.dumps(model,ensure_ascii=False).replace('<','\\u003c')
(root/'EigenKI.html').write_text((root/'template.html').read_text().replace('__MODEL__',payload))
print('EigenKI.html fertig')
