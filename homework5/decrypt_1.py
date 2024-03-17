import sys

if (len(sys.argv) != 3):
    print('Usage: decrypt.py INFILE OUTFILE')
    exit()

infile = sys.argv[1]
outfile = sys.argv[2]
key = ord('4')

with open(infile, 'rb') as inf:
    with open(outfile, 'wb') as outf:
        contents = inf.read()
        for b in contents:
            outf.write((b ^ key).to_bytes(1, 'big'))
