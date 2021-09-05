#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import mutton


def test_base_request():
    """Test base Request."""
    request = mutton.Request({}, {})
    request.event = {'hi': 'hello'}
    request.context = {'hi': 'hello'}
    assert request.event['hi'] == 'hello'
    assert request.context['hi'] == 'hello'


def test_base_handler():
    """Test base Handler."""

    class BaseTestHandler(mutton.Handler):
        """Test handler."""

        def pre_process_record(self, record):
            assert record.event['value'] == 1.0

        def process_record(self, record):
            """Test perform method."""
            response = mutton.Response()
            response.body = record.event['value']
            return response

        def post_process_record(self, record):
            assert record.event['value'] == 1.0

        def handle_exception(self, record, exception):
            raise Exception("Unexpected Error Occurred!")

    test_handler = BaseTestHandler(mutton.Request)
    request_object = {'value': 1.0}
    invocation = test_handler(request_object, {})

    assert invocation == 1.0


def test_base_response():
    """Test base Response."""
    response = mutton.Response()

    # test setitem
    response['test'] = 'hi'
    assert response['test'] == 'hi'

    # test delitem
    del response['test']
    assert 'test' not in response.store

    x = [x for x in response]
    assert x

    response.body = 'hello'
    assert response.serialized == 'hello'
    assert response['body'] == 'hello'

    response.key_map['test'] = 'test'
    response.test = 'hello'
    assert response['test'] == 'hello'

    assert len(response) == len('hello')
