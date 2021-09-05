from abc import ABC, abstractmethod


class Handler(ABC):
    """Base Handler."""

    def __init__(self, request_class):
        """Initialize the handler."""
        self.request_class = request_class
        self.request = None

    def __call__(self, event, context, **kwargs):
        self.request = self.request_class(event, context)
        response = self.perform(self.request, **kwargs)

        return response.serialized

    def perform(self, request, **kwargs):
        return self.process(request)

    def process(self, record):
        response = None
        try:
            self.pre_process_record(record)
            response = self.process_record(record)
        except Exception as e:
            self.handle_exception(record, e)
        finally:
            self.post_process_record(record)

        return response

    @abstractmethod
    def pre_process_record(self, record):
        pass

    @abstractmethod
    def process_record(self, record):
        pass

    @abstractmethod
    def post_process_record(self, record):
        pass

    @abstractmethod
    def handle_exception(self, record, exception):
        pass
