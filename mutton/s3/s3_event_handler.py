from abc import abstractmethod, ABCMeta

import mutton


class S3EventHandler(mutton.EventHandler, metaclass=ABCMeta):

    def __init__(self):
        """Initialize the handler."""
        super().__init__(mutton.s3.S3EventRequest)

    def pre_process_record(self, record):
        pass

    def post_process_record(self, record):
        pass
