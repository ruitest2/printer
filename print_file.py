#!/usr/bin/env python3
"""
print_file.py  –  tiny CUPS helper

Usage examples
--------------
python print_file.py test.jpg     # print a JPEG
python print_file.py demo.pdf     # print a PDF
"""

import mimetypes
import os
import sys

import cups

# 1. locate file
path = sys.argv[1] if len(sys.argv) > 1 else "test.jpg"
if not os.path.isfile(path):
    sys.exit(f"❌  File not found: {path}")

mime, _ = mimetypes.guess_type(path)
if mime is None:
    sys.exit(f"❌  Could not determine MIME type for {path}")

# 2. connect to CUPS and find the Brother printer queue
conn = cups.Connection()
printers = conn.getPrinters()
queue = next((p for p in printers if "Brother_HL_L2325DW" in p), None)
if queue is None:
    sys.exit("❌  Brother queue not found; current queues: " + ", ".join(printers))

# 3. submit the job
options = {"document-format": mime}

job_id = conn.printFile(queue, path, os.path.basename(path), options)
print(f"✅  Sent {path} ({mime}) to {queue} as job #{job_id}")
