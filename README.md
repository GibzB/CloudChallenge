# ☁️ Cloud Challenges 
My cloud computing learning journey. My hope is to encourage you to build secure, scalable, highly available and cost-effective cloud applications. 

## Google AppSheet
Google Appsheet AppSheet is an application that provides a no-code development platform for application software, which allows users to create mobile, tablet, and web applications using data sources like Google Drive, other cloud-based spreadsheet and database platforms.

#### Lessons Learnt
- Created an app using the AppSheet UI.
- Configured the app using data from a sheet on Google drive.
- Used the live app preview to modify the data displayed in the app.
- Verified that the data changes made via the app have been persisted in the underlying data source (sheet on Google drive).

## Cloud IAM
Google Cloud's Identity and Access Management (IAM) service lets you create and manage permissions for Google Cloud resources. Cloud IAM unifies access control for Google Cloud services into a single system and provides a consistent set of operations.

#### Lessons learnt
- Assigning and revoking roles/permissions to users from Google Cloud Project Owner and Viewer roles.



## DataProc
Cloud Dataproc is a fast, easy-to-use, fully-managed cloud service for running Apache Spark and Apache Hadoop clusters in a simpler, more cost-efficient way. 
Learnt how to use the Cloud Console to create and update a Dataproc cluster and then submit a job in that cluster.



## BQML (Big Query Machine Language)
BigQuery is Google's fully managed, NoOps, low cost analytics database where you can query terabytes and terabytes of data without having any infrastructure to manage or needing a database administrator. BQ uses SQL and can take advantage of the pay-as-you-go model and it also allows you to focus on analyzing data to find meaningful insights.
Big Query Machine Learning (BQML, product in beta) is a new feature in BigQuery where data analysts can create, train, evaluate, and predict with machine learning models with minimal coding.

- ## BigQuery: Command Line
  BigQuery is a serverless, highly scalable cloud data warehouse that solves this problem by enabling super-fast SQL queries using the processing power   of Google's infrastructure.
  BigQuery can be accessed by using the Console, Web UI or a command-line tool using a variety of client libraries such as Java, .NET, or Python. There   are also a variety of solution providers that provide tools to access BigQuery 
  
  #### Lessons learnt
  - Used `bq`, (the python-based command line tool for BigQuery), to query public tables and load sample data into BigQuery



## Troubleshooting Common SQL Errors with BigQuery
Logic of troubleshooting queries. It provides activities within the context of a real-world scenario. Throughout the lab, imagine you're working with a new data analyst on your team, and they've provided you with their queries below to answer some questions on your ecommerce dataset. Use the answers to fix their queries to get a meaningful result.

#### Lessons learnt
- Queried the data-to-insights public dataset
- Used the BigQuery Query editor to troubleshoot common SQL errors
- Used the Query Validator
- Troubleshoot syntax and logical SQL errors


## Google Cloud Billing Reports
I learned how to use Google Cloud Billing reports and the cost breakdown report to gain visibility into your current and forecasted costs!
Google Cloud Billing reports, provides built-in cost reporting for GCP within the Google Cloud Console. Billing reports can be viewed from a live billing account and in that case understanding current and forecasted GCP costs, which then can be analyzed in relation to costs using report filters to identify cost drivers and trends.
I explored a sample of Cloud Billing records in BigQuery. After examining the sample dataset and table, I composed and ran queries on the billing data.



## DataFlow & Apache Beam
All provide templates, for streaming, batch and utility


## Looker & Google Data Studio
Has lookML, and is 100% web based
have many data visualisations, and shared through various google applications

Data studio is integrated into bitquery
Dashboard can be created by templates and link a data source


## Terraform Fundamentals
Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing, popular service providers and custom in-house solutions.

Configuration files describe to Terraform the components needed to run a single application or your entire data center. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform can determine what changed and create incremental execution plans that can be applied.

Terraform can manage both low-level components such as compute instances, storage, and networking, and high-level components such as DNS entries and SaaS features.

## Google Cloud Pub/Sub: Qwik Start - Console


