import os
import zipfile

from dazzle.libs.model.result import Result
	
def fileiterator(zipf):
    for result, archive_file, zip_file in process(zipf):
        if result.success:
            yield (archive_file.filename, zip_file.read(archive_file))


def process(zipf):
    if zipfile.is_zipfile(zipf):
        openzip = zipfile.ZipFile(zipf, "r", zipfile.ZIP_STORED)

        if not openzip.testzip():
            filelist = openzip.infolist()

            for f in filelist:
                # is a file and not dir
                if f.file_size > 0 and f.compress_type != zipfile.ZIP_STORED:
                    if f.file_size < 1024 * 1024 * 4: # 4MB
                        yield (Result(), f, openzip)
                    else:
                        yield (Result(
                            success=False, 
                            message='Zip file contains a file larger than 4MB'), None, None)
        else:
            yield (Result(False, 'Provided file is not a zip file'), None, None)
    else:
        yield (Result(False, 'Provided file is not a zip file'), None, None)






