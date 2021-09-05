from cached_property import cached_property

import mutton


class S3EventRequest(mutton.EventRequest):

    def build_records(self):
        raw = self.event['Records']
        for record in raw:
            record = S3EventRecord(record)
            self.add_record(record)


class S3EventRecord:
    def __init__(self, record):
        super().__init__()
        self.__aws_region = record["awsRegion"]
        self.__event_name = record["eventName"]
        self.__event_source = record["eventSource"]
        self.__event_time = record["eventTime"]
        self.__event_version = record["eventVersion"]
        self.__s3 = S3Entity(record["s3"])

    @cached_property
    def aws_region(self):
        return str(self.__aws_region)


class S3Entity:
    def __init__(self, entity):
        super().__init__()
        self.__configuration_id = entity["configurationId"]
        self.__bucket = S3BucketEntity(entity["bucket"])
        self.__object = S3ObjectEntity(entity["object"])
        self.__s3_schema_version = entity["s3SchemaVersion"]


class S3BucketEntity:
    def __init__(self, bucket_entity):
        super().__init__()
        self.__name = bucket_entity["name"]
        self.__arn = bucket_entity["arn"]


class S3ObjectEntity:
    def __init__(self, object_entity):
        super().__init__()
        self.__key = object_entity["key"]
        self.__size = object_entity["size"]
        self.__etag = object_entity["eTag"]
        self.__version_id = object_entity["versionId"]
        self.__sequencer = object_entity["sequencer"]
