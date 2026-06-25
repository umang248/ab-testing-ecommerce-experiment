# E-commerce Urgency Nudge A/B Test Analysis

This repository contains a comprehensive, end-to-end A/B testing analysis for an e-commerce checkout flow. The experiment evaluates the impact of adding an urgency nudge (**"Only 3 left in stock!"**) on the product detail page.

##  Business Scenario
* **Core Question:** Does adding a scarcity-driven urgency nudge increase purchase conversion rates, and does it introduce negative trade-offs?
* **Experimental Groups:**
  * **Control (5,000 users):** Standard product detail page layout.
  * **Treatment (5,000 users):** Product detail page with the urgency nudge displayed.
* **Key Demographics:** 56% Mobile traffic, 44% Desktop traffic.

---

## Dataset

The dataset was synthetically generated to mimic a real e-commerce A/B test based on industry benchmarks (2-3% typical lift, ~10% base conversion rate)

Variables include:
- User ID
- Experiment Group
- Device Type
- Conversion Status
- Session Duration
- Return Indicator
- User Type
- Timestamp

Synthetic data was used to demonstrate experimentation methodology while avoiding privacy concerns.

---

##  Key Features

This project walks through the complete lifecycle of A/B test analysis, organized into 7 distinct sections in a Jupyter Notebook:

**0. Setup:** Environmental configuration, importing dependencies (`scipy`, `statsmodels`, `seaborn`, `pandas`), and loading datasets.   
**1. Experiment Design:** Pre-test power analysis to calculate the required sample size and post-hoc power calculations.   
**2. EDA & Sanity Checks:** 
   * **Sample Ratio Mismatch (SRM)** testing using Chi-Square Goodness-of-Fit.
   * Data quality verification.
   * Daily traffic trends and daily conversion rates checks to rule out **novelty effects**.
  
**3. Core Analysis:** Conversion rate metrics, **Two-Proportion Z-test**, Confidence Intervals, **Cohen's h** effect size calculation, and a **10,000-resample vectorized bootstrap simulation** to visualize lift probability.   
**4. Guardrail Metrics:** Analyzing the impact on **Return Rates** (impulse buying side-effects) and overall **Session Durations** (t-test).  
**5. Segmentation:** Drilling down performance by **Device Type** (Desktop vs. Mobile) and **User Type** (New vs. Returning) to uncover divergent behaviors. **6. Results Summary:** A centralized summary table aggregating all computed statistics.   


---

##  Summary of Results

All statistics are generated dynamically from the experiment dataset:

| Segment / Metric | Control Size | Treatment Size | Control Metric | Treatment Metric | Absolute Lift | P-value | Stat. Sig (alpha=5%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Overall Conversion** | 5,000 | 5,000 | 9.88% | 12.18% | +2.30% | 0.0002 | **Yes** |
| **Desktop Conversion** | 2,200 | 2,200 | 11.68% | 16.82% | +5.14% | 0.0000 | **Yes** |
| **Mobile Conversion** | 2,800 | 2,800 | 8.46% | 8.54% | +0.07% | 0.9237 | **No** |
| **Return Rate (Purchasers)** | 494 | 609 | 8.50% | 11.49% | +2.99% | 0.1018 | **No (Directional)** |
| **Session Duration (s)** | 5,000 | 5,000 | 100.35s | 104.40s | +4.04s | 1.6605e-05 | **Yes** |

---

##  Key Strategic Recommendations (From PM Decision Memo)

* **Ship to Desktop (100% Rollout):** Conversion rates significantly increased by **+5.14%** (relative lift of **+44.0%**, p < 0.0001). For 1,000,000 annual desktop sessions (AOV = $50.00, Return cost = $10.00), this rollout yields an estimated **+$1,831,818.18** in annual net revenue.
* **Keep Control on Mobile (0% Rollout):** The conversion lift was flat (**+0.07%**, p = 0.92). Adding a banner on restricted viewports likely pushed critical checkout elements below the fold, canceling out any psychological urgency boost.
* **Monitor Return Rates:** The return rate rose directionally from **8.50%** to **11.49%** (p = 0.1018), showing signs of increased impulse purchasing. Post-rollout return rate alerts should be configured in production.

---

##  Setup & Execution

### 1. Clone the repository
```bash
git clone https://github.com/umang248/ab-testing-ecommerce-experiment.git
cd ab-testing-ecommerce-experiment
```

### 2. Install Dependencies
Ensure you have Python 3.10+ installed. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels notebook
```

### 3. Generate the Data
If you want to regenerate the dataset from scratch, run the scripts:
```bash
python generate_data.py
```

### 4. Run the Jupyter Notebook
Start the Jupyter Notebook server:
```bash
jupyter notebook ab_testing_analysis.ipynb
```
Or open the notebook file inside your preferred IDE (e.g. VS Code, PyCharm) equipped with a Jupyter extension.
