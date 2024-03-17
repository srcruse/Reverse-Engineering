import sys

if (len(sys.argv) != 3):
    print('Usage: decrypt.py INFILE OUTFILE')
    exit()

infile = sys.argv[1]
outfile = sys.argv[2]
key = [ord(i) for i in 'R3V3R53']

with open(infile, 'rb') as inf:
    with open(outfile, 'wb') as outf:
        contents = inf.read()
        strs = [contents[i:i+7] for i in range(0, len(contents), 7)]
        for s in strs:
            for i in range(0,len(s)):
                outf.write((s[i] ^ key[i]).to_bytes(1, 'big'))
