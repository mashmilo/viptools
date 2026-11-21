import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_a import A
from content_b import B
from content_c import C
MORE = {**A, **B, **C}
