# Build a Serverless App with Cloud Run that Creates PDF Files

## Overview

In this lab, I learned how to build a serverless app using Cloud Run that converts uploaded files into PDFs and stores them in separate folders in Google Cloud Storage. Pet Theory, a veterinary clinic chain, wanted to address customer complaints regarding their invoices in DOCX format, which many clients couldn't open. They decided to use Cloud Run as a scalable, cost-efficient solution that required minimal maintenance.

## Architecture

The architecture involves a Node.js app deployed on Cloud Run, triggered by events in Google Cloud Storage. When a file is uploaded to a storage bucket, the Cloud Run service processes the file and converts it into a PDF, storing the result in a separate bucket.

## Objectives

By the end of the lab, I was able to:

- Convert a Node.js application to a container.
- Build and deploy containers using Google Cloud Build.
- Create a Cloud Run service that automatically converts files to PDFs.
- Use event-driven architecture with Cloud Storage and Pub/Sub to trigger Cloud Run.

## Prerequisites

This lab assumes intermediate knowledge of the Google Cloud Console and shell environments. Experience with Firebase or Docker is helpful but not required.

---

## Task 1: Understanding the Task

Pet Theory’s goal was to automate the conversion of invoices into PDFs. I reviewed the requirements and learned about using LibreOffice within the Cloud Run environment to handle the document conversion.

## Task 2: Enabling Cloud Run API

I started by enabling the Cloud Run API through the Console. Here, I will insert a screenshot showing the enabled Cloud Run API for clarity.

## Task 3: Deploying a Simple Cloud Run Service

I cloned the Pet Theory repository in Cloud Shell, edited the `package.json` file, and set up the environment for the Node.js app to run. Next, I built the container using Google Cloud Build and verified it in the Artifact Registry. I will include a screenshot of the Artifact Registry showing the container.

I deployed the application and tested it using authorized requests to the Cloud Run service.

## Task 4: Triggering the Cloud Run Service with Cloud Storage

I created two Cloud Storage buckets: one for uploading documents and another for processed PDFs. Then, I created a Pub/Sub notification to trigger the Cloud Run service whenever a new file was uploaded. This section will have screenshots showing the Cloud Storage buckets and Pub/Sub topic setup.

## Task 5: Testing Cloud Run Triggering

To test, I uploaded files to the "upload" bucket and checked Cloud Logging for the file details. This task helped me verify that the Cloud Run service was correctly triggered. A screenshot of Cloud Logging results will be placed here for better understanding.

## Task 6: Adding LibreOffice to the Container

I modified the Dockerfile to include the installation of LibreOffice, which is needed for document conversion. Then I updated the Node.js app to handle the PDF conversion process. The next step was deploying this updated version using Cloud Build, and I will insert a screenshot of the build process here.

## Task 7: Testing the PDF Conversion Service

I created a script to upload files to the "upload" bucket and watched as they were processed and moved to the "processed" bucket. Screenshots of both the upload bucket (before and after file deletion) and the processed bucket with converted PDFs will be added here.

## Lessons Learned

1. **Serverless Architecture**: Cloud Run abstracts infrastructure management, allowing focus on the application itself. It’s scalable and cost-efficient, as the service scales to zero when not in use. This is ideal for businesses with limited IT resources.
2. **Event-driven Processing**: Using Cloud Storage and Pub/Sub to trigger processes allows for seamless, automatic workflows. This is a powerful pattern applicable in real-world scenarios, such as file processing, logging, or notifications.
3. **Containerization**: Building a containerized app using Docker is crucial for deploying consistent, isolated environments. In this lab, I learned how to package Node.js applications with dependencies like LibreOffice. This approach ensures that the app runs reliably across various environments.
4. **Automation**: The automation of invoice conversion saved significant time for Pet Theory’s small operations team. Automation is key to reducing manual workloads and improving efficiency in real-world business processes.

## Skills Gained

- **Cloud Run and Event-driven Architecture**: I became proficient in deploying and managing serverless applications using Cloud Run and automating workflows through Pub/Sub and Cloud Storage.
- **Containerization with Docker**: I gained hands-on experience creating Docker containers for Node.js apps, which is highly valuable for deploying scalable microservices.
- **Logging and Debugging**: I learned how to monitor and debug services using Cloud Logging, ensuring that I could troubleshoot any issues during deployment and testing.

---

Screenshots for each step will be added as specified to provide a clearer, more visual understanding of the process.
