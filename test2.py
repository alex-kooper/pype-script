from pype_script import iterate
from pype_script.components import pmap, pfilter, preduce
from operator import add

pipeline = (
    iterate(xrange(20)) | pmap(lambda x: x * 3) | pfilter(lambda x: x % 2 == 0) 
)    

for i in pipeline:
    print "Number:  %d" % i

for i in pipeline | preduce(add):
    print "Sum:     %d" % i

print "Minimum: %d" % min(pipeline)
print "Maximum: %d" % max(pipeline)
 
