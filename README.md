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
  You can access BigQuery by using the Console, Web UI or a command-line tool using a variety of client libraries such as Java, .NET, or Python. There     are also a variety of solution providers that you can use to interact with BigQuery.
  
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
