# Optimize Costs for Google Kubernetes Engine: Challenge Lab

## Introduction

In this lab, I worked on deploying and optimizing the **OnlineBoutique** application on **Google Kubernetes Engine (GKE)**. The primary objective was to manage costs and improve performance by configuring the environment according to best practices. This involved tasks like creating clusters, configuring node pools, updating application components, and applying autoscaling techniques.

Throughout this challenge, I had to apply previously learned concepts, research, and problem-solving skills to complete the tasks. Automated checkpoints provided feedback along the way to ensure tasks were completed correctly. Screenshots of the Google Cloud Console will be placed at key checkpoints for better understanding.

---

## Challenge Scenario

I was tasked with leading the GKE administration for an online shop managed by **OnlineBoutique**. The focus was on optimizing costs while maintaining high performance.

### Objectives:

- Deploy the OnlineBoutique app to GKE.
- Make configuration changes for cost optimization.
- Ensure performance scaling based on traffic demand.

---

## Task 1: Create a Cluster and Deploy the App

The first step was to create a GKE cluster in a specified zone using the naming convention `team-resource-number`. I started by creating a zonal cluster with two nodes, using the machine type `e2-standard-2` to ensure cost-efficiency.

Once the cluster was set up, I created separate namespaces for `dev` and `prod` environments to manage resource segregation. I deployed the OnlineBoutique app to the `dev` namespace using the provided commands.

**Checkpoint**: Screenshot of the cluster configuration and namespaces will be placed here.

---

## Task 2: Migrate to an Optimized Node Pool

Next, I reviewed the resource consumption in the existing node pool and determined that a more optimized pool with smaller machines could be used. I created a new node pool named `custom-pool` using the machine type `custom-2-3584` with two nodes.

After that, I migrated all deployments to this new node pool by cordoning and draining the default pool. Once safely migrated, I deleted the default pool.

**Checkpoint**: Screenshot of the node pool migration and deleted pool will be shown here.

### Lessons Learned:

Migrating workloads between node pools can be done efficiently with careful coordination. In real-world scenarios, this helps reduce resource waste and optimizes infrastructure costs.

---

## Task 3: Apply a Frontend Update

A last-minute frontend update was required. To ensure there was no downtime, I first set a **Pod Disruption Budget (PDB)** for the `frontend` deployment. This ensured that a minimum of one instance was always available during the update.

I updated the frontend Docker image and set the `ImagePullPolicy` to `Always` to pull the latest version during redeploy.

**Checkpoint**: Screenshot of the pod disruption budget and image update will be inserted here.

### Lessons Learned:

Applying a PDB minimizes downtime during updates, a critical real-world practice for businesses running high-availability services.

---

## Task 4: Autoscale for Traffic Surges

To handle anticipated traffic surges, I configured **horizontal pod autoscaling (HPA)** for the `frontend` deployment based on a target CPU utilization of 50%. I set the scaling range between 1 and 5 pods.

Additionally, I enabled **cluster autoscaling** to scale nodes between 1 and 6 nodes. This ensures the cluster scales up during traffic peaks and scales down when demand drops.

Lastly, I simulated a traffic surge using a built-in load generator to observe how the autoscaling performed.

**Checkpoint**: Screenshot of the HPA configuration and cluster autoscaling will be placed here.

### Lessons Learned:

Autoscaling is critical for handling varying traffic loads without over-provisioning resources, directly optimizing cloud infrastructure costs. This is highly applicable for e-commerce and large-scale applications that experience unpredictable traffic patterns.

---

## Task 5: (Optional) Optimize Other Services

After autoscaling the frontend, I monitored other workloads and identified services that were pushing resource limits. I applied additional autoscaling strategies to optimize their performance as well.

If time allowed, I could have implemented **Node Auto Provisioning** to further optimize resource utilization.

---

## Conclusion

In this lab, I successfully deployed and optimized the OnlineBoutique app on GKE by:

1. Creating and configuring clusters.
2. Migrating to optimized node pools.
3. Updating the frontend without downtime.
4. Applying horizontal and cluster autoscaling to manage traffic surges.

These skills are directly applicable in real-world scenarios where cloud cost optimization and performance tuning are crucial for business success.

**Checkpoint**: Final screenshots of all the configured resources will be shown here.

---

## Skills Gained

- GKE Cluster and Node Pool management.
- Kubernetes Namespace and Deployment handling.
- Horizontal and Cluster Autoscaling.
- Pod Disruption Budget management.
- Cost optimization strategies for cloud resources.
