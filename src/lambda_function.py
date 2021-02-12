import boto3
import os
import requests

from datahub_metrics_ingest.DHMetric import DHMetric
from datahub_metrics_ingest.FormatterFactory import FormatterFactory
from datahub_metrics_ingest.ElasticsearchDAO import ElasticsearchDAO
from datahub_metrics_ingest.util import write_metrics_to_csv, read_csv


ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL')\
    if os.environ.get('ELASTICSEARCH_API_BASE_URL') is not None else 'http://localhost'


def lambda_handler(event, context):
    # S3 file upload triggered lambda
    try:
        s3fps = {
            (e['s3']['bucket']['name'], e['s3']['object']['key'])
            for e in event['Records']
        }
        for bucket, key in s3fps:
            infile = get_data_stream(bucket, key)
            ingest(infile)
    except Exception as e:
        print(f"Error ingesting NTL metric file {s3fps} ==> {str(e)}")
        raise

def get_data_stream(bucket: str, key: str):
    client = boto3.client('s3')
    obj = client.get_object(Bucket=bucket, Key=key)
    return obj['Body']._raw_stream

def ingest(infile: str, write_to_es: bool = True):
    all_metrics = read_csv(infile)

    formatter = FormatterFactory().get_formatter('ntl')
    metric_objs = formatter.get_data_objects(all_metrics)
    if write_to_es:
        ElasticsearchDAO(ELASTICSEARCH_API_BASE_URL).write_to_elasticsearch(metric_objs)
    return metric_objs


if (__name__ == '__main__'):
    file_dir = os.path.dirname(os.path.realpath(__file__))
    
    with open(os.path.join(file_dir, '../tests/sample.csv'), 'r') as infile:    
        metric_objs = ingest(infile, write_to_es=False)
        

    with open(os.path.join(file_dir, '../tests/sample.csv'), 'r') as infile:
        infile_recs = read_csv(infile)

    infile_sum = sum([int(i['Pageviews']) for i in infile_recs])
    metric_objs_sum = sum([i.count for i in metric_objs])
    
    assert len(metric_objs) == 36
    assert len(metric_objs[0].__dict__.keys()) == 7
    assert metric_objs_sum == infile_sum
    
    write_metrics_to_csv("ntl_metrics.csv", metric_objs)
    print('Tests passed. Sample file "ntl_metrics.csv" generated.')