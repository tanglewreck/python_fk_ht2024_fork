#   Skriv ett program som kopierar innehållet i filen du skapade i
#   W06_exercise01.py till en annan, ny, fil.
#
#   TIPS:
#   Läs in innehållet i filen med hjälp av read() och skriv
#   sedan med hjälp av write(). Det behövs två open()-satser för detta.
#

import os
import pathlib
import sys

if len(sys.argv) != 3:
    """Want two command-line arguments: infile outfile"""
    sys.stderr.write(f"Usage: {os.path.basename(sys.argv[0])} INFILE OUTFILE\n")
    raise SystemExit(1)

# try-except here (for IndexError) probably not necessary since we
# already know that there are *two* command-line arguments
# (sys.argv[0] contains the name of the executable, i.e.
# the filename of this program.)
try:
    path_in = pathlib.Path(sys.argv[1])  # Get in-filename
    path_in.stat()                       # Raises FileNotFoundError if
                                      # infile does not exist
    path_out = pathlib.Path(sys.argv[2])
except (IndexError, FileNotFoundError) as e:
    sys.stderr.write(str(e) + "\n")
    raise SystemExit(1)

# Check if output file exist and
# ask user for comfirmation to overwrite.
try:
    if not path_out.exists():
        path_out.touch()    # Try to touch the file: will raise PermissionError
                         # if we don't have the proper permissions
    else:
        confirm = input(f"WARNING: Output file ({path_out}) exists.\nOverwrite [y/N]?")
        # Exit graciously if answer is not 'y' or if empty
        if not confirm.lower() == "y" or not confirm:
            sys.stderr.write(f"Will not overwrite outfile ({path_out}).\n")
            raise SystemExit(0)
except (PermissionError) as e:
    sys.stderr.write(f"Cannot open outfile ({path_out}) for writing:\n{str(e)}\n")

# Try to read from infile (path_in) and write
# to outfile (path_out)
try:
    in_data = path_in.read_text()
    if written := path_out.write_text(in_data, encoding="utf-8"):
        sys.stdout.write(f"Wrote {written} characters to outfile ({path_out})\n")
except (OSError, PermissionError) as e:
    sys.stderr.write(str(e) + "\n")


