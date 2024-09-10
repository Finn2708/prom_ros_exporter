FROM ros:noetic-ros-base

RUN apt-get update && \
    apt-get install -y \
      python3-catkin-tools \
      python3-pip \
      ros-noetic-roscpp-tutorials && \
    apt-get clean
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install prometheus_client

WORKDIR /workspace
COPY src src

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && catkin_make"
RUN echo "source /workspace/devel/setup.bash" >> /root/.bashrc

COPY ros_entrypoint.sh /ros_entrypoint.sh
RUN chmod +x /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]