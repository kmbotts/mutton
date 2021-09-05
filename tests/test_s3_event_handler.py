#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
"""Test base objects."""
import mutton.s3 as mutton


def test_s3_event_handler():
    """Test S3 Handler"""

    class S3TestHandler(mutton.S3EventHandler):
        """Test handler."""

        def pre_process_record(self, record):
            assert record is not None

        def process_record(self, record):
            """Test record."""
            assert record.aws_region == "us-west-2"
            assert record.event_name == "1111"
            assert record.event_source == "source"
            assert record.event_time == "2021-01-01T00:00:00.000Z"
            assert record.event_version == "3333"
            s3 = record.s3
            s3_bucket = s3.bucket
            assert s3_bucket.name == "bucketName"
            assert s3_bucket.arn == "bucketArn"

            s3_object = s3.object
            assert s3_object.key == "objectKey"
            assert s3_object.size > 0
            assert s3_object.etag == "6666"
            assert s3_object.version_id == "7777"
            assert s3_object.sequencer == "8888"

        def post_process_record(self, record):
            assert record is not None

        def handle_exception(self, record, exception):
            raise Exception("Unexpected Error Occurred!", exception)

    test_handler = S3TestHandler()
    request_object = {
        'Records': [
            {
                'awsRegion': 'us-west-2',
                'eventName': '1111',
                'eventSource': 'source',
                'eventTime': '2021-01-01T00:00:00.000Z',
                'eventVersion': "3333",
                's3': {
                    'configurationId': "4444",
                    's3SchemaVersion': "5555",
                    'bucket': {
                        'name': 'bucketName',
                        'arn': 'bucketArn'
                    },
                    'object': {
                        'key': 'objectKey',
                        'size': 1,
                        'eTag': '6666',
                        'versionId': '7777',
                        'sequencer': '8888'
                    }
                }
            }
        ]
    }
    invocation = test_handler(request_object, {})
    assert invocation is None


def test_s3_event_handler_exception():
    """Test S3 Handler"""

    class S3TestHandler(mutton.S3EventHandler):
        """Test handler."""

        def process_record(self, record):
            raise Exception("Throw it!")

        def handle_exception(self, record, exception):
            """Test record."""
            """Test record."""
            assert record.aws_region == "us-west-2"
            assert record.event_name == "1111"
            assert record.event_source == "source"
            assert record.event_time == "2021-01-01T00:00:00.000Z"
            assert record.event_version == "3333"
            s3 = record.s3
            s3_bucket = s3.bucket
            assert s3_bucket.name == "bucketName"
            assert s3_bucket.arn == "bucketArn"

            s3_object = s3.object
            assert s3_object.key == "objectKey"
            assert s3_object.size > 0
            assert s3_object.etag == "6666"
            assert s3_object.version_id == "7777"
            assert s3_object.sequencer == "8888"
            x = exception.args
            assert str(x).__contains__("Throw it!")

    test_handler = S3TestHandler()
    request_object = {
        'Records': [
            {
                'awsRegion': 'us-west-2',
                'eventName': '1111',
                'eventSource': 'source',
                'eventTime': '2021-01-01T00:00:00.000Z',
                'eventVersion': "3333",
                's3': {
                    'configurationId': "4444",
                    's3SchemaVersion': "5555",
                    'bucket': {
                        'name': 'bucketName',
                        'arn': 'bucketArn'
                    },
                    'object': {
                        'key': 'objectKey',
                        'size': 1,
                        'eTag': '6666',
                        'versionId': '7777',
                        'sequencer': '8888'
                    }
                }
            }
        ]
    }
    invocation = test_handler(request_object, {})
    assert invocation is None
