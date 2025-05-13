import shlex
import os
import sys
import subprocess

subprocess.check_call(
    [
        "cmake",
        *shlex.split(os.getenv("CMAKE_ARGS")),
        '-D', 'ENABLE_TLS=1',
        *(['-D', 'ENABLE_RDMA=1'] if sys.platform == 'linux' else []),
        '-G', 'Ninja',
        '.',
    ]
)

subprocess.check_call(["ninja", '-v', '-c', 'build', 'install'])
