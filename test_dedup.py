from pype_script import iterate, dedup, pmap

pipeline = (
    iterate((1, 2, 3, 2, 3, 4, 5, 6, 7, 6)) 
    | dedup() | pmap(lambda x: "Value --> %d" % x)
)    

for i in pipeline:
    print i

