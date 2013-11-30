
class PipelineError(Exception):
    pass

class Pipeline(object):
    """
    Pipeline represents a chain of iterables that together can transform input
    into output. The first iterable can be any iterable, other iterables, in
    order to be chained (added to pipeline), need to have an attribute
    'input_iterable'. Pipeline can be created like this:

    Pipeline(iterable1) | iterable2 | iterable3

    Pipeline is iterable iteself and can be used in a for loop or any other
    place iterable can be used. If a pipeline is used for side effect (like
    writing into a file or a DB) method run() can be used to run it. There
    are other shortcut methods that allows to run pipeline.
    """

    def __init__(self, first_iterable=None, last_iterable=None):
        self.first_iterable = self.last_iterable = first_iterable

        if last_iterable:
            self.last_iterable = last_iterable

    def add(self, iterable):
        """ add an iterable to the pipeline

        Pipeline is immutable, add creates a new pipeline.
        """
        iterable.input_iterable = self.last_iterable
        return Pipeline(self.first_iterable, iterable)

    # Infix operator '|' can be used as a synonym for add
    __or__ = add

    def __iter__(self):
        return iter(self.last_iterable)

    def to_list(self):
        """ Run the pipeline and return result as a list. """
        return list(self)

    def aggregate(self):
        """ Run (iterate) the pipeline and return the object generated by
            the pipeline.

        The pipline has to end with an aggregate function that generates
        just one value. If pipeline generates more than one value,
        the PipelineError exception is raised.
        """
        lst = self.to_list()

        if len(lst) != 1:
            raise PipelineError(
                """
                Trying to use Pipeline.aggregate() for pipeline
                that returns multiple values'
                """
            )

        return lst[0]

    def run(self):
        """ Run (iterate) pipeline but discard the output object

        This is the method that can be used to run the pipeline if it used for
        side effect, like writing into a file or a database.
        """
        # Unused variable
        #pylint: disable=W0612

        for i in iter(self.last_iterable):
            pass

        #pylint: enable=W0612

#Invalid class name
#pylint: disable=C0103

iterate = Pipeline

