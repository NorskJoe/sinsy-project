import subprocess
import re

xmlFile = 'test.xml'

htmlOutput = subprocess.check_output([ 'curl', '-v', '-F', 'LANG=jp', '-F', 'SPKR_LANG=english', '-F', 'SPKR=4', '-F', 'SYNALPHA=0.55', '-F', 'VIBPOWER=1', '-F', 'F0SHIFT=0', '-F', 'SYNSRC=@' + xmlFile, 'http://sinsy.sp.nitech.ac.jp/index.php' ])

m = re.search('\.\/(temp\/[0-9_]+\.wav)', htmlOutput)
wavFile = m.group(0)

subprocess.check_call(['curl', '-O', 'http://sinsy.sp.nitech.ac.jp/' + wavFile])

