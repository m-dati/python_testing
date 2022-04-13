
""" Tests for the Python base containers, based on communication functionalities. """

import sys
import os
import time
import wget

def testwww(url, xfile):
    """Test that the simple python webserver answers to an internal get request"""

    found = False
    outdir= "/tmp"
    filename=""

    if xfile in os.listdir(outdir):
        os.remove(outdir+'/'+xfile)

    for x in (range(4)):
        try:
            filename = wget.download(url,outdir)
            print(f"\n N:{x} file:{filename} ")
            if xfile in os.listdir(outdir):
                found = True
                break

        except Exception as e: 
            print(e)
            break

        finally:
            time.sleep(5)

    if found:
        print(f"\nPASS {filename} received")

    else:
        print(f"\nFAIL {url} {filename}")

if __name__ == "__main__":
    a=sys.argv[1]
    b=sys.argv[2]
    testwww(a,b)
