from flask import make_response

class Base(object):

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self):
        result = self.run()

        return make_response(
            result[1],
            result[0],
        )

    def run(self):
        #To be implemented in each endpoint's subclass
        raise NotImplementedError

