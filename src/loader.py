import json
import io


def get_data_from_s3(client, *, bucket: str, key: str) -> dict:
    """Return a dictionary contains data from S3 file
    Args:
        client:
        bucket (str): specify bucket name
        key (str): specify object key
    """
    response = client.get_object(
        Bucket=bucket,
        Key=key,
    )
    body = response.get('Body')
    return json.load(io.BytesIO(body.read()))
