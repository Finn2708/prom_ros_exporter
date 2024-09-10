# PROMETHEUS ROS Exporter

This is a demo node that exports ROS metrics to Prometheus.


# Getting Started

```
# Build the container
docker compose build

# Run the stack
docker compose up -d
```

Open [Grafana](localhost:3000) (User: `admin`, PW: `grafana`) and review the `Chatter` dashboard.
