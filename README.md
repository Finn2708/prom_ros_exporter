# PROMETHEUS ROS Exporter

This is a demo node that exports ROS metrics to Prometheus.


# Getting Started

Assuming you run ROS locally, run the launch file like this:
```
catkin build
source devel/setup.bash
roslaunch node_exporter node_exporter.launch
```

Generate some traffic, e.g. with:
```
roslaunch roscpp_tutorials talker_listener.launch
```

Start Prometheus and Grafana:
```
cd docker
docker compose up -d
```

