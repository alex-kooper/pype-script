from pype_script import Pipeline
from pype_script.components import map, filter

pipeline = (
    Pipeline(xrange(20)) 
    | map(lambda x: x * 3) | filter(lambda x: x % 2 == 0) | map(lambda x: "Value --> %d" % x)
)    

for i in pipeline:
    print i

