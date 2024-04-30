def calculate_clv(preds, data, MM=1300, r=0.1):
    """
    Calculate Customer Lifetime Value (CLV) for each customer in the DataFrame.

    Parameters:
        - preds (pd.DataFrame): A dataframe of survival function predictions.
        - data (pd.DataFrame): A dataframe of the original dataset, where we want to save results to.
        - MM (float): A constant representing the monetary value.
        - r (float): The periodic interest rate for discounting.

    Returns:
        - pd.Series: Series containing CLV values for each customer.
    """

    # Calculating clv
    sequence = list(range(1, len(preds.columns) + 1))
    # Iterating over each column in data_clv
    for num in sequence:
        # Discount the values in the column based on time-value-of-money calculation
        preds.iloc[:, num - 1] /= (1 + r/12) ** (num - 1)
    # Calculate CLV for each row
    data['CLV'] = MM * preds.sum(axis=1)