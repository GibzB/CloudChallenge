# Analyzing Security Findings with Google Cloud's Security Command Center: A Simple Guide for Tech Enthusiasts

Welcome, young tech enthusiasts! Today, we're diving into the world of  **Google Cloud Security Command Center (SCC)** . If you’re curious about how companies like Cymbal Bank keep their data safe in the cloud, this is the place to start.

Google Cloud Security Command Center is a platform that helps businesses like Cymbal Bank monitor their systems for security issues, vulnerabilities, and potential threats. It allows them to find problems, fix them, and keep their cloud systems running safely.

In this tutorial, we’ll explore **how Security Command Center works** and show you how to export and analyze security findings with tools like **Pub/Sub** and  **BigQuery** .

Let’s break it down into simple steps so that even a four-year-old tech enthusiast can follow along!

## What is Security Command Center (SCC)?

Imagine you have a superhero team looking after your house, making sure everything is safe. Well, **Security Command Center** is like a superhero team for your cloud systems! It watches over everything, makes sure no bad guys (threats) get in, and helps you fix things if something goes wrong.

Here’s what SCC can do:

1. **Discover Problems:** It helps find misconfigurations or security problems in your cloud systems.
2. **Report Threats:** It tells you when something dangerous is happening in your cloud environment.
3. **Fix Issues:** It helps you patch up vulnerabilities and protect your data from attacks.

## Scenario: Cymbal Bank and the Cloud Security Engineer

Let’s imagine a company called  **Cymbal Bank** . They’re a big bank in the U.S. that helps people manage their money. They have lots of data in the cloud, and they want to make sure it’s secure.

Your job as a **Cloud Security Engineer** is to help Cymbal Bank use Security Command Center to keep their data safe. To do that, you’ll learn how to:

* **Export security findings to Pub/Sub** , a tool for sending messages.
* **Export findings to BigQuery** to analyze data and find patterns.

## Task 1: Creating a Continuous Export Pipeline to Pub/Sub

### What is Pub/Sub?

**Pub/Sub** is like a digital post office where messages can be sent and received. If Security Command Center finds a problem (like a vulnerability), it can send that message to Pub/Sub. From there, it can go to other security systems that are looking for problems.

### Step-by-Step: Setting Up Pub/Sub

1. **Create a Pub/Sub Topic:**
   * Imagine a topic as a mailbox. First, you need to create a mailbox (called a  **topic** ) where Security Command Center will send messages.
   * In Google Cloud Console, search for **Pub/Sub** and click  **Create Topic** .
   * Name your topic  **export-findings-pubsub-topic** .
2. **Create a Subscription:**
   * A **subscription** is like a friend who’s always checking the mailbox to read the messages.
   * You’ll create a subscription so you can pull messages (security findings) from the topic.
3. **Configure Continuous Exports:**
   * Now, connect Security Command Center to the topic. Go to the **Security** section in Google Cloud Console and click on  **Risk Overview** .
   * Click **Settings** and then  **Continuous Exports** .
   * Select the Pub/Sub topic you created earlier, so that SCC will start sending messages to Pub/Sub whenever a new problem is found.
4. **Create New Findings:**
   * You can simulate a problem by creating a new virtual machine (VM) in the cloud. This will generate security findings (like “This machine has a public IP address”).
   * These findings will automatically be sent to Pub/Sub, where they can be picked up and analyzed by other systems.

## Task 2: Export and Analyze Findings with BigQuery

### What is BigQuery?

**BigQuery** is like a giant notebook where you can store lots of data and then ask it questions (queries). In this task, we’ll export findings from Security Command Center and use BigQuery to look for patterns or problems.

### Step-by-Step: Using BigQuery for Analysis

1. **Create a BigQuery Dataset:**
   * In your Cloud Shell (a special terminal), you’ll create a place to store your data by setting up a  **dataset** .
   * Run some commands to set up a new BigQuery dataset, which will hold your security findings.
2. **Export Findings to BigQuery:**
   * After you’ve created the dataset, you’ll export the security findings (problems found by SCC) to BigQuery.
   * This is done by configuring the export to send findings into a  **BigQuery table** . When new findings are generated, they will show up in your BigQuery table.
3. **Analyze the Data:**
   * Once the findings are in BigQuery, you can ask questions like: “What security problems happen the most?” or “Are there certain types of problems that happen in specific areas of our cloud?”
   * You can run queries to explore the data and find out where improvements need to be made.

## Task 3: Export Findings to Cloud Storage and BigQuery

Sometimes, you want to keep your findings in a **Cloud Storage bucket** (another type of storage in Google Cloud) before moving them to BigQuery. This allows you to first store all your data and then analyze it.

### Step-by-Step: Exporting to Cloud Storage and BigQuery

1. **Create a Cloud Storage Bucket:**
   * In Google Cloud Console, create a new  **Cloud Storage bucket** . This is like a digital box where you can store things before moving them to BigQuery.
   * Name the bucket something like `scc-export-bucket-<your-name>`.
2. **Export Findings to Cloud Storage:**
   * Go to the **Security Findings** page in the Google Cloud Console and export your findings to the Cloud Storage bucket you just created.
   * Make sure to choose **JSONL** as the format, which is a special way to save the data.
3. **Create a BigQuery Table:**
   * Once your findings are in Cloud Storage, you can create a new **BigQuery table** to hold and analyze the data.
   * Link your Cloud Storage bucket to BigQuery and create the table, where you can then look at all the findings that were exported.

## Why is This Important?

Now that you know how to **export security findings** to Pub/Sub and BigQuery, let’s talk about why it matters:

* **Continuous Monitoring:** By setting up continuous exports, you can always know when a new problem occurs in your cloud systems.
* **Quick Action:** Exporting findings to Pub/Sub helps quickly send security issues to other monitoring tools, so they can be fixed fast.
* **Smart Analysis:** Using BigQuery to analyze security findings allows you to look at trends and make smart decisions about where to improve your systems.

For Cymbal Bank, using these tools means they can always stay one step ahead in keeping their customer data safe.

## Conclusion

Today, you’ve learned how to use **Security Command Center** to monitor and export security findings. Whether you’re sending them to **Pub/Sub** for quick action or to **BigQuery** for deeper analysis, you now understand how these tools can help companies like Cymbal Bank stay safe in the cloud.

Remember, just like how you use tools to keep your toys or data organized, security tools help keep important information safe. Keep learning and exploring — you’re well on your way to becoming a cloud security superhero! 🦸‍♂️🦸‍♀️
