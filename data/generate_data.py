import pandas as pd
import numpy as np
import datetime

# Set seed for reproducibility
np.random.seed(42)

# Configuration
n_total = 10000
n_control = 5000
n_treatment = 5000

mobile_pct = 0.56
desktop_pct = 0.44

# Group Sample Sizes
n_ctrl_mobile = int(n_control * mobile_pct)      # 2800
n_ctrl_desktop = int(n_control * desktop_pct)    # 2200
n_treat_mobile = int(n_treatment * mobile_pct)   # 2800
n_treat_desktop = int(n_treatment * desktop_pct) # 2200

# Exact Conversion Counts
c_ctrl_mobile = 237      # CR ~ 8.46%
c_ctrl_desktop = 257     # CR ~ 11.68%
c_treat_mobile = 239     # CR ~ 8.54%
c_treat_desktop = 370    # CR ~ 16.82%

# Exact Return Counts (among converted users)
r_ctrl_mobile_conv = 20  # Out of 237 converted
r_ctrl_desktop_conv = 22 # Out of 257 converted
# Total Control returns = 42 out of 494 conversions (~8.50%)

r_treat_mobile_conv = 21  # Out of 239 converted
r_treat_desktop_conv = 49 # Out of 370 converted
# Total Treatment returns = 70 out of 609 conversions (~11.49%)

# Create user cohorts
def generate_cohort(group, device, n_users, n_converted, n_returned):
    # Converted status
    converted = np.zeros(n_users, dtype=int)
    converted[:n_converted] = 1
    
    # Returned status
    returned = np.zeros(n_users, dtype=int)
    # Returns only occur for converted users
    returned[:n_returned] = 1
    
    # Shuffle converted and returned together to keep returns mapped to conversions
    idx_conv = np.where(converted == 1)[0]
    idx_non_conv = np.where(converted == 0)[0]
    
    # Shuffle returns within converted indices
    np.random.shuffle(idx_conv)
    returned_mask = np.zeros(n_users, dtype=int)
    returned_mask[idx_conv[:n_returned]] = 1
    
    # Shuffle all users to randomize the row order
    all_indices = np.arange(n_users)
    np.random.shuffle(all_indices)
    
    # Session duration (in seconds, log-normal)
    durations = np.zeros(n_users)
    for i in range(n_users):
        if group == 'control':
            mu, sigma = 4.5, 0.45 # mean ~ 99.5 seconds
        else: # treatment
            if device == 'desktop':
                mu, sigma = 4.62, 0.40 # mean ~ 110 seconds (interacting with nudge)
            else:
                mu, sigma = 4.5, 0.45 # mean ~ 99.5 seconds (mobile treatment - no effect)
        durations[i] = round(np.random.lognormal(mu, sigma), 1)
        
    # User type (60% new, 40% returning)
    user_types = np.random.choice(['new', 'returning'], size=n_users, p=[0.60, 0.40])
    
    # Create DataFrame
    df = pd.DataFrame({
        'group': group,
        'device': device,
        'converted': converted,
        'returned': returned_mask,
        'session_duration': durations,
        'user_type': user_types
    })
    
    return df

# Generate each segment
df_ctrl_mob = generate_cohort('control', 'mobile', n_ctrl_mobile, c_ctrl_mobile, r_ctrl_mobile_conv)
df_ctrl_desk = generate_cohort('control', 'desktop', n_ctrl_desktop, c_ctrl_desktop, r_ctrl_desktop_conv)
df_treat_mob = generate_cohort('treatment', 'mobile', n_treat_mobile, c_treat_mobile, r_treat_mobile_conv)
df_treat_desk = generate_cohort('treatment', 'desktop', n_treat_desktop, c_treat_desktop, r_treat_desktop_conv)

# Combine all cohorts
df = pd.concat([df_ctrl_mob, df_ctrl_desk, df_treat_mob, df_treat_desk], ignore_index=True)

# Generate timestamps over a 14-day period with traffic seasonality
start_date = datetime.datetime(2026, 6, 8, 0, 0, 0)
days = 14

day_weights = [
    1.0,  # Mon
    1.1,  # Tue
    1.15, # Wed
    1.05, # Thu
    0.95, # Fri
    0.7,  # Sat
    0.8,  # Sun
    1.0,  # Mon
    1.1,  # Tue
    1.15, # Wed
    1.05, # Thu
    0.95, # Fri
    0.7,  # Sat
    0.8   # Sun
]
day_probs = np.array(day_weights) / sum(day_weights)

assigned_days = np.random.choice(np.arange(days), size=len(df), p=day_probs)

timestamps = []
for d in assigned_days:
    # Beta distribution peak for afternoon/evening (around 7 PM)
    hour = int(np.random.beta(5, 2) * 24)
    minute = np.random.randint(0, 60)
    second = np.random.randint(0, 60)
    
    dt = start_date + datetime.timedelta(days=int(d), hours=hour, minutes=minute, seconds=second)
    timestamps.append(dt)

df['timestamp'] = timestamps

# Generate unique user_ids
user_ids = [f"USR_{i:05d}" for i in range(1, len(df) + 1)]
df['user_id'] = user_ids

# Shuffle the final dataframe completely
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Reorder columns
df = df[['user_id', 'timestamp', 'group', 'device', 'user_type', 'converted', 'returned', 'session_duration']]

# Write to CSV
df.to_csv('ab_test_data.csv', index=False)
print("Data generation complete! Saved as 'ab_test_data.csv'.")

# Quick print of summaries to verify math
print(f"Total Rows: {len(df)}")
print(df.groupby(['group', 'device'])['converted'].agg(['count', 'sum', 'mean']))
print("Overall converted:")
print(df.groupby('group')['converted'].agg(['count', 'sum', 'mean']))
print("Overall returned among converted:")
print(df[df['converted'] == 1].groupby('group')['returned'].agg(['count', 'sum', 'mean']))
