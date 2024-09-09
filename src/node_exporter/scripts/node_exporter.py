#!/usr/bin/env python

import rospy
from prometheus_client import start_http_server, Gauge
from rosgraph_msgs.msg import TopicStatistics


class ROSPrometheusExporter:
    def __init__(self):
        self.topic_stats = {}

        # Prometheus metrics
        self.topic_frequency_gauge = Gauge('ros_topic_frequency', 'Message frequency on ROS topics (Hz)', ['topic'])
        self.topic_bandwidth_gauge = Gauge('ros_topic_bandwidth', 'Bandwidth usage on ROS topics (bytes/sec)', ['topic'])

        # Start the Prometheus HTTP server to expose metrics at port 8000
        start_http_server(8000)

        # Subscribe to the /statistics topic which provides topic statistics
        rospy.Subscriber('/statistics', TopicStatistics, self.statistics_callback)

        # ROS node initialization
        rospy.init_node('ros_prometheus_exporter', anonymous=True)

    def statistics_callback(self, msg):
        """Callback to handle TopicStatistics messages."""
        # Extract information from the message
        topic = msg.topic
        interval = msg.window_stop - msg.window_start
        frequency = msg.delivered_msgs / interval.to_sec()
        bandwidth = msg.traffic / interval.to_sec()

        # Update the Prometheus metrics
        self.topic_frequency_gauge.labels(topic).set(frequency)
        self.topic_bandwidth_gauge.labels(topic).set(bandwidth)

    def run(self):
        """Run the ROS Prometheus exporter node."""
        rospy.spin()

if __name__ == '__main__':
    try:
        exporter = ROSPrometheusExporter()
        exporter.run()
    except rospy.ROSInterruptException:
        pass
