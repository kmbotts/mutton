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

    @cached_property
    def event_name(self):
        return str(self.__event_name)

    @cached_property
    def event_source(self):
        return str(self.__event_source)

    @cached_property
    def event_time(self):
        return str(self.__event_time)

    @cached_property
    def event_version(self):
        return str(self.__event_version)

    @cached_property
    def s3(self):
        return self.__s3


class S3Entity:
    def __init__(self, entity):
        super().__init__()
        self.__configuration_id = entity["configurationId"]
        self.__bucket = S3BucketEntity(entity["bucket"])
        self.__object = S3ObjectEntity(entity["object"])
        self.__s3_schema_version = entity["s3SchemaVersion"]

    @cached_property
    def configuration_id(self):
        return str(self.__configuration_id)

    @cached_property
    def bucket(self):
        return self.__bucket

    @cached_property
    def object(self):
        return self.__object

    @cached_property
    def s3_schema_version(self):
        return str(self.__s3_schema_version)


class S3BucketEntity:
    def __init__(self, bucket_entity):
        super().__init__()
        self.__name = bucket_entity["name"]
        self.__arn = bucket_entity["arn"]

    @cached_property
    def name(self):
        return str(self.__name)

    @cached_property
    def arn(self):
        return str(self.__arn)


class S3ObjectEntity:
    def __init__(self, object_entity):
        super().__init__()
        self.__key = object_entity["key"]
        self.__size = object_entity["size"]
        self.__etag = object_entity["eTag"]
        self.__version_id = object_entity["versionId"]
        self.__sequencer = object_entity["sequencer"]

    @cached_property
    def key(self):
        return str(self.__key)

    @cached_property
    def size(self):
        return self.__size

    @cached_property
    def etag(self):
        return str(self.__etag)

    @cached_property
    def version_id(self):
        return str(self.__version_id)

    @cached_property
    def sequencer(self):
        return str(self.__sequencer)
