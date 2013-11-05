from pype_script import iterate, pmap, pfilter, take_first, skip_first

pipeline = (
    iterate(xrange(20)) | pmap(lambda x: x * 3) | pfilter(lambda x: x % 2 == 0) 
    | skip_first(2) | take_first(5) | pmap(lambda x: "Value --> %d" % x)
)    

for i in pipeline:
    print i

