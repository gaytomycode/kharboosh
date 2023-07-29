import io
import sys
import kharboosh

def test_main():
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    kharboosh.main()
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    assert output == "Hello, Kharboosh!\n"
