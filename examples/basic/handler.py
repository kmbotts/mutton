#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mutton


class BasicHandler(mutton.Handler):
    """Test handler."""

    def pre_process_record(self, record):
        pass

    def process_record(self, record):
        """Test perform method."""
        response = mutton.Response()
        response.body = record.event
        return response

    def post_process_record(self, record):
        pass

    def handle_exception(self, record, exception):
        raise RuntimeError(exception)


basic = BasicHandler(mutton.Request)