## Introduction to Docker
Docker is an open platform for developing, shipping, and running applications. With Docker, you can separate your applications from your infrastructure and treat your infrastructure like a managed application. Docker helps you ship code faster, test faster, deploy faster, and shorten the cycle between writing code and running code.

Docker does this by combining kernel containerization features with workflows and tooling that helps you manage and deploy your applications.

Docker containers can be directly used in Kubernetes, which allows them to be run in the Kubernetes Engine with ease. After learning the essentials of Docker, you will have the skillset to start developing Kubernetes and containerized applications.

#### Lessons learnt
- Ran containers based on public images from Docker Hub.
- Built your own container images and pushed them to Google Container Registry.
- Learned ways to debug running containers.
- Ran containers based on images pulled from Google Container Registry.


## Classify Text into Categories with the Natural Language API
Used the Cloud Natural Language API lets you extract entities from text, perform sentiment and syntactic analysis, and classify text into categories.

#### Lessons learnt
- Created a Natural Language API request and called the API with `curl`
- Used the NL API's text classification feature
- Used text classification to understand a dataset of a news articles


## Bigtable:Command Line
Cloud Bigtable is Google's NoSQL Big Data database service. It's the same database that powers many core Google services, including Search, Analytics, Maps, and Gmail. Bigtable is designed to handle massive workloads at consistent low latency and high throughput, so it's a great choice for both operational and analytical applications, including IoT, user analytics, and financial data analysis.

#### Lessons learnt
- Used the `cbt` command line to connect to a Cloud Bigtable instance
- Performed basic administrative tasks, and read and write data in a table.



## Cloud SQL for SQL Server
Cloud SQL provides a cloud-based alternative to local MySQL, PostgreSQL, and SQL Server databases. You should use Cloud SQL if you want to spend less time managing your database and more time using it.


#### Lessons learnt
- created a SQL Server instance on Google Cloud and connected to it using SQL Server Management Studio!
- performed basic SQL operations using the Google Cloud Console and a client.


## Encrypting Disks with Customer-Supplied Encryption Keys
Compute Engine encrypts all data at rest by default. It handles and manages this encryption without any additional action on your part. However, one can control and manage this encryption alone by providing thier own encryption keys.

#### Lessons learnt
- Created an encryption key and wrapped it with the Compute Engine RSA public key certificate.
- Encrypted a new persistent disk with your own key.
- Attached the disk to a compute engine instance.
- Created a snapshot from an encrypted disk.


## Creating a BigQuery Authorized View
Giving a view access to a dataset is also known as creating an authorized view in BigQuery. An authorized view lets you share query results with particular users and groups without giving them access to the underlying tables. You can also use the view's SQL query to restrict the columns (fields) the users are able to query.

#### Lessons learnt
- Created and used Authorized Views in BigQuery.
- Implemented row-level filtering using information about the logged-in user.
- Set permissions on BigQuery datasets.
- Authorized Views to provide audiences read-only access to subsets of tables.
- Used the `SESSION_USER()` function to limit access to specific rows within a table/view.


## Orchestrating the Cloud with Kubernetes
Kubernetes is an open source project (available on kubernetes.io) which can run on many different environments, from laptops to high-availability multi-node clusters, from public clouds to on-premise deployments, from virtual machines to bare metal.

Used the managed Kubernetes Engine environment that allowed me to focus on experiencing Kubernetes rather than setting up the underlying infrastructure.

