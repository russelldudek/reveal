from pathlib import Path
import base64, io, zipfile, subprocess, sys, shutil
ROOT=Path(__file__).resolve().parents[1]
CHUNKS=ROOT/'scripts'/'bootstrap_chunks'
data=''.join(p.read_text() for p in sorted(CHUNKS.glob('part*.txt')))
with zipfile.ZipFile(io.BytesIO(base64.b64decode(data))) as z:
    z.extractall(ROOT)
subprocess.run([sys.executable, str(ROOT/'scripts'/'build_artifacts.py')], check=True)
shutil.rmtree(CHUNKS)
Path(__file__).unlink()
