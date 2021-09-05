from abc import abstractmethod, ABCMeta

import mutton


class SQSEventHandler(mutton.EventHandler, metaclass=ABCMeta):

    def __init__(self):
        """Initialize the handler."""
        super().__init__(mutton.sqs.SQSEventRequest)

    def pre_process_record(self, record):
        pass

    def post_process_record(self, record):
        pass
