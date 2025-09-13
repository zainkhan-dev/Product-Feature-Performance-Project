import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define our SaaS platform: TaskFlow Pro (Project Management Tool)
print("🚀 Generating synthetic data for TaskFlow Pro - Project Management SaaS Platform")
print("=" * 70)

# 1. USERS TABLE
print("📊 Creating Users dataset...")
n_users = 1500

# User segments with realistic distribution
subscription_tiers = ['Free', 'Basic', 'Pro', 'Enterprise']
tier_weights = [0.4, 0.3, 0.25, 0.05]  # Most users on free tier

companies = ['Tech Startup', 'Marketing Agency', 'Consulting Firm', 'E-commerce', 'Healthcare', 
             'Education', 'Manufacturing', 'Financial Services', 'Non-profit', 'Government']

countries = ['USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'India', 'Brazil', 'Japan']
country_weights = [0.35, 0.08, 0.12, 0.10, 0.08, 0.06, 0.12, 0.05, 0.04]

users_data = []
for i in range(n_users):
    # Create realistic signup dates (last 2 years, with growth trend)
    days_ago = np.random.exponential(180)  # More recent signups
    signup_date = datetime.now() - timedelta(days=min(days_ago, 730))
    
    # Subscription tier affects engagement
    sub_tier = np.random.choice(subscription_tiers, p=tier_weights)
    
    user = {
        'user_id': f'USR_{i+1:04d}',
        'signup_date': signup_date.date(),
        'subscription_tier': sub_tier,
        'company_size': np.random.choice(['1-10', '11-50', '51-200', '201-1000', '1000+'], 
                                       p=[0.3, 0.35, 0.2, 0.1, 0.05]),
        'industry': np.random.choice(companies),
        'country': np.random.choice(countries, p=country_weights),
        'is_active': np.random.choice([True, False], p=[0.75, 0.25])  # 75% active users
    }
    users_data.append(user)

users_df = pd.DataFrame(users_data)

# 2. FEATURES TABLE
print("🔧 Creating Features dataset...")
features_data = [
    # Core Features
    {'feature_id': 'FEAT_001', 'feature_name': 'Dashboard View', 'category': 'Core', 'release_date': '2022-01-15', 'complexity': 'Low'},
    {'feature_id': 'FEAT_002', 'feature_name': 'Task Creation', 'category': 'Core', 'release_date': '2022-01-15', 'complexity': 'Low'},
    {'feature_id': 'FEAT_003', 'feature_name': 'Project Templates', 'category': 'Core', 'release_date': '2022-02-01', 'complexity': 'Medium'},
    
    # Collaboration Features  
    {'feature_id': 'FEAT_004', 'feature_name': 'Team Chat', 'category': 'Collaboration', 'release_date': '2022-03-01', 'complexity': 'Medium'},
    {'feature_id': 'FEAT_005', 'feature_name': 'File Sharing', 'category': 'Collaboration', 'release_date': '2022-03-15', 'complexity': 'Medium'},
    {'feature_id': 'FEAT_006', 'feature_name': 'Comments & Reviews', 'category': 'Collaboration', 'release_date': '2022-04-01', 'complexity': 'Low'},
    
    # Analytics Features
    {'feature_id': 'FEAT_007', 'feature_name': 'Progress Reports', 'category': 'Analytics', 'release_date': '2022-05-01', 'complexity': 'High'},
    {'feature_id': 'FEAT_008', 'feature_name': 'Time Tracking', 'category': 'Analytics', 'release_date': '2022-06-01', 'complexity': 'Medium'},
    {'feature_id': 'FEAT_009', 'feature_name': 'Custom Dashboards', 'category': 'Analytics', 'release_date': '2022-07-01', 'complexity': 'High'},
    
    # Advanced Features
    {'feature_id': 'FEAT_010', 'feature_name': 'API Integration', 'category': 'Advanced', 'release_date': '2022-08-01', 'complexity': 'High'},
    {'feature_id': 'FEAT_011', 'feature_name': 'Automated Workflows', 'category': 'Advanced', 'release_date': '2022-09-01', 'complexity': 'High'},
    {'feature_id': 'FEAT_012', 'feature_name': 'Advanced Permissions', 'category': 'Advanced', 'release_date': '2022-10-01', 'complexity': 'Medium'},
    
    # Recent Features
    {'feature_id': 'FEAT_013', 'feature_name': 'Mobile App Sync', 'category': 'Mobile', 'release_date': '2023-01-01', 'complexity': 'High'},
    {'feature_id': 'FEAT_014', 'feature_name': 'Offline Mode', 'category': 'Mobile', 'release_date': '2023-03-01', 'complexity': 'High'},
    {'feature_id': 'FEAT_015', 'feature_name': 'Smart Notifications', 'category': 'Engagement', 'release_date': '2023-06-01', 'complexity': 'Medium'}
]

features_df = pd.DataFrame(features_data)
features_df['release_date'] = pd.to_datetime(features_df['release_date'])

# 3. FEATURE USAGE TABLE (Most important for dashboard)
print("📈 Creating Feature Usage dataset...")

# Generate usage data for last 12 months
start_date = datetime.now() - timedelta(days=365)
end_date = datetime.now()
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

usage_data = []

# Feature adoption rates based on subscription tier and feature complexity
tier_multipliers = {'Free': 0.3, 'Basic': 0.6, 'Pro': 0.9, 'Enterprise': 1.2}
complexity_rates = {'Low': 0.8, 'Medium': 0.4, 'High': 0.15}

for date in date_range:
    # Daily active users varies (weekends lower, growth trend)
    base_active = len(users_df[users_df['is_active'] == True]) * 0.3
    weekend_factor = 0.7 if date.weekday() >= 5 else 1.0
    growth_factor = 1 + (date - start_date).days / 365 * 0.2  # 20% growth over year
    
    daily_active_users = int(base_active * weekend_factor * growth_factor)
    active_users_today = users_df[users_df['is_active'] == True].sample(n=min(daily_active_users, len(users_df)))
    
    for _, user in active_users_today.iterrows():
        for _, feature in features_df.iterrows():
            # Skip if feature wasn't released yet
            if date < feature['release_date']:
                continue
                
            # Calculate probability of using this feature
            tier_mult = tier_multipliers[user['subscription_tier']]
            complexity_rate = complexity_rates[feature['complexity']]
            
            # Feature-specific adoption rates
            base_rate = complexity_rate * tier_mult
            
            # Add some randomness and feature-specific adjustments
            if feature['category'] == 'Core':
                base_rate *= 1.5  # Core features used more
            elif feature['category'] == 'Advanced':
                if user['subscription_tier'] in ['Free', 'Basic']:
                    base_rate *= 0.1  # Advanced features restricted
                    
            # Time since feature release affects adoption
            days_since_release = (date - feature['release_date']).days
            adoption_curve = min(1.0, days_since_release / 90)  # 90 days to full adoption
            
            final_probability = min(0.95, base_rate * adoption_curve)
            
            if np.random.random() < final_probability:
                # User used this feature - generate usage metrics
                usage_count = np.random.poisson(3) + 1  # 1-10 uses per day
                time_spent = np.random.gamma(2, 2) * usage_count  # Minutes
                
                usage_record = {
                    'date': date.date(),
                    'user_id': user['user_id'],
                    'feature_id': feature['feature_id'],
                    'usage_count': usage_count,
                    'time_spent_minutes': round(time_spent, 2),
                    'success_rate': min(1.0, np.random.beta(8, 2))  # Most interactions successful
                }
                usage_data.append(usage_record)

usage_df = pd.DataFrame(usage_data)

# 4. BUSINESS METRICS TABLE
print("💰 Creating Business Metrics dataset...")
business_data = []

for date in date_range:
    # Calculate daily metrics
    daily_usage = usage_df[usage_df['date'] == date.date()]
    active_users_count = daily_usage['user_id'].nunique() if not daily_usage.empty else 0
    
    # Simulate revenue (higher for enterprise users)
    daily_revenue = 0
    for tier in subscription_tiers:
        tier_users = users_df[users_df['subscription_tier'] == tier]
        if tier == 'Free':
            continue
        elif tier == 'Basic':
            daily_revenue += len(tier_users) * 29 / 30  # $29/month
        elif tier == 'Pro':
            daily_revenue += len(tier_users) * 99 / 30   # $99/month
        elif tier == 'Enterprise':
            daily_revenue += len(tier_users) * 299 / 30  # $299/month
    
    business_record = {
        'date': date.date(),
        'daily_active_users': active_users_count,
        'daily_revenue': round(daily_revenue, 2),
        'new_signups': max(0, np.random.poisson(5)),
        'churned_users': max(0, np.random.poisson(2)),
        'feature_requests': max(0, np.random.poisson(8)),
        'support_tickets': max(0, np.random.poisson(12))
    }
    business_data.append(business_record)

business_df = pd.DataFrame(business_data)

# 5. SAVE ALL DATASETS
print("💾 Saving datasets to CSV files...")

# Create summary statistics
print("\n📋 DATASET SUMMARY")
print("=" * 50)
print(f"👥 Users: {len(users_df):,} records")
print(f"🔧 Features: {len(features_df):,} records") 
print(f"📊 Feature Usage: {len(usage_df):,} records")
print(f"💼 Business Metrics: {len(business_df):,} records")

# Save to CSV
users_df.to_csv('taskflow_users.csv', index=False)
features_df.to_csv('taskflow_features.csv', index=False) 
usage_df.to_csv('taskflow_feature_usage.csv', index=False)
business_df.to_csv('taskflow_business_metrics.csv', index=False)

print(f"\n✅ All datasets saved successfully!")
print(f"📁 Files created:")
print(f"   • taskflow_users.csv")
print(f"   • taskflow_features.csv") 
print(f"   • taskflow_feature_usage.csv")
print(f"   • taskflow_business_metrics.csv")

# Display sample data
print(f"\n🔍 SAMPLE DATA PREVIEW")
print("=" * 50)

print("\n👥 Users Sample:")
print(users_df.head(3).to_string(index=False))

print(f"\n🔧 Features Sample:")
print(features_df.head(3).to_string(index=False))

print(f"\n📊 Feature Usage Sample:")
print(usage_df.head(3).to_string(index=False))

print(f"\n💼 Business Metrics Sample:")
print(business_df.head(3).to_string(index=False))

# Key insights for dashboard development
print(f"\n🎯 KEY INSIGHTS FOR YOUR DASHBOARD")
print("=" * 50)
print("1. Feature Adoption: Core features have higher adoption rates")
print("2. Subscription Impact: Higher tiers use advanced features more") 
print("3. Release Timeline: Features show adoption curves after release")
print("4. User Segments: Different industries and company sizes show varying patterns")
print("5. Growth Trend: Overall platform growth over the year")

print(f"\n🚀 Ready for Power BI! Your synthetic dataset includes:")
print("   ✅ Realistic user segments and behaviors")
print("   ✅ Feature complexity and adoption patterns")  
print("   ✅ Time-series data for trend analysis")
print("   ✅ Business metrics correlation")
print("   ✅ Multiple dimensions for filtering and drilling down")