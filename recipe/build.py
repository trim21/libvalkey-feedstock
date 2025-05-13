import shlex
import os
import sys
import subprocess
import json
from pathlib import Path

print(json.dumps(dict(os.environ), ensure_ascii=False, indent=2, sort_keys=True))
print(json.dumps(os.environ["CMAKE_ARGS"], ensure_ascii=False, indent=2, sort_keys=True))
print(json.dumps(shlex.split(os.environ["CMAKE_ARGS"], posix=os.name == 'posix'),
                 ensure_ascii=False, indent=2,
                 sort_keys=True))

subprocess.check_call(
    [
        "cmake",
        *shlex.split(os.environ["CMAKE_ARGS"], posix=os.name == 'posix'),
        '-D', 'ENABLE_TLS=1',
        *(['-D', 'ENABLE_RDMA=1'] if sys.platform == 'linux' else []),
        '-G', 'Ninja',
        '.',
        '-B', 'build',
    ]
)

print(Path('build/cmake_install.cmake').read_text('utf-8'))

subprocess.check_call(["ninja", '-v', '-C', 'build', 'install'])
