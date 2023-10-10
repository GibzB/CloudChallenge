# Getting Started with GKE


* Provisioned a [Kubernetes](http://kubernetes.io/) cluster using [Kubernetes Engine.](https://cloud.google.com/container-engine)
* Deployed and managed Docker containers using `kubectl`.


List of enabled APIs that need to be enabled

* Kubernetes Engine API
* Container Registry API


Named the cluster **webfrontend** and configure it to run 2 nodes:

```
gcloud container clusters create webfrontend --zone $MY_ZONE --num-nodes 2
```


To check your the installed version of Kubernetes using the `kubectl version` command:

```
kubectl version
```

> The `gcloud container clusters create` command automatically authenticated `kubectl` for you.


Launched a single instance of the nginx container. (Nginx is a popular web server.)

```
kubectl create deploy nginx --image=nginx:1.17.10
```


Exposed the nginx container to the Internet:

```
kubectl expose deployment nginx --port 80 --type LoadBalancer
```


Scaled up the number of pods running:

```
kubectl scale deployment nginx --replicas 3
```
