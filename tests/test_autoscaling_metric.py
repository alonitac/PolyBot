import unittest2 as unittest
from unittest.mock import Mock
from utils import calc_backlog_per_instance


class TestBacklogPerInstanceMetric(unittest.TestCase):
    def setUp(self):
        self.sqs_queue_client = Mock()
        self.asg_client = Mock()


    def test_no_worker_full_queue(self):
        self.sqs_queue_client.attributes = {
            'ApproximateNumberOfMessages': '100'
        }

        self.asg_client.describe_auto_scaling_groups = Mock(return_value={
            'AutoScalingGroups': [{
                'DesiredCapacity': 0
            }]
        })

        self.assertEqual(calc_backlog_per_instance(self.sqs_queue_client, self.asg_client, None), 99)

    def test_no_worker__queue_empty(self):
        self.sqs_queue_client.attributes = {
            'ApproximateNumberOfMessages': '0'
        }

        self.asg_client.describe_auto_scaling_groups = Mock(return_value={
            'AutoScalingGroups': [{
                'DesiredCapacity': 0
            }]
        })

        self.assertEqual(calc_backlog_per_instance(self.sqs_queue_client, self.asg_client, None), 0)

    def test_2_worker__queue_50(self):
        self.sqs_queue_client.attributes = {
            'ApproximateNumberOfMessages': '50'
        }

        self.asg_client.describe_auto_scaling_groups = Mock(return_value={
            'AutoScalingGroups': [{
                'DesiredCapacity': 2
            }]
        })

        self.assertEqual(calc_backlog_per_instance(self.sqs_queue_client, self.asg_client, None), 25)
