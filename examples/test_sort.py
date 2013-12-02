from pype_script import iterate, sort, pmap

pipeline = (
    iterate(xrange(10)) | sort(reverse=True) | pmap(lambda x: "Value --> %d" % x)
)

for i in pipeline:
    print i

