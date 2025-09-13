# 📊 Business Impact Dashboard (Power BI)

## 📌 Overview
This project contains a **Power BI dashboard** that analyzes the **business impact of feature usage**.  
It provides insights into **revenue correlation, churn risk, ROI analysis, and user lifecycle distribution**.  

The report is designed for **decision-makers and product teams** to track how user behavior and feature adoption influence revenue and retention.  

---

## 🔑 Key Pages & Insights

### 1. Revenue Correlation with Feature Usage
- Scatter plot showing relationship between **feature usage** and **revenue**  
- Helps identify high-revenue driving features  

### 2. Churn Risk Indicators 
- Churn risk segmented into **Healthy, Low, Medium, High Risk**  

### 3. Feature ROI Analysis
- Bar chart of **ROI by feature**  
- Payback period and cost-to-benefit comparisons  

### 4. User Lifecycle Stage Distribution
- Donut chart showing users across stages:  
  - *New User, Active New, Established Active, At Risk, Churned, Dormant*  
- Segmented further by **subscription tier**  

---

## 🛠️ Tech & Tools
- **Power BI Desktop**  
- **DAX Measures** for custom metrics (ROI, churn risk, lifecycle stages, stickiness)  
- **Data Model includes**:  
  - `taskflow_users` → user data with signup date & subscription tier  
  - `taskflow_feature_usage` → feature interactions, usage count, time spent  
  - `taskflow_features` → feature metadata with complexity & category  
  - `taskflow_business_metrics` → daily revenue, financial KPIs  

---

## 📂 Repository Structure
