#!/usr/bin/env python3
import mimetypes
import os
import sys

import cups

# 1. locate file
path = "test.jpg"

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
