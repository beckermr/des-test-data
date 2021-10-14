import os
import yaml

with open("source_info.yaml") as fp:
    si = yaml.safe_load(fp.read())

for k, v in si.items():
    if isinstance(v, str):
        src = os.path.join(os.environ["MEDS_DIR"], v)
        dst = os.path.join("DESDATA", v)
        if os.path.exists(os.path.join(os.environ["MEDS_DIR"], v)):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            os.system("cp %s %s" % (src, dst))
