from boto import connect_s3
from boto.s3.key import Key  

from dazzle.libs.utils import constants as Constants
from dazzle.libs.model.result import Result

def s3_upload (folder_name, file_names, file_contents):
    if not folder_name:
        raise ValueError('folder not provided')
        
    if not file_names:
        raise ValueError('No files provided')

    if not file_contents:
        raise ValueError('No files provided')

    if len(file_names) != len(file_contents):
        raise AssertionError('Given names are not one-for-one with content')

    conn = connect_s3(Constants.S3_ACCESS_KEY, Constants.S3_SECRET_KEY)
    bucket = conn.get_bucket(Constants.S3_BUCKET)
    k = Key(bucket)

    if not k:
        return Result(success=False, message='S3 connection error')

    files = zip(file_names, file_contents)

    for name, content in files:
        k.key = s3_upload_dir(folder_name) + '/' + name
        k.set_contents_from_string(content, replace=True) 
        k.make_public()

    return Result(success=True)


def s3_upload_dir (template_name):
    return '%s/%s' % (Constants.S3_TEMPLATE_FOLDER_NAME, template_name)


def s3_dir_contents (template_name):
    if not template_name:
        raise ValueError('folder not provided')

    template_loc = s3_upload_dir(template_name)

    conn = connect_s3(Constants.S3_ACCESS_KEY, Constants.S3_SECRET_KEY)
    bucket = conn.get_bucket(Constants.S3_BUCKET)
    bucket_entries = bucket.list(prefix=template_loc)

    prefix_len = len(template_loc)
    file_list = []
    for key in bucket_entries:
        file_name = key.name
        file_list.append(file_name[prefix_len:])

    return file_list






