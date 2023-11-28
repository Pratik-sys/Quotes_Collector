import os, boto3, json
from Quote.extension import app

session = boto3.Session(
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRETE_KEY"),
)
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRETE_KEY"),
)
def upload_to_s3():
    """if .env file is present in the root location then upload it to S3 bucket"""
    try:
        if os.path.exists(os.path.abspath(".env")):
            app.looger.info("File is alrady present in %s lcoation", os.path.abspath(".env"))
            s3.upload_file(os.getenv("UPLOAD_PATH"), os.getenv("BUCKET_NAME"), os.getenv("OBJECT"))
            return json.dumps({"Msg" : "File is uploaded"})
        else:
            app.logger.error("File Not found in %s", os.path.abspath(".env"))
            return json.dumps({"Msg" :"Failed while uploading"})
    except FileNotFoundError as ex:
        return json.dumps(ex)

def download_from_s3():
    """if .env file is not present in the download the file from S3 bucket"""
    try:
        if os.path.exists(os.path.abspath(".env")):
            app.looger.info("File is alrady present in %s lcoation", os.path.abspath(".env"))
            return json.dumps({"Msg" : "File lready exist"})
        else:
            app.logger.error("Downloading from S3 bucket to root lcoation")
            s3.download_file(os.getenv("BUCKET_NAME"), os.getenv("OBJECT"), os.getenv("DOWNLOAD_PATH"))
            return json.dumps({"Msg" : "File downloaded"})
    except Exception as ex:
        return json.dumps(ex)
    