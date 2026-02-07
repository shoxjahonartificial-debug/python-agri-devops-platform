````markdown
# Python Agri DevOps Platform

<!-- ![telegram-cloud-photo-size-2-5203935126805484093-w](https://github.com/user-attachments/assets/16b5a375-c17e-469e-9953-8515984a962b)
 -->
![Python Agri DevOps Platform](assets/banner.png)

---

## Why this project exists

Modern agricultural platforms increasingly depend on software systems for data processing, automation, monitoring, and decision support.  
Despite this, many agriculture-focused applications are still deployed using **manual, error-prone processes** that do not scale and are difficult to maintain.

The **Python Agri DevOps Platform** was created to answer a simple but critical question:

**Why should agricultural software be built and operated using modern DevOps practices?**

This project demonstrates *why* DevOps is essential by showing:
- how automation reduces human error  
- how containerisation ensures consistency  
- how CI/CD improves reliability and delivery speed  
- how orchestration enables scalability  

The goal is not just to run a Python application, but to operate it **correctly, professionally, and sustainably**.

---

## Project Overview

The **Python Agri DevOps Platform** is a DevOps-focused Python project designed to showcase a complete software delivery lifecycle.  
It integrates continuous integration, continuous deployment, containerisation, and Kubernetes-based orchestration in a single, cohesive platform.

This repository is intentionally structured to reflect **real-world engineering standards**, not simplified examples.

---

## Why DevOps for Agriculture

Agricultural platforms often operate in environments where:
- system downtime affects operations  
- data accuracy is critical  
- scalability is required during peak seasons  
- manual deployments are risky  

Applying DevOps principles ensures that:
- deployments are predictable and repeatable  
- systems recover faster from failures  
- changes can be delivered safely and frequently  
- infrastructure scales with demand  

This project exists to demonstrate those principles in practice.

---

## High-Level Architecture

The platform follows a standard DevOps flow:

1. Code is pushed to GitHub  
2. CI pipelines are triggered automatically  
3. Docker images are built and validated  
4. Kubernetes deploys the application using Helm  

Each stage is automated to reduce risk and improve reliability.

---

## Repository Structure and Why It Matters

```text
python-agri-devops-platform/
│
├── .github/workflows/        # CI/CD automation
├── app/                      # Python application logic
├── devops-chart/             # Helm charts for deployment
├── helm/python-agri/          # Environment configurations
├── Dockerfile                # Container definition
├── requirements.txt          # Dependency management
└── README.md
````

**Why this structure?**

* Clear separation between application and infrastructure
* CI/CD logic isolated from business logic
* Helm charts versioned alongside code
* Easier maintenance and scalability

This structure mirrors professional DevOps repositories.

---

## Application Layer – Why It Is Stateless

The Python application is designed to be **stateless**.

**Why stateless?**

* Enables horizontal scaling
* Simplifies container orchestration
* Improves fault tolerance
* Avoids dependency on local storage

All configuration is externalised, aligning with cloud-native best practices.

---

## Containerisation – Why Docker Is Used

Docker ensures that the application behaves the same way:

* on a developer machine
* in CI pipelines
* in production environments

**Why Docker matters here:**

* eliminates “works on my machine” issues
* standardises deployment
* accelerates onboarding

### Build the Image

```bash
docker build -t python-agri-devops-platform .
```

### Run the Container

```bash
docker run -p 8000:8000 python-agri-devops-platform
```

---

## CI/CD Pipeline – Why Automation Is Mandatory

Manual builds and deployments do not scale.

The CI/CD pipeline exists to ensure:

* every code change is validated
* broken builds are detected early
* deployments are consistent

**Why GitHub Actions?**

* native GitHub integration
* declarative pipelines
* industry-standard tooling

All workflows are defined under `.github/workflows`.

---

## Kubernetes and Helm – Why Orchestration Is Required

Kubernetes manages application lifecycle at scale.

**Why Kubernetes and Helm?**

* automated scheduling
* self-healing containers
* configuration abstraction
* versioned releases

Helm simplifies deployment management and rollback strategies.

### Deploy Using Helm

```bash
helm install python-agri ./devops-chart
```

---

## Monitoring and Observability – Why Visibility Matters

Without observability, failures go unnoticed.

Monitoring enables:

* early failure detection
* performance tracking
* capacity planning

This platform supports integration with monitoring tools to ensure operational awareness.

---

## DevOps Principles Demonstrated

* Continuous Integration
* Continuous Deployment
* Infrastructure as Code
* Automation first approach
* Scalability and resilience
* Operational observability

These principles guide every architectural decision in this project.

---

## Intended Use

This repository is intended for:

* DevOps academic assessment
* Demonstrating professional CI/CD pipelines
* Learning Docker, Kubernetes, and Helm
* DevOps portfolio presentation

---

## Conclusion – Why This Project Matters

The **Python Agri DevOps Platform** demonstrates that DevOps is not optional for modern agricultural software.
By automating delivery, enforcing consistency, and enabling scalability, this project shows *why* DevOps is a foundational requirement for reliable digital agriculture platforms.

---

## Author

**Shoxjahon Artificial**
GitHub: [https://github.com/shoxjahonartificial-debug/python-agri-devops-platform](https://github.com/shoxjahonartificial-debug/python-agri-devops-platform)

---

## License

This project is provided for educational and demonstration purposes.

```
```

![telegram-cloud-photo-size-2-5203964878043943202-w](https://github.com/user-attachments/assets/200081b2-62ca-4963-903d-8a9fe479df30)

---

## Explanation of the Prometheus Metrics Endpoint (`/metrics`)

This file represents the **Prometheus metrics output** exposed by the application through the `/metrics` endpoint.
It is automatically generated by the application using the **Prometheus Python client library** and is used by Prometheus to collect performance data.

The metrics are exposed in **plain text format**, which is the standard format required by Prometheus.

---

### 1. HTTP Requests Counter

```text
# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",path="/",status="200"} 87
http_requests_total{method="GET",path="/metrics",status="200"} 29
```

This metric counts the **total number of HTTP requests** handled by the application.

* `method` shows the HTTP method used (GET)
* `path` shows the endpoint that was accessed
* `status` shows the HTTP response code

For example:

* The root endpoint `/` was accessed **87 times**
* The `/metrics` endpoint was accessed **29 times** by Prometheus

This metric helps monitor **traffic volume** and request behaviour.

---

### 2. HTTP Request Timestamp (`http_requests_created`)

```text
# TYPE http_requests_created gauge
http_requests_created{method="GET",path="/",status="200"} 1.770472736e+09
```

This metric stores the **Unix timestamp** when the first request for this label set was created.

It is useful for:

* understanding when the service started receiving traffic
* correlating request activity with other metrics or events

---

### 3. HTTP Request Latency Histogram

```text
# HELP http_request_duration_seconds HTTP request latency
# TYPE http_request_duration_seconds histogram
```

This metric measures **how long HTTP requests take to be processed**.

The histogram is split into **buckets**, for example:

```text
http_request_duration_seconds_bucket{le="0.1",method="GET",path="/"} 86
http_request_duration_seconds_bucket{le="0.5",method="GET",path="/"} 87
http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/"} 87
```

This means:

* 86 requests were completed in **less than 0.1 seconds**
* All 87 requests were completed in **less than 0.5 seconds**
* `+Inf` represents the total number of requests

---

### 4. Request Count and Total Duration

```text
http_request_duration_seconds_count{method="GET",path="/"} 87
http_request_duration_seconds_sum{method="GET",path="/"} 0.87048
```

* `count` shows the total number of measured requests
* `sum` shows the **total accumulated response time** in seconds

These values are used by Prometheus to calculate:

* average response time
* percentiles (e.g. 95th percentile latency)

---

### 5. Metrics for `/metrics` Endpoint

The same latency and count metrics are also collected for the `/metrics` endpoint itself:

```text
http_request_duration_seconds_count{method="GET",path="/metrics"} 29
```

This confirms that:

* Prometheus is **successfully scraping the application**
* The monitoring pipeline is working correctly

---

## Overall Purpose of These Metrics

These metrics provide **application-level observability**, allowing:

* Monitoring of request volume
* Monitoring of response time performance
* Detection of slow or failing endpoints
* Integration with Grafana dashboards for visualisation

By exposing this `/metrics` endpoint, the application enables **real-time monitoring** using Prometheus and Grafana, which is a standard practice in modern DevOps environments.

![telegram-cloud-photo-size-2-5203964878043943204-w](https://github.com/user-attachments/assets/f804a0a5-8685-402d-9c1d-0ce4bb8304c0)

## Kubernetes Deployment Overview

This diagram represents the current state of the application deployed in a Kubernetes cluster and managed through Helm.

- The **Helm release (`devops-assignment`)** is the root component that manages all Kubernetes resources.
- A **Service (SVC)** exposes the application internally within the cluster.
- A **Deployment (D)** controls the application lifecycle and ensures the desired number of replicas is running.
- Multiple **ReplicaSets (RS)** are shown, representing previous deployment revisions created during updates.
- Only the **latest ReplicaSet** is actively serving traffic, while older ReplicaSets are retained for rollback purposes.
- A **Pod** is running successfully (`1/1 Running`), confirming that the application is healthy and operational.
- Supporting resources such as **ServiceAccount (SA)** and **ServiceMonitor (SM)** are also included for access control and monitoring integration.

This visualization demonstrates a **successful, stable Kubernetes deployment** with versioned rollouts, high availability, and observability enabled — reflecting production-ready DevOps practices.
---
<img width="2048" height="732" alt="image" src="https://github.com/user-attachments/assets/54c2bd9e-3b52-4eff-87e0-a1d8e07c94f0" />


## 📊 Kubernetes Cluster Monitoring (Grafana Dashboard)

This dashboard provides a **real-time overview of Kubernetes cluster health and resource utilisation** using metrics collected from **Prometheus** and visualised in **Grafana**.

It enables operators to monitor **CPU, memory, nodes, pods, and Kubernetes objects** across the cluster.

---

## 🔹 Global Resource Usage

### Global CPU Usage

Displays CPU consumption across the entire cluster:

* **Real** – actual CPU usage by workloads
* **Requests** – CPU resources requested by pods
* **Limits** – maximum CPU limits defined for pods

Example insights:

* Real CPU usage is low (~2–3%), indicating **available headroom**
* Requests and limits are properly configured, reducing the risk of resource contention

---

### Global RAM Usage

Shows cluster-wide memory usage:

* **Real** – actual memory usage
* **Requests** – requested memory by workloads
* **Limits** – memory limits applied to pods

Example:

* Memory utilisation is around **66%**, which is within a safe operational range
* Helps detect potential memory pressure or leaks

---

## 🔹 Cluster Overview

### Nodes

```
Nodes: 4
```

Indicates the number of worker nodes currently available in the Kubernetes cluster.

---

### Namespaces

```
Namespaces: 8
```

Shows logical isolation units used to organise workloads and services.

---

### Running Pods

```
Running Pods: 36
```

Represents the number of actively running pods across all namespaces.

---

## 🔹 Kubernetes Resource Count

This panel tracks the number of core Kubernetes objects over time:

* ConfigMaps
* Secrets
* Deployments
* Services
* Pods
* Containers
* DaemonSets
* StatefulSets

**Purpose:**

* Detect unexpected changes
* Identify configuration drift
* Monitor scaling behaviour

Stable values indicate a **healthy and predictable cluster state**.

---

## 🔹 CPU Utilisation Over Time

### Cluster CPU Utilisation

Shows CPU usage trends across the cluster:

* Short spikes indicate temporary workload bursts
* Sustained low usage confirms **efficient resource management**

This data is useful for:

* Capacity planning
* Horizontal Pod Autoscaler (HPA) tuning

---

## 🔹 Memory Utilisation Over Time

### Cluster Memory Utilisation

Tracks memory usage percentage across all nodes:

* Stable usage around **65–67%**
* No sharp upward trends, indicating **no memory leaks**

This helps ensure:

* Node stability
* Prevention of OOM (Out Of Memory) errors

---

## 🔹 Namespace-Level Visibility

### CPU Utilisation by Namespace

Shows which namespaces consume the most CPU resources.

### Memory Utilisation by Namespace

Highlights memory usage distribution across namespaces.

**Benefits:**

* Identify noisy neighbours
* Enforce resource quotas
* Improve multi-tenant cluster governance

---

## 🛠 Observability Stack

* **Prometheus** – collects Kubernetes and application metrics
* **Grafana** – visualises cluster health and performance
* **Kubernetes** – orchestrates containerised workloads
* **Argo CD** – enables GitOps-based deployment and monitoring consistency

---



