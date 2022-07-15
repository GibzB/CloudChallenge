# ☁️ CloudChallenges 
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
