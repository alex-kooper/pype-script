from pype_script import iterate, sort, pmap

pipeline = (
    iterate(xrange(10, 0, -1)) | sort() | pmap(lambda x: "Value --> %d" % x)
)

for i in pipeline:
    print i

