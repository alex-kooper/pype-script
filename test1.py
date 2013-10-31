from pype_script import iterate, pmap, pfilter

pipeline = (
    iterate(xrange(20)) | pmap(lambda x: x * 3) | pfilter(lambda x: x % 2 == 0) 
    | pmap(lambda x: "Value --> %d" % x)
)    

for i in pipeline:
    print i

