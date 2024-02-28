import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("Data/Advertising.csv")
# Collect individual model outputs
results_dict = {}
# Perform Simple Linear Regression for each feature individually
for feature in ['TV', 'radio', 'newspaper']:
    X = df[[feature]]
    y = df['sales']

    # Add a constant to the features matrix for the intercept term
    X = sm.add_constant(X)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = sm.OLS(y_train, X_train)

    # Train the model
    results = model.fit()

    # Make predictions on the test set
    y_pred = results.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error for {feature}: {mse}')

    # Get the summary of the model
    print(results.summary())
    results_dict[feature] = results

    # Plot the results
    fig, ax = plt.subplots()
    ax.scatter(X_test[feature], y_test, label='Actual')
    ax.plot(X_test[feature], y_pred, color='red', label='Predicted')
    ax.set_xlabel(feature)
    ax.set_ylabel('Sales')
    ax.set_title(f'Simple Linear Regression for {feature}')
    ax.legend()
    plt.show()
    
# Combine the individual predictions for budget allocation
total_budget = 1000
budget_allocation = {}

# Calculate the denominator for normalization
denominator = sum(result.params[1] for result in results_dict.values())

for feature, result in results_dict.items():
    # Calculate the budget allocation based on the coefficient
    allocation = total_budget * (result.params[1] / denominator)
    budget_allocation[feature] = allocation

# Print the budget allocation
print("Budget Allocation:")
for channel, allocation in budget_allocation.items():
    print(f"{channel}: ${allocation:.2f}")


# Plot the results
fig, ax = plt.subplots()
ax.bar(budget_allocation.keys(), budget_allocation.values())
ax.set_ylabel('Budget Allocation ($)')
ax.set_title('Budget Allocation for Advertisement Channels')
plt.show()

# Define features (X) and target variable (y)
X = df[['TV', 'radio', 'newspaper']]
y = df['sales']

# Add a constant to the features matrix for the intercept term
X = sm.add_constant(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = sm.OLS(y_train, X_train)

# Train the model
results = model.fit()

# Make predictions on the test set
y_pred = results.predict(X_test)


# Get the summary of the model
print(results.summary())

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')


# Budget Allocation Calculation
total_budget = 1000
budget_allocation = (total_budget * results.params[1:]) / results.params[1:].sum()

# Print the budget allocation
print("Budget Allocation:")
for channel, allocation in zip(['TV', 'radio', 'newspaper'], budget_allocation):
    print(f"{channel}: ${allocation:.2f}")

# Plot the results
fig, ax = plt.subplots()
ax.bar(['TV', 'radio', 'newspaper'], budget_allocation)
ax.set_ylabel('Budget Allocation ($)')
ax.set_title('Budget Allocation for Advertisement Channels')
plt.show()