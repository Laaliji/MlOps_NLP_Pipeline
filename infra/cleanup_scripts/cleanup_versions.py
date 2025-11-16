# infra/cleanup_versions.py
# This is a placeholder: when you use a hosted system (e.g. Valohai) you will
# call its API to list versions and delete older ones. This script is a template.


import os


VALO_TOKEN = os.environ.get('VALO_TOKEN')


if not VALO_TOKEN:
    print("Set VALO_TOKEN env var to use this script")
    exit(0)


# Implementation depends on Valohai API: see their docs. This file is a reminder/template.


print("Implement version cleanup per provider API")