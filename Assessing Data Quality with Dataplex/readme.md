# Assessing Data Quality with Dataplex Lab

## **Overview**

In this lab, I used Google Cloud's Dataplex to assess the data quality of BigQuery tables. Dataplex enables centralized discovery, management, monitoring, and governance of data across various environments like data lakes, data warehouses, and marts. I created Dataplex resources such as lakes, zones, and assets, defined data quality rules via a YAML specification file, and ran a data quality job to validate the data. The results were stored in BigQuery for review.

## **Steps**

### **Task 1: Create a Lake, Zone, and Asset in Dataplex**

In this task, I set up foundational resources in Dataplex:

1. **Create a Lake** :

* Navigate to  **Dataplex > Manage Lakes** .
* Create a new lake with the name `Ecommerce Lake`.
* The lake takes  ~3 minutes to be created.

![1](<images/Screenshot 2024-10-06 at 12.43.12.png>)

1. **Add a Zone** :

* Inside the lake, add a zone named `Customer Contact Raw Zone`, selecting **Raw zone** type.
* Ensure **Metadata discovery** is enabled.

![2](<images/Screenshot 2024-10-06 at 12.46.08.png>)

1. **Attach an Asset** :

* In the zone, attach the **BigQuery dataset (customers)** asset.

![3](<images/Screenshot 2024-10-06 at 12.48.39.png>)

---

### **Task 2: Query BigQuery Table to Review Data Quality**

We explored the **contact_info** table in BigQuery to identify potential data quality issues.

1. **Run the Query** :

* Navigate to  **BigQuery > SQL Workspace** .
* Run the query to fetch 50 records from the **contact_info** table.
* Identify any data quality issues such as missing customer IDs or invalid emails.

 
 ![4](<images/Screenshot 2024-10-06 at 13.08.46.png>)

---

### **Task 3: Create and Upload a Data Quality Specification File**

We defined data quality rules using a  **CloudDQ YAML specification file** .

1. **Create the YAML File** :

* In  **Cloud Shell** , create a YAML file that specifies `NOT_NULL` (customer IDs) and `VALID_EMAIL` (email addresses) rules.
* Bind these rules to the respective columns in the **contact_info** table.

1. **Upload the YAML File** :

* Upload the file to a pre-created **Cloud Storage** bucket.

  **Checkpoint 5 Screenshot** : Screenshot of Cloud Shell showing successful YAML file upload to Cloud Storage.

---

### **Task 4: Define and Run a Data Quality Job in Dataplex**

In this task, I created and executed a data quality job based on the uploaded YAML file.

1. **Create the Data Quality Job** :

* In  **Dataplex** , navigate to the **Process** section and create a new data quality task.
* Select the YAML file and **customers_dq_dataset** to store the results.

  **Checkpoint 6 Screenshot** : Screenshot showing the data quality job being created and its status after completion.

---

### **Task 5: Review Data Quality Results in BigQuery**

In this task, I reviewed the data quality results by querying the **dq_summary** table in BigQuery.

1. **View Data Quality Results** :

* Navigate to  **BigQuery > SQL Workspace** .
* Review the **dq_summary** table and run queries to identify records with invalid emails and missing customer IDs.

  **Checkpoint 7 Screenshot** :
* Screenshot of the **dq_summary** table preview.
* Screenshot of the query results showing invalid email addresses.
* Screenshot of the query results showing records missing customer IDs.

---

## **Lessons Learned from Assessing Data Quality with Dataplex**

### 1. **Importance of Data Lakes in Centralized Data Management**

* Dataplex lakes serve as centralized storage for data assets, facilitating efficient data governance. In real-world scenarios, businesses deal with diverse data sources; using a data lake ensures streamlined data management and quality control.

### 2. **Understanding the Role of Data Quality**

* Ensuring data quality is essential for accurate decision-making. This lab highlighted the importance of defining data quality checks to catch issues like null values or invalid emails. Real-world organizations rely on high-quality data to avoid costly mistakes and improve operational efficiency.

### 3. **YAML Specification for Data Quality**

* Defining data quality rules via YAML files is a flexible and customizable approach. Organizations can easily adapt data quality checks to fit their unique business needs, such as validating customer or patient data to avoid incorrect service delivery.

### 4. **Automating Data Quality Tasks**

* Automating data quality checks ensures continuous validation of data pipelines, helping organizations maintain data integrity without manual intervention. This is particularly useful in environments with frequent data ingestion, such as e-commerce or finance.

### 5. **Real-Time Monitoring and Insights**

* The ability to quickly identify and address data quality issues is crucial for businesses operating in real-time data environments. Real-time feedback helps prevent issues from affecting operational processes in industries like finance, healthcare, and supply chain management.

### 6. **Data Governance and Compliance**

* Data quality reports generated by Dataplex help ensure compliance with regulatory standards like GDPR or HIPAA. Maintaining high-quality data reduces risks of non-compliance and enhances trust in the data used for analytics and reporting.

---

## **Real-World Application**

### **E-commerce** :

* Dataplex helps ensure accurate customer contact information, reducing the risk of failed marketing campaigns and improving customer engagement.

### **Healthcare** :

* Accurate patient records prevent treatment errors, reduce billing mistakes, and ensure compliance with regulations.

### **Finance** :

* Monitoring transaction data quality enhances reporting accuracy, mitigates fraud, and improves decision-making processes.

---

## **Conclusion**

By using Dataplex, businesses can enhance their data quality management processes, centralize governance, and automate data quality checks. This ensures reliable data across various industries, enabling better decision-making and compliance with regulations.