Used [App](https://github.com/kelseyhightower/app); a 12-Factor application and the following Docker images:
   -  [`kelseyhightower/monolith`](https://hub.docker.com/r/kelseyhightower/monolith) - Monolith includes auth and hello services.
   -  [`kelseyhightower/auth`](https://hub.docker.com/r/kelseyhightower/auth) - Auth microservice. Generates JWT tokens for authenticated users.
   -  [`kelseyhightower/hello`](https://hub.docker.com/r/kelseyhightower/hello) - Hello microservice. Greets authenticated users.
   -  [`nginx`](https://hub.docker.com/_/nginx) - Frontend to the auth and hello services.

#### Lessons Learnt
- Provisioned a completed Kubernetes cluster using Kubernetes Engine.
- Deployed and managed Docker containers using kubectl.
- Broke an application into microservices using Kubernetes' Deployments and Services


## Using gsutil to Perform Operations on Buckets and Objects
`gsutil` is a Python application that lets you access Cloud Storage from the command line. The gsutil tool has commands such as `mb` and `cp` to perform operations. Each command has a set of options that are used to customize settings further.

#### Lessons Learnt
- Created a bucket
- Copied files from a local folder to a bucket
- Synchronized the contents of the local folder with the contents of the bucket
- Changed access control permissions on objects
- Deleted a bucket.


## Deploying an Open Source Cassandra™ Database using the GCP Marketplace
Apache Cassandra for GCP gives users and enterprises a simple deployment process to quickly install a Cassandra cluster on GCP in a single region across multiple zones. Each cluster also includes a VM that provides a complete set of development resources including code examples, docs, and data integration tools. Optionally, DataStax Luna also provides subscription-based support for open-source Cassandra on GCP. DataStax Luna subscribers get the benefits of open-source software, with direct access to leading Cassandra contributors.

#### Lessons Learnt
- Deployed an Apache Cassandra™ database, 
- Connected to the database using CQL Shell and run some simple DDL commands to create a table, 
- Loaded some data and query it.


## Google Cloud Sustainability
built a collection of tools to help you accurately report the carbon emissions associated with your Google Cloud usage and take action to reduce your carbon footprint. The Carbon Sense suite brings together features from multiple Google Cloud products, like Active Assist and Carbon Footprint, to help users everywhere make progress towards ensuring a healthier planet.

There are three key categories of carbon emissions associated with running workloads in the cloud:

- Electricity consumption
- Burning on-site fossil fuels
- Upstream and downstream activities

Carbon-free energy includes wind, solar, geothermal, biomass, nuclear, hydropower, and pumped storage or battery storage discharge. For each region    Google Cloud operates in, we measure the percentage of carbon free energy (CFE%) consumed in a particular location on an hourly basis.
The regional CFE score represents the average percentage of time your applications deployed in that cloud region will be running on carbon-free energy.

To lower your carbon emissions, you need to reduce the electricity consumption of your cloud workloads from carbon-based sources. To lower your carbon emissions, here are the recommended primary strategies:

1. Choose cloud regions with higher average hourly CFE%, and lower grid carbon intensity. For regions that have the same CFE%, use grid carbon intensity to further compare the emissions performance of those regions.
2. Optimize cloud workloads to reduce carbon emissions. For example, increase efficiency by using elastic cloud services and autoscaling features to minimize unused compute resources, and run batch workloads during times when grid carbon intensity is lower.
3. Set organizational policies to restrict the location of cloud resources to cleaner regions.

#### Lessons Learnt
- Explored your Carbon Footprint Data
- Used the Cloud Region Picker
- Reduced your cloud carbon footprint with Active Assist recommendations


## Cloud Scheduler
Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It allows you to schedule virtually any job, including batch, big data jobs, cloud infrastructure operations, and more. You can automate everything, including retries in case of failure to reduce manual intervention. Cloud Scheduler allows you to manage all your automation tasks from one place.

#### Lessons Learnt
- Created a Cloud Scheduler job.
- Set a recurring schedule for a job.
- Specified a Cloud Pub/Sub topic as the job target.
- Ran a job.
- Verified success.


## Datastore
(Cloud Datastore) is a highly scalable, fully managed NoSQL database service offered by Google on the Google Cloud Platform.
Cloud storage is something that allows you to save data and files in an off-site location that you access either through the public internet or a dedicated private network connection. This is very cost-effective for businesses since physical files can replaced with cloud storage records.[3] Cloud Datastore is built upon Google's Bigtable and Megastore technology.
Google Cloud Datastore allows the user to create databases either in Native or Datastore Mode. Native Mode is designed for mobile and web apps, while Datastore Mode is designed for new server projects.

Datastore features include:

- `Atomic transactions.` 
Datastore can execute a set of operations where either all succeed, or none occur.
High availability of reads and writes. Datastore runs in Google data centers, which use redundancy to minimize impact from points of failure.
- `Massive scalability with high performance.`
Datastore uses a distributed architecture to automatically manage scaling. Datastore uses a mix of indexes and query constraints so your queries scale with the size of your result set, not the size of your data set.
- `Flexible storage and querying of data.` 
Datastore maps naturally to object-oriented and scripting languages, and is exposed to applications through multiple clients. It also provides a SQL-like query language.
- `Balance of strong and eventual consistency.` 
Datastore ensures that entity lookups by key and ancestor queries always receive strongly consistent data. `All other queries are eventually consistent. The consistency models allow your application to deliver a great user experience while handling large amounts of data and users.
- `Encryption at rest.` 
Datastore automatically encrypts all data before it is written to disk and automatically decrypts the data when read by an authorized user. For more information, see Server-Side Encryption.
- `Fully managed with no planned downtime.` 
Google handles the administration of the Datastore service so you can focus on your application. Your application can still use Datastore when the service receives a planned upgrade.

Note: Firestore, the newest version of Datastore, makes all queries strongly consistent.

#### Lessons Learnt
- Stored and queried data in Google Cloud Datastore using the Google Cloud.


## Transfer Learning (a case of Classifying Images of Cats and Dogs)

In transfer learning, building a new model to classify your original dataset, reuse of the extraction feature part and re-train the classification part with the dataset. This method uses less computational resources and training time. Deep learning from scratch can take days, but transfer learning can be done in short order.
Tensorflow(an end-to-end open source platform for machine learning) tools, libraries and community services pushes for easy build and deployment of ML powered applications.

#### Lessons Learnt
- Examined and understood my image data
- Built an input pipeline using Keras ImageDataGenerator
- Used a pre-trained model for feature extraction
- Fine-tuned a pre-trained model


## Working with Cloud Build
 
Cloud Build is a service that executes your builds on Google Cloud. Cloud Build can import source code from a variety of repositories or cloud storage spaces, execute a build to your specifications, and produce artifacts such as Docker containers or Java archives.

#### Lessons Learnt
- Used Cloud Build to build and push Docker container
- Used Container Registry to store and deploy containers




## Managing Deployments Using Kubernetes Engine
 
 
Heterogeneous deployments typically involve connecting two or more distinct infrastructure environments or regions to address a specific technical or operational need. Heterogeneous deployments are called "hybrid", "multi-cloud", or "public-private", depending upon the specifics of the deployment. For the purposes of this lab, heterogeneous deployments include those that span regions within a single cloud environment, multiple public cloud environments (multi-cloud), or a combination of on-premises and public cloud environments (hybrid or public-private).

Various business and technical challenges can arise in deployments that are limited to a single environment or region:

Maxed out resources: In any single environment, particularly in on-premises environments, you might not have the compute, networking, and storage resources to meet your production needs.
Limited geographic reach: Deployments in a single environment require people who are geographically distant from one another to access one deployment. Their traffic might travel around the world to a central location.
Limited availability: Web-scale traffic patterns challenge applications to remain fault-tolerant and resilient.
Vendor lock-in: Vendor-level platform and infrastructure abstractions can prevent you from porting applications.
Inflexible resources: Your resources might be limited to a particular set of compute, storage, or networking offerings.
Heterogeneous deployments can help address these challenges, but they must be architected using programmatic and deterministic processes and procedures. One-off or ad-hoc deployment procedures can cause deployments or processes to be brittle and intolerant of failures. Ad-hoc processes can lose data or drop traffic. Good deployment processes must be repeatable and use proven approaches for managing provisioning, configuration, and maintenance.

Three common scenarios for heterogeneous deployment are multi-cloud deployments, fronting on-premises data, and continuous integration/continuous delivery (CI/CD) processes.



#### Lessons Learnt
- Worked more with the `kubectl` command-line tool, and many styles of deployment configurations set up in YAML files to launch, update, and scale deployments.
- Updated deployments and deployment styles



## VPC Network Peering

Google Cloud Virtual Private Cloud (VPC) Network Peering allows private connectivity across two VPC networks regardless of whether or not they belong to the same project or the same organization.

VPC Network Peering allows you to build SaaS (Software-as-a-Service) ecosystems in Google Cloud, making services available privately across different VPC networks within and across organizations, allowing workloads to communicate in private space.

VPC Network Peering is useful for:

Organizations with several network administrative domains.
Organizations that want to peer with other organizations.
If you have multiple network administrative domains within your organization, VPC Network Peering allows you to make services available across VPC networks in private space. If you offer services to other organizations, VPC Network Peering allows you to make those services available in private space to those organizations.

The ability to offer services across organizations is useful if you want to offer services to other enterprises, and it is useful within your own enterprise if you have several distinct organization nodes due to your own structure or as a result of mergers or acquisitions.

VPC Network Peering gives you several advantages over using external IP addresses or VPNs to connect networks, including:

Network Latency: Private networking offers lower latency than public IP networking.

Network Security: Service owners do not need to have their services exposed to the public Internet and deal with its associated risks.

Network Cost: Networks that are peered can use internal IPs to communicate and save Google Cloud egress bandwidth costs. Regular network pricing still applies to all traffic.



## Ingesting Data Into The Cloud
 
The techniques used to ingest this data from the website into the cloud can be applied to other data sets that provide comprehensive real world data but must be parsed and cleaned before to be usefull.

#### Lessons Learnt
- Used a bash script to download selected data from a large public data set(US Bureau of Transport Statistics (BTS) website).
- Stored the data in Cloud Storage
- Loaded data into Google BigQuery

## Cloud Run
Cloud Run is a managed compute platform that enables you to run stateless containers that are invocable via HTTP requests. Cloud Run is serverless: it abstracts away all infrastructure management, so you can focus on what matters most — building great applications.

Cloud Run automatically and horizontally scales your container image to handle the received requests, then scales down when demand decreases.

Knative, letting you choose to run your containers either fully managed with Cloud Run, or in your Google Kubernetes Engine cluster with Cloud Run on GKE.

#### Lessons Learnt
- Deployed an application packaged in a container image to Cloud Run.



## Detect Labels, Faces, and Landmarks in Images with the Cloud Vision API
The Cloud Vision API lets you understand the content of an image by encapsulating powerful machine learning models in a simple REST API.
In this lab, we will send images to the Vision API and see it detect objects, faces, and landmarks.

#### Lessons Learnt
- Called the Vision API with curl by passing it the URL of an image in a Cloud Storage bucket
- Used the Vision API's label, face, and landmark detection methods


## Google Workspace Admin: Provisioning
Google Workspace Provisioning is supported by Google to automate user provisioning for many cloud applications. With Google Workspace User Provisioning, you can provision all the users with their identities from any external sources automatically in the Google Admin console.

#### Lessons learnt
- Created Google Groups
- Created a Calendar resource
- Adde a domain to your Google Workspace organization.

## Google Workspace Admin: Managing Applications
Designated "power users" (for example, an external service desk or key-users of departments) can perform simple tasks that would otherwise have to be carried out by the Google domain administrators. User management is key to Google Workspace administration since it’s the first step in building a collaborative team environment. Once that user logs in they have access to Google-powered apps like Gmail, Meet, Drive, Calendar, and more.
This tool allows your Google domain administrators to adjust settings in the user account. Without having to log into the account. This ensures the security of the account and the privacy of your employees while simplifying communication, file sharing, and provide everything you need to unite your team for success.Touching on three different applications in this lab, specifically Gmail, Google Vault, and Google Drive. 

#### Lessons learnt
- Created three OUs and add users to those OUs
- Configured application access based on OUs
- Configured application settings based on OUs


## Google Workspace Admin: Securing
Google Workspace administrators are presented with a wealth of security settings, which they will need to learn in order to effectively keep their environment secure.
With options not limited to reviewing a list of all user accounts and devices, disabling or removing accounts and devices accordingly. They can also review and manage Google Workspace apps, Google Services, Marketplace Apps, and any apps that connect to Google Workspace via SAML (Security Assertion Markup Language). 

#### Lessons learnt
- Reviewed password policy settings
- Enabled user account recovery
- Enabled 2-Step Verification for a subset of users
- Whitelisted apps in the Marketplace

## Deploy Kubernetes Load Balancer Service with Terraform
A service is a grouping of pods that are running on the cluster. Services are "cheap" and you can have many services within the cluster. Kubernetes services can efficiently power a microservice architecture.

Services provide important features that are standardized across the cluster: load-balancing, service discovery between applications, and features to support zero-downtime application deployments.

Each service has a pod label query which defines the pods which will process data for the service. This label query frequently matches pods created by one or more replication controllers. Powerful routing scenarios are possible by updating a service's label query via the Kubernetes API with deployment software.
All Kubernetes resources described in YAML files, orchestration with Terraform presents a few benefits:

- One language
You can use the same configuration language to provision the Kubernetes infrastructure and to deploy applications into it.
Drift detection - terraform plan will always present you the difference between reality at a given time and the config you intend to apply.
- Full lifecycle management - 
Terraform doesn't just initially create resources, but offers a single command to create, update, and delete tracked resources without needing to inspect the API to identify those resources.
- Synchronous feedback - 
While asynchronous behavior is often useful, sometimes it's counter-productive as the job of identifying operation results (failures or details of created resource) is left to the user. e.g. you don't have the IP/hostname of the load balancer until it has finished provisioning, hence you can't create any DNS record pointing to it.
- Graph of relationships - 
Terraform understands relationships between resources which may help in scheduling - e.g. Terraform won't try to create a service in a Kubernetes cluster until the cluster exists.

#### Lessons learnt
- Familiarized myself with Kubernetes Services where I set up a Kubernetes cluster and deployed a Load Balancer type NGINX service
- Familiarized myself with `kubectl` CLI.


## Google Cloud Packet Mirroring with OpenSource IDS.
Traffic Mirroring is a key feature in Google Cloud networking for security and network analysis. Its functionality is similar to that of a network tap or a span session in traditional networking. In short, Packet Mirroring captures network traffic (ingress and egress) from select "mirrored sources", copies the traffic, and forwards the copy to "collectors".
Packet Mirroring captures the full payload of each packet and thus consumes additional bandwidth as it is not based on any sampling period, it is able to be used for better troubleshooting, security solutions, and higher layer application based analysis.
founded on a "Packet Mirroring Policy", which contains the following attributes:

Region
VPC Network(s)
Mirrored Source(s)
Collector (destination)
Mirrored traffic (filter)

Google Cloud Packet Mirroring does not require any additional software on the VMs and it is fully distributed across each of the mirrored virtual machines. The "Collector" IDS is placed out-of-path using an Internal Network Load Balancer (ILB) and will receive both "north-south" traffic and "east-west" traffic.

#### Lessons learnt
- Created a Google Cloud environment, configure the "Collector" ILB, configure the Packet Mirror Policy
- Completed network tests to validate the configuration and use of Packet Mirroring with the Open Source IDS.


## HTTPS Content-Based Load Balancer with Terraform
[External HTTP(S) Load Balancing](https://cloud.google.com/load-balancing/docs/https) is a proxy-based Layer 7 load balancer that enables you to run and scale your services behind a single external IP address. External HTTP(S) Load Balancing distributes HTTP and HTTPS traffic to backends hosted on a variety of Google Cloud platforms (such as Compute Engine, Google Kubernetes Engine (GKE), Cloud Storage, and so on), as well as external backends connected over the internet or via hybrid connectivity. 


#### Lessons learnt
- Learned how to configure load balancing modules in Terraform
- Used the modules to create a global HTTPS Content-Based Load Balancer
- Configured Terraform in the Google Cloud environment



## Getting Started with Vault
Vault is an identity-based secrets and encryption management system. A secret is anything that you want to tightly control access to, such as API encryption keys, passwords, or certificates. Vault provides encryption services that are gated by authentication and authorization methods. Using Vault’s UI, CLI, or HTTP API, access to secrets and other sensitive data can be securely stored and managed, tightly controlled (restricted), and auditable.
Vault comes with various pluggable components called secrets engines and authentication methods allowing you to integrate with external systems. The purpose of those components is to manage and protect your secrets in dynamic infrastructure (e.g. database credentials, passwords, API keys).


#### Lessons learnt
- Deployed the Vault development server

- Enabled secrets engines

- Managed authentication methods

- Versioned, created, got, and destroyed secrets

- Created and revoked authorization tokens

- Enable and use the userpass auth method

- Used the Vault web UI

- Used the transit secret engine to encrypt/decrypt data




## Continuous Delivery with Jenkins in Kubernetes Engine
Jenkins is the go-to automation server used by developers who frequently integrate their code in a shared repository. 

Jenkins is an open-source automation server that lets you flexibly orchestrate your build, test, and deployment pipelines. Jenkins allows developers to iterate quickly on projects without worrying about overhead issues that can stem from continuous delivery.

When you need to set up a continuous delivery (CD) pipeline, deploying Jenkins on Kubernetes Engine provides important benefits over a standard VM-based deployment.

When your build process uses containers, one virtual host can run jobs on multiple operating systems. Kubernetes Engine provides ephemeral build executors—these are only utilized when builds are actively running, which leaves resources for other cluster tasks such as batch processing jobs. Another benefit of ephemeral build executors is speed—they launch in a matter of seconds.

Kubernetes Engine also comes pre-equipped with Google's global load balancer, which you can use to automate web traffic routing to your instance(s). The load balancer handles SSL termination and utilizes a global IP address that's configured with Google's backbone network—coupled with your web front, this load balancer will always set your users on the fastest possible path to an application instance.

Now that you've learned a little bit about Kubernetes, Jenkins, and how the two interact in a CD pipeline, it's time to go build one.


#### Lessons learnt
- Provisioned a Jenkins application into a Kubernetes Engine Cluster
- Set up my Jenkins application using Helm Package Manager
- Explored the features of a Jenkins application
- Created and exercise a Jenkins pipeline



## Deploy Your Website on Cloud Run
Running websites can be difficult with all of the overhead of creating and managing VMs, clusters, pods, services, etc. This is fine for larger, multi-tiered applications, but if you are just trying to get your website deployed and visible, it's a lot of overhead.

With Cloud Run, Google Cloud's implementation of Google's Knative framework, you can manage and deploy your website without any of the infrastructure overhead you experience with a VM or pure Kubernetes-based deployments. Not only is this a simpler approach from a management perspective, it also gives you the ability to "scale to zero" when there are no requests coming into your website.

Cloud Run brings "serverless" development to containers and can be run either on your own Google Kubernetes Engine (GKE) clusters or on a fully managed PaaS solution provided by Cloud Run.

#### Lessons learnt
- Built a Docker image using Cloud Build and upload it to Artifact Registry
- Deployed Docker images to Cloud Run
- Managed Cloud Run deployments
- Setup an endpoint for an application on Cloud Run



## Deploy, Scale, and Update Your Website on Google Kubernetes Engine
Running websites and applications is hard. Things go wrong when they shouldn't, servers crash, increase in demand causes more resources to be utilized, and making changes without downtime is complicated and stressful. Imagine if there was a tool that could help you do all this and even allow you to automate it. With Kubernetes, all of this is not only possible, it's easy!


#### Lessons learnt
- Created a GKE cluster
- Created a Docker container
- Deployed the container to GKE
- Exposed the container via a service
- Scaled the container to multiple replicas
- Modified the website
- Rolled out a new version with zero downtime



## Create and Test a Document AI Processor
The Document AI API is a document understanding solution that takes unstructured data, such as documents and emails, and makes the data easier to understand, analyze, and consume. With the general form processor used in this lab, you can extract key/value pairs from a simple document.


#### Lessons learnt
- Created and tested Document AI processor using the Cloud Console.
- Tested Document AI processors using the command line.
- Tested Document AI synchronous API calls using Python.



## Loading Data into Google Cloud SQL
Cloud SQL is a fully managed relational database service for MySQL, PostgreSQL, and SQL Server with rich extension collections, configuration flags, and developer ecosystems.
Many applications running on Compute Engine, App Engine and other services in Google Cloud use Cloud SQL for database storage.

Each Cloud SQL instance is powered by a virtual machine (VM) running on a host Google Cloud server. Each VM operates the database program, such as MySQL Server, PostgreSQL, or SQL Server, and service agents that provide supporting services, such as logging and monitoring. The high availability option also provides a standby VM in another zone with a configuration that's identical to the primary VM.

The database is stored on a scalable, durable network storage device called a persistent disk that attaches to the VM. A static IP address sits in front of each VM to ensure that the IP address an application connects to persists throughout the lifetime of the Cloud SQL instance.

#### Lessons Learnt
- Create Cloud SQL instance
- Create a Cloud SQL database
- Import text data into Cloud SQL
- Build an initial data model using queries


## Cloud Spanner - Database Fundamentals (OD)
Cloud Spanner is Google’s fully managed, horizontally scalable relational database service. Customers in financial services, gaming, retail and many other industries trust it to run their most demanding workloads, where consistency and availability at scale are critical.

#### Lessons Learnt
- Created and deleted an instance, database, tables.
- Insert and modified data.
- Used the Google Cloud CLI with Cloud Spanner.
- Used Automation Tools with Cloud Spanner.



## Datadog: Getting started with the Helm Chart
Datadog is a hosted infrastructure monitoring platform. This chart adds the Datadog Agent to all nodes in your cluster via a DaemonSet. It also optionally depends on the kube-state-metrics chart. For more information about monitoring Kubernetes with Datadog, please refer to the Datadog documentation website.

Datadog offers two variants, switch to a -jmx tag if you need to run JMX/java integrations. The chart also supports running the standalone dogstatsd image.

#### Lessons Learnt
- Deployed the Datadog Helm chart
- Added a toleration to the agent
- Changed configuration values from the Helm chart
- Checked the logs
- Enabled the APM agent
- Enabled the cluster agent


## Check Point: Next-Gen Data Center Security CloudGuard for Google Cloud
Next-Gen Data Center Security CloudGuard for Google Cloud is a comprehensive training program that teaches users how to secure their data centers using the powerful CloudGuard security solution from Check Point. The module covers a wide range of topics, including how to configure and manage firewall policies, how to protect against advanced threats, and how to troubleshoot and optimize security performance. The module also includes hands-on lab exercises that allow users to practice their skills in a simulated environment and gain real-world experience with the CloudGuard solution. Whether you are a security professional looking to expand your knowledge or an IT administrator looking to secure your data center, this module is a valuable resource for anyone looking to improve their security skills.

#### Lessons Learnt
- Prepared a public cloud environment for deployment
- Deployed a Check Point CloudGuard cluster on Google Cloud
- Created and configured the Cluster object on SmartConsole
- Created an access policy and publish/install it on the Cluster
- Created hosts in two different departments/locations and test the connectivity between them.



## Using Elastic Stack to Monitor Google Cloud
The Elastic Stack, also known as the ELK Stack, is a collection of open-source tools that are used for data analysis and visualization. It includes Elasticsearch, Logstash, and Kibana. Elasticsearch is a search engine and data analysis tool, Logstash is used for data collection, and Kibana is a visualization tool. Together, these tools allow for the efficient collection, analysis, and visualization of large amounts of data in real-time. They can be used for a variety of applications such as log analysis, security analytics, and business intelligence.

Throughout the lab, I learnt how to use different Beats modules to collect data from different services on Google Cloud, such as Google Compute Engine, Google Kubernetes Engine, and Google Cloud Storage. You will also learn how to use Logstash, which is a data processing pipeline, to transform and enrich the data collected by Beats before it is indexed in Elasticsearch.
I learnt how to use Kibana, which is a web-based data visualization and exploration tool, to gain insights from the data collected by Beats. With Kibana, you will be able to create visualizations and dashboards that will help you understand the performance of your services on Google Cloud.
I developed a solid understanding of how to use the Elastic Stack to monitor services on Google Cloud and gain insights into their performance.


#### Lessons learnt

- Created an Elasticsearch deployment using Elastic Cloud
- Used Beats to collect and monitor data from Google Cloud services
- Used Kibana to visualize and explore the data collected by Beats
- Used Logstash to transform and enrich the data collected by Beats
- Gained insights into the performance of your services on Google Cloud using the Elastic Stack.
