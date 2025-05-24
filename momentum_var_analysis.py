#####
# HISTORICAL SIMULATION APPROACH 
#####
# Function to calculate Historical VaR
 def historical_var(returns, percentiles):
 return returns.quantile(percentiles)
 # Historical VaR calculations
 percentiles = [0.05, 0.01, 0.10]
 VaR_long_historical = historical_var(long_excess_returns, percentiles)
 VaR_short_historical = historical_var(short_excess_returns,
 percentiles)
 VaR_spread_historical = historical_var(spread_excess_returns,
 percentiles)
 print("Historical VaR (Long Portfolio):", VaR_long_historical.values)
 print("Historical VaR (Short Portfolio):", VaR_short_historical.values)
 print("Historical VaR (Spread Portfolio):",
 VaR_spread_historical.values)

#####
# PARAMETRIC APPROACH 
#####
 # Calculate the mean and standard deviation of excess returns for each portfolio
 mean_long = long_excess_returns.mean()
 std_long = long_excess_returns.std()
 mean_short = short_excess_returns.mean()
 std_short = short_excess_returns.std()
 mean_spread = spread_excess_returns.mean()
 std_spread = spread_excess_returns.std()
 # Function to calculate parametric VaR
def parametric_var(mean, std, percentiles):
 return norm.ppf(percentiles, mean, std)
 # Parametric VaR calculations
 VaR_long_parametric = parametric_var(mean_long, std_long, [0.05, 0.01,
 0.10])
 VaR_short_parametric = parametric_var(mean_short, std_short, [0.05,
 0.01, 0.10])
 VaR_spread_parametric = parametric_var(mean_spread, std_spread, [0.05,
 0.01, 0.10])
 print("Parametric VaR (Long Portfolio):", VaR_long_parametric)
 print("Parametric VaR (Short Portfolio):", VaR_short_parametric)
 print("Parametric VaR (Spread Portfolio):", VaR_spread_parametric)

#####
# MONTE CARLO SIMULATION APPROACH 
#####
 # Define the number of simulations
 n_simulations = 10000
 # Function to calculate Monte Carlo VaR using historical returns
 def monte_carlo_var_from_historical(returns, n_simulations,
 percentiles):
 mean = returns.mean()
 std = returns.std()
 simulated_returns = np.random.normal(mean, std, n_simulations)
 # Use the percentile values directly
 return np.percentile(simulated_returns, percentiles)
 # Monte Carlo VaR calculations
 VaR_long_monte_carlo =
 monte_carlo_var_from_historical(long_excess_returns, n_simulations, [5,
 1, 10])
 VaR_short_monte_carlo =
 monte_carlo_var_from_historical(short_excess_returns, n_simulations,
 [5, 1, 10])
 VaR_spread_monte_carlo =
 monte_carlo_var_from_historical(spread_excess_returns, n_simulations,
 [5, 1, 10])
 # Display the results
 print("Monte Carlo VaR (Long Portfolio):", VaR_long_monte_carlo)
 print("Monte Carlo VaR (Short Portfolio):", VaR_short_monte_carlo)
 print("Monte Carlo VaR (Spread Portfolio):", VaR_spread_monte_carlo)
