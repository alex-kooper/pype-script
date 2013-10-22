from pype_script.components import map

d = map(lambda x: x * 2)
d.input_iterator = xrange(10)

