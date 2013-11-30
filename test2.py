from operator import add
from pype_script import iterate, pmap, pfilter, preduce, pmin

pipeline = (
    iterate(xrange(20)) | pmap(lambda x: x * 3) | pfilter(lambda x: x % 2 == 0)
)

for i in pipeline:
    print "Number:  %d" % i

for i in pipeline | preduce(add):
    print "Sum:     %d" % i

print "Minimum: %d" % (pipeline | pmin()).aggregate()
print "Maximum: %d" % max(pipeline)

