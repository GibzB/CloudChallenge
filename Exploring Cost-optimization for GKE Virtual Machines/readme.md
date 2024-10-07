# Exploring Cost Optimization for GKE Virtual Machines

## Overview

In this lab, I explored how to optimize infrastructure resources in Google Kubernetes Engine (GKE) to reduce costs, while ensuring efficient architecture for application workloads. By selecting suitable machine types and understanding cross-zonal traffic, I learned how to implement strategies that maximize resource utilization and minimize unnecessary costs.

### Objectives

This lab aimed to teach me how to:

* Examine resource usage of a deployment.
* Scale up a deployment.
* Migrate workloads to a node pool with an optimized machine type.
* Explore regional cluster location options.
* Monitor flow logs between pods in different zones.
* Move chatty pods to minimize cross-zonal traffic costs.

## Task 1: Understanding Node Machine Types

### General Overview

A machine type defines virtual hardware resources for a Compute VM instance, such as memory, vCPUs, and disk limits. The two major types I worked with were **E2** and  **N1** , where **E2** offers cost optimization and is generally ideal for small workloads. For larger applications, optimized machine types reduce costs by efficiently utilizing available resources.

Choosing the right machine type is crucial for cost efficiency. In real-world scenarios, this can apply to organizations running large-scale workloads—selecting a properly shaped machine type prevents unnecessary scaling and ensures high performance at a reduced cost.

## Task 2: Optimizing the Hello App Cluster

### Inspecting the Hello Demo Cluster's Resources

I started with two **E2-medium** (2vCPU, 4GB) nodes, deploying the Hello App with 400 mcpu requests and kube-system pods.

### Scaling Up the Hello App

I scaled the app by adding a new replica and noticed that the cluster experienced a  **cpu bottleneck** , leading me to increase node pool size to handle the additional workload.

#### Scaling Example (Add Screenshot)

In this step, I will include a screenshot showing the CPU allocation of nodes after scaling.

This task illustrated how real-world applications might require node pool resizing based on fluctuating demand. For instance, e-commerce websites experience high traffic during sales, necessitating an infrastructure that can automatically scale efficiently while keeping costs under control.

## Task 3: Migrate to an Optimized Node Pool

### Creating an Optimized Node Pool

I created a new node pool with a larger machine type and migrated the workload. Moving the app from three **E2-medium** machines to one **E2-standard-2** resulted in significant cost savings without performance loss.

#### Node Pool Creation (Add Screenshot)

Here, I will include a screenshot of the node pool migration and cost comparison.

Optimizing nodes in Kubernetes clusters is akin to managing physical data centers, where optimizing hardware selection ensures fewer machines handle the same workloads at lower costs. In real-world cloud architecture, such optimization strategies are crucial for businesses with tight infrastructure budgets.

## Task 4: Managing Regional Clusters and Reducing Cross-Zonal Traffic

### Observing Traffic

I monitored cross-zonal traffic between two chatty pods using  **VPC flow logs** . The ping request between the two pods running on different zones demonstrated noticeable latency and potential cost increases due to inter-zonal traffic.

#### Flow Logs Analysis (Add Screenshot)

Here, I will add a screenshot from the BigQuery dataset showing flow logs indicating cross-zonal traffic.

### Moving Pods to the Same Zone

By adjusting the **Pod Anti Affinity** rule to a **Pod Affinity** rule, I ensured that both pods were scheduled on the same node. This minimized cross-zonal traffic and improved latency.

#### Traffic Reduction (Add Screenshot)

A screenshot here will demonstrate the reduced latency after moving the pods to the same zone.

In large clusters, moving chatty services to the same zone can significantly reduce operational costs. Enterprises using GKE in multiple regions can optimize network traffic and save on cross-zonal egress costs.

## Conclusion

Through this lab, I developed a deep understanding of Kubernetes infrastructure optimization, specifically in Google Cloud's GKE. By learning how to right-size node pools, manage inter-zonal traffic, and handle resource scaling, I gained valuable skills applicable in real-world cloud operations where cost and performance are of paramount importance.
