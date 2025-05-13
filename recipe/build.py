import shlex
import os
import sys
import subprocess
import json

print(json.dumps(dict(os.environ), ensure_ascii=False, indent=2, sort_keys=True))

subprocess.check_call(
    [
        "cmake",
        *shlex.split(os.environ["CMAKE_ARGS"]),
        '-D', 'ENABLE_TLS=1',
        *(['-D', 'ENABLE_RDMA=1'] if sys.platform == 'linux' else []),
        '-G', 'Ninja',
        '.',
        '-B', 'build',
    ]
)

subprocess.check_call(["ninja", '-v', '-C', 'build', 'install'])
