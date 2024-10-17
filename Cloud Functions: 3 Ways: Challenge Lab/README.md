
# Cloud Functions: 3 Ways - Challenge Lab

## Overview

In this challenge lab, I was tasked with solving a real-world problem for a new development team by automating code execution in response to specific events within a Google Cloud project. The goal was to implement solutions using Cloud Storage and HTTP triggers. Unlike other labs that provide step-by-step instructions, I was given a scenario and left to figure out the steps on my own. An automated scoring system was used to validate my progress at various stages.

> *PS: I will be placing the screenshots at appropriate points throughout the README to illustrate the checkpoints for each task, ensuring clarity and enhancing understanding.*

## Scenario & Objectives

The development team required automation for their project with the following requests:

1. Create a Cloud Storage bucket to store project files.
2. Create and deploy a Cloud Function (2nd gen) that triggers on new events in the Cloud Storage bucket.
3. Create and deploy a Cloud Function (2nd gen) that responds to HTTP requests with minimum instances set to avoid cold starts.

Throughout the challenge, I ensured that the appropriate APIs were enabled, IAM permissions were correctly assigned, and all resources were created in the specified region.


## Tasks

### Task 1: Create a Cloud Storage Bucket

The first task was to create a Cloud Storage bucket using my Project ID as the bucket name.

#### Steps:

1. Navigate to the **Cloud Storage** section of the Google Cloud Console.
2. Click **Create Bucket** and provide the Project ID as the bucket name.
3. Choose the appropriate region, ensuring it's the region specified in the task requirements.

![1](<images/Screenshot 2024-10-17 at 11.20.27.png>)

#### Task 2: Create, Deploy, and Test a Cloud Storage Function (2nd Gen)

Next, I created and deployed a Cloud Function that responds to new events in the Cloud Storage bucket. The function was written in **Node.js 20** and deployed with **2 maximum instances** to handle scaling.

#### Steps:

1. **Enable APIs**: Ensure that the Cloud Functions API and Cloud Storage API are enabled.
2. **Create a Function**: Navigate to **Cloud Functions** and create a new function.
3. Name the function (I used  `cs-monitor`), set the trigger type to **Cloud Storage**, and specify the bucket created in Task 1 as the trigger.
4. Set the **Region** to match the requirements.
5. **Code the Function**:
   - **index.js**: (Replace `cs-monitor` with your function name)
     ```javascript
     const functions = require('@google-cloud/functions-framework');

     functions.cloudEvent('cs-monitor', (cloudevent) => {
       console.log('A new event in your Cloud Storage bucket has been logged!');
       console.log(cloudevent);
     });
     ```
   - **package.json**:
     ```json
     {
       "name": "nodejs-functions-gen2-codelab",
       "version": "0.0.1",
       "main": "index.js",
       "dependencies": {
         "@google-cloud/functions-framework": "^2.0.0"
       }
     }
     ```
6. Set the **Entry point** to your function name and deploy the function.
7. Test the function by uploading any file to the Cloud Storage bucket.

![2](<images/Screenshot 2024-10-17 at 11.27.22.png>)

#### Lessons Learned:

- I learned the importance of handling event-based triggers for real-time systems using Cloud Functions. This applies in real-world scenarios where automation of backend processes like data logging, file conversions, or notification systems can enhance operational efficiency.

### Task 3: Create and Deploy a HTTP Function (2nd Gen)

#### Description:

The third task involved creating an HTTP-triggered Cloud Function, which could respond to HTTP requests. The goal was to minimize cold starts by setting **1 minimum instance** and allowing up to **2 maximum instances** for better scalability.

#### Steps:

1. **Create a Function**: Navigate to **Cloud Functions** and create a new HTTP-triggered function.
2. Name the function (I used `http-responder`) and set the trigger to **HTTP**.
3. Set the **Region** to match the task's requirements.
4. **Code the Function**:
   - **index.js** (replace `http-responder` with your function name):
     ```javascript
     const functions = require('@google-cloud/functions-framework');

     functions.http('http-responder', (req, res) => {
       res.status(200).send('HTTP function (2nd gen) has been called!');
     });

     ```
   - **package.json**:
     ```json
     {
       "name": "nodejs-functions-gen2-codelab",
       "version": "0.0.1",
       "main": "index.js",
       "dependencies": {
         "@google-cloud/functions-framework": "^2.0.0"
       }
     }
     ```
5. Set the **Entry point** to your function name and deploy it with **1 minimum instance** and **2 maximum instances**.
6. Test the function by sending an HTTP request (e.g., using curl or Postman).

![3](<images/Screenshot 2024-10-17 at 11.28.23.png>)

#### Lessons Learned:

- This task highlighted the trade-off between cold starts and resource allocation. By setting a minimum number of instances, I ensured that my application would respond quickly even during periods of inactivity. This concept is crucial in real-world scenarios where latency and user experience are critical, such as in online services, e-commerce platforms, or API services.

## Final Thoughts

This lab provided a hands-on opportunity to work with Cloud Functions in both event-driven and HTTP-triggered scenarios. I learned how to automate tasks in a cloud environment, deploy functions with scalable configurations, and manage cold start issues—all of which are applicable in real-world cloud development and operations. The ability to trigger functions based on Cloud Storage events and HTTP requests opens up a wide range of possibilities for building serverless applications, improving operational efficiency, and reducing costs.
