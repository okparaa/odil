#!/usr/bin/env python3

import os
text = '''<!--- DO NOT EDIT THIS FILE. Generated by [[GEN]]-->
# Inferring velocity from tracer

```
./veltracer.py
```
'''

outdir = "out_veltracer"
text += "Output directory `[[OUTDIR]]`:\n"
text += "* [`train.log`]([[EXAMPLES]]/[[OUTDIR]]/train.log)\n"
text += "* [`train.csv`]([[EXAMPLES]]/[[OUTDIR]]/train.csv)\n"

for name in ['u', 'vx']:
    png = f"{name}_00005.png"
    text += f"* [`{png}`]([[EXAMPLES]]/[[OUTDIR]]/{png})  \n"
    text += f'  <img src="[[EXAMPLES]]/[[OUTDIR]]/{png}" width=300>\n'

gen = text
gen = gen.replace('[[GEN]]', os.path.basename(__file__))
gen = gen.replace('[[EXAMPLES]]', "https://cselab.github.io/odil/examples")
gen = gen.replace('[[OUTDIR]]', outdir)
with open("README.md", 'w') as f:
    f.write(gen)
