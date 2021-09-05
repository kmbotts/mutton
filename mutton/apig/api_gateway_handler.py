from abc import ABCMeta

import mutton


class APIGatewayHandler(mutton.Handler, metaclass=ABCMeta):

    def __init__(self):
        """Initialize the handler."""
        super().__init__(mutton.apig.APIGatewayRequest)

    def pre_process_record(self, record):
        pass

    def post_process_record(self, record):
        pass
