from bucket import bucket
from celery import shared_task
from A import settings

# TODO: can be async?
def all_bucket_object_task():
    result = bucket.get_objects()
    return result


@shared_task
def delete_object_task(key):
    bucket.delete_object(key)

@shared_task
def download_object_task(key):
    bucket.download_object(key)

@shared_task
def upload_object_task():
    bucket.upload_file('/home/mohammad/Desktop/myapp/django/aws/testfile.txt', settings.AWS_STORAGE_BUCKET_NAME, 'test_file_s3')