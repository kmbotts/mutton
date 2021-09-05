from abc import ABCMeta

import mutton


class EventHandler(mutton.Handler, metaclass=ABCMeta):

    def __init__(self, request_class):
        """Initialize the handler."""
        super().__init__(request_class)

    def perform(self, request, **kwargs):
        for record in request.records:
            self.process(record)

        return mutton.EventResponse()

    def pre_process_record(self, record):
        pass

    def post_process_record(self, record):
        pass
