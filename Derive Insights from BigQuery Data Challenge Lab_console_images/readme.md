### **Derive Insights from BigQuery Data: Challenge Lab**

---

### **Overview**

This lab will challenge you to use BigQuery to perform COVID-19-related queries. The tasks focus on identifying key pandemic data insights.

---

### **Task 1: Total Confirmed Cases**

**Query:** The total count of confirmed cases worldwide.

* The query results for the **total_cases_worldwide** output.

![1](images/Screenshot 2024-09-30 at 11.30.49.png)

### **Task 2: Worst Affected Areas**

**Query:** Number of U.S. states with more than a certain number of deaths.

* After showing the output for  **count_of_states**

![2](images/Screenshot 2024-09-30 at 11.31.30.png)

### **Task 3: Identifying Hotspots**

**Query:** List of U.S. states with more than a certain number of confirmed cases.

* After the query displays the **state** and **total_confirmed_cases** in descending order.

![3](images/Screenshot 2024-09-30 at 11.32.41.png)

### **Task 4: Fatality Ratio**

**Query:** Case-fatality ratio for Italy in a specific month.

* After showing the results for  **total_confirmed_cases** ,  **total_deaths** , and  **case_fatality_ratio**

![4](images/Screenshot 2024-09-30 at 11.35.45.png)

### **Task 5: Identifying Specific Day**

**Query:** Date when Italy’s death count crossed a specific threshold.

* After showing the date result in the format  **yyyy-mm-dd** .

![5](images/Screenshot 2024-09-30 at 11.36.43.png)

---

### **Task 6: Finding Days with Zero Net New Cases**

**Updated Query:** Correct the provided query to return the proper output.

* After displaying the correct number of days with zero increases in confirmed cases.

![6](images/Screenshot 2024-09-30 at 11.40.17.png)

### **Task 7: Doubling Rate**

**Query:** Dates in the U.S. where cases increased by more than a certain percentage.

* After showing the list of dates with  **Confirmed_Cases_On_Day** ,  **Confirmed_Cases_Previous_Day** , and  **Percentage_Increase_In_Cases** .

![7](images/Screenshot 2024-09-30 at 11.41.12.png)

### **Task 8: Recovery Rate**

**Query:** List of recovery rates for countries with over 50K confirmed cases.

* After displaying the fields  **country** ,  **recovered_cases** ,  **confirmed_cases** , and  **recovery_rate** .

![8](images/Screenshot 2024-09-30 at 11.47.29.png)

### **Task 9: CDGR (Cumulative Daily Growth Rate)**

**Corrected Query:** Fix the query to calculate France’s CDGR.

* After the query calculates the correct values for France's  **CDGR**

![9](images/Screenshot 2024-09-30 at 11.49.06.png)

### **Task 10: Create a Looker Studio Report**

**Report Requirements:** Plot U.S. confirmed cases and deaths over a date range (***2020-03-22 to 2020-04-20***)

![10](images/Screenshot 2024-09-30 at 11.44.35.png)

* The looker report would look similar to this.

![looker](images/looker.png)
