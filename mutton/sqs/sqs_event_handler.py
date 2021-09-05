from abc import abstractmethod, ABCMeta

import mutton


class SQSEventHandler(mutton.EventHandler, metaclass=ABCMeta):

    def __init__(self):
        """Initialize the handler."""
        super().__init__(mutton.sqs.SQSEventRequest)

