#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import mutton.sqs as mutton


def test_sqs_event_handler():
    """Test SQS Handler"""

    class SQSTestHandler(mutton.SQSEventHandler):
        """Test handler."""

        def pre_process_record(self, record):
            assert record is not None

        def process_record(self, record):
            """Test record."""
            assert record.message_id == "1111"
            assert record.receipt_handle == "2222"
            assert record.body == "hello"
            assert record.md5_of_body == "3333"
            assert record.md5_of_message_attributes == "4444"
            assert record.event_source_arn == "arn"
            assert record.event_source == "source"
            assert record.aws_region == "us-west-2"
            assert record.attributes['messageDeduplicationId'] == "5555"
            assert record.attributes['messageGroupId'] == "6666"
            assert record.message_attributes['correlationId']['stringValue'] == "7777"
            assert record.message_attributes['correlationId']['dataType'] == "String"

        def post_process_record(self, record):
            assert record is not None

        def handle_exception(self, record, exception):
            raise Exception("Unexpected Error Occurred!")

    test_handler = SQSTestHandler()
    request_object = {
        'Records': [
            {
                'messageId': '1111',
                'receiptHandle': '2222',
                'body': 'hello',
                'md5OfBody': '3333',
                'md5OfMessageAttributes': '4444',
                'eventSourceArn': 'arn',
                'eventSource': 'source',
                'awsRegion': 'us-west-2',
                'attributes': {
                    'messageDeduplicationId': '5555',
                    'messageGroupId': '6666'
                },
                'messageAttributes': {
                    'correlationId': {
                        'stringValue': '7777',
                        'dataType': 'String'
                    }
                }
            }
        ]
    }
    invocation = test_handler(request_object, {})
    assert invocation is None


def test_sqs_event_handler_exception():
    """Test SQS Handler"""

    class SQSTestHandler(mutton.SQSEventHandler):
        """Test handler."""

        def process_record(self, record):
            raise Exception("Throw it!")

        def handle_exception(self, record, exception):
            """Test record."""
            assert record.message_id == "1111"
            assert record.receipt_handle == "2222"
            assert record.body == "hello"
            assert record.md5_of_body == "3333"
            assert record.md5_of_message_attributes == "4444"
            assert record.event_source_arn == "arn"
            assert record.event_source == "source"
            assert record.aws_region == "us-west-2"
            assert record.attributes['messageDeduplicationId'] == "5555"
            assert record.attributes['messageGroupId'] == "6666"
            assert record.message_attributes['correlationId']['stringValue'] == "7777"
            assert record.message_attributes['correlationId']['dataType'] == "String"
            x = exception.args
            assert str(x).__contains__("Throw it!")

    test_handler = SQSTestHandler()
    request_object = {
        'Records': [
            {
                'messageId': '1111',
                'receiptHandle': '2222',
                'body': 'hello',
                'md5OfBody': '3333',
                'md5OfMessageAttributes': '4444',
                'eventSourceArn': 'arn',
                'eventSource': 'source',
                'awsRegion': 'us-west-2',
                'attributes': {
                    'messageDeduplicationId': '5555',
                    'messageGroupId': '6666'
                },
                'messageAttributes': {
                    'correlationId': {
                        'stringValue': '7777',
                        'dataType': 'String'
                    }
                }
            }
        ]
    }
    invocation = test_handler(request_object, {})
    assert invocation is None
