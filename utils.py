import time
import boto3
from yt_dlp import YoutubeDL
from loguru import logger
import json


def search_download_youtube_video(video_name, num_results=1):
    """
    This function downloads the first num_results search results from Youtube
    :param video_name: string of the video name
    :param num_results: integer representing how many videos to download
    :return: list of paths to your downloaded video files
    """

    ydl_opts = {
                   'max_filesize': 104857600
    }
    with YoutubeDL(ydl_opts) as ydl:
        try:

            videos = ydl.extract_info(f"ytsearch{num_results}:{video_name}", download=True)['entries']
            return [ydl.prepare_filename(video) for video in videos]
        except Exception as e:
            print(f"error in search_download_youtube_video: {repr(e)}")


"""
def get_sqs_messages():
    with open('uconfig.json') as f:
        config = json.load(f)
        
    session = boto3.Session(
        aws_access_key_id=config.get('aws_access_key_id'),
        aws_secret_access_key=config.get('aws_secret_access_key'))
    sqs = session.resource('sqs')
    queue = sqs.Queue(config.get('sqs_url'))
    approximate_messages = queue.attributes.get('ApproximateNumberOfMessages')
    
    return approximate_messages
"""


def calc_backlog_per_instance(sqs_queue_client, asg_client, asg_group_name):

    while True:
        try:
            msgs_in_queue = int(sqs_queue_client.attributes.get('ApproximateNumberOfMessages'))
            asg_size = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_group_name])['AutoScalingGroups'][0]['DesiredCapacity']

            if msgs_in_queue == 0:
                backlog_per_instance = 0
            elif asg_size == 0:
                backlog_per_instance = 99
            else:
                backlog_per_instance = msgs_in_queue / asg_size

            logger.info(f'backlog per instance: {backlog_per_instance}')
            logger.info(f'msgs in queue: {msgs_in_queue}')
            logger.info(f'asg size: {asg_size}')
            # TODO send the backlog_per_instance metric to cloudwatch

            awsregion = 'eu-central-1'
            cloudwatch = boto3.client('cloudwatch', region_name=awsregion)
            cloudwatch.put_metric_data(
                Namespace='Shlomigd-metric',
                MetricData=[
                    {
                        'MetricName': 'backlog_per_instance',
                        'Value': backlog_per_instance,
                        'Unit': 'Count'
                    }
                ]
            )
        except Exception as e:
            print(f"error in calc_backlog_per_instance: {repr(e)}")

        time.sleep(60)
