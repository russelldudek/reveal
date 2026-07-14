from pathlib import Path
import base64, io, zipfile, subprocess, sys, shutil
ROOT=Path(__file__).resolve().parents[1]
CHUNKS=ROOT/'scripts'/'bootstrap_chunks'
WORKFLOW=ROOT/'.github'/'workflows'/'campaign-build.yml'
trigger_workflow=WORKFLOW.read_text()
data=''.join(p.read_text() for p in sorted(CHUNKS.glob('part*.txt')))
with zipfile.ZipFile(io.BytesIO(base64.b64decode(data))) as z:
    z.extractall(ROOT)
WORKFLOW.write_text(trigger_workflow)
subprocess.run([sys.executable, str(ROOT/'scripts'/'build_artifacts.py')], check=True)
shutil.rmtree(CHUNKS)
Path(__file__).unlink()
