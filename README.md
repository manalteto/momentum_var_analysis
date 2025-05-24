# Value at Risk (VaR) Analysis of a Momentum Strategy

This project extends a previously developed momentum-based portfolio by estimating the Value at Risk (VaR) using three different methodologies. It evaluates the risk of a long-short strategy and compares it with a long-only approach, providing insight into the strategy's downside risk profile.

## Objectives

- Estimate VaR for a momentum strategy using three models
- Analyze the impact of different estimation periods on VaR
- Compare long-short vs. long-only momentum risk
- Provide interpretation and recommendations for risk management decisions

## Methodologies Used

- Historical Simulation
- Parametric (Variance-Covariance)
- Monte Carlo Simulation

## Tools & Data

- Python
- `pandas`, `numpy`, `matplotlib`, `scipy`, `statsmodels`
- Data sourced from CRSP and Kenneth French Data Library

## Interpretation & Risk Insights

### 1. Model Assumptions

- **Historical Simulation:** Assumes past market conditions will repeat. Does not assume a specific return distribution.
- **Parametric Method:** Assumes normally distributed returns. Relies on mean and standard deviation.
- **Monte Carlo Simulation:** Simulates returns from a statistical model (e.g., normal distribution). Flexible but model-dependent.

### 2. Result Interpretation

- VaR quantifies the maximum expected loss at a given confidence level (e.g., 5%, 1%).
- **Long Portfolio** has the highest risk.
- **Short Portfolio** shows the lowest risk.
- **Spread Portfolio** offers balanced risk, combining both long and short positions.

### 3. Sensitivity to Estimation Period

VaR results are sensitive to the estimation window:
- **Longer periods** capture more extreme events → higher VaR.
- **Shorter periods** may underestimate risk.
- Historical method is especially impacted.

### 4. Recommended VaR for Risk Management

The **5% Monte Carlo VaR for the Spread Portfolio** (~ -10.77%) is the most balanced and robust estimate:
- Captures a broad range of potential outcomes
- Does not rely on restrictive normality assumptions
- Offers a realistic and risk-aware perspective suitable for reporting

### 5. Long-Only vs. Long-Short Comparison

- **Long-Only Portfolio:** Higher VaR, indicating greater standalone risk.
- **Long-Short (Spread) Portfolio:** Lower VaR due to risk diversification.
- Conclusion: Long-short strategies may offer better downside protection than long-only momentum portfolios.


