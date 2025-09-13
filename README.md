# 📊 Product Feature Performance Dashboard (Power BI)

## 📌 Overview
This project contains a **Power BI dashboard** designed to analyze **product feature performance** for a SaaS platform.  
The report highlights **user engagement, feature adoption, revenue impact, and churn risk** across multiple user segments.  

---

## 🔑 Key Insights & Pages

### 1. Feature Performance
- **Feature adoption trend** (monthly usage growth)  
- **Top features by usage** (ranked list)  
- **Feature success rate vs usage** (scatter plot)  
- **Feature category comparison** (Core, Collaboration, Analytics, Engagement, Mobile, Advanced)  

### 2. User Segmentation
- **User distribution by subscription tier** (Free, Basic, Pro, Enterprise)  
- **User engagement by subscription tier**  
- **Geographic distribution of active users**  
- **Industry and company size usage patterns**  

### 3. Business Impact
- **Revenue correlation with feature usage** (scatter plot)  
- **Churn risk indicators** (Healthy, Low, Medium, High Risk)  
- **Feature ROI analysis** (ROI and payback period per feature)  
- **Lifecycle stage distribution** (New, Active New, Established Active, At Risk, Churned)  

---

## 🛠️ Tech & Tools
- **Power BI Desktop**  
- **DAX measures** for metrics like ROI, churn risk, lifecycle stages, and feature adoption  
- Synthetic dataset includes:
  - `users` → user demographics, signup date, subscription tier  
  - `features` → feature metadata (release date, complexity, category)  
  - `feature_usage` → daily feature interactions (usage count, time spent, success rate)  
  - `business_metrics` → daily revenue, signups, churn, support tickets  

---
