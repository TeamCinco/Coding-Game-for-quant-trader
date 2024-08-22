import random

code_snippets = [
    ("import __ as pd", "pandas", "Library for data manipulation and analysis"),
    ("import __ as np", "numpy", "Library for numerical operations"),
    ("import __ as yf", "yfinance", "Library for fetching financial data"),
    ("from scipy import __", "stats", "Module for statistical functions"),
    ("import matplotlib.pyplot as __", "plt", "Library for creating plots"),
    ("from datetime import __, __", "datetime, timedelta", "Classes for working with dates and times"),
    
    ("def fetch_data(stock_symbol, market_symbol, start_date, end_date):", None, "Function definition to fetch stock and market data"),
    ("    data = yf.__(__, __, __, __)", "download, [stock_symbol, market_symbol], start=start_date, end=end_date", "Download historical price data"),
    ("    data = data['__ __']", "Adj Close", "Select adjusted closing prices"),
    ("    log_returns = np.__(data / data.__(1)).__()", "log, shift, dropna", "Calculate log returns and remove NaN values"),
    ("    returns = data.__().__()", "pct_change, dropna", "Calculate percentage returns and remove NaN values"),
    ("    return __", "returns", "Return the calculated returns"),
    
    ("def calculate_beta(stock_returns, market_returns):", None, "Function definition to calculate beta"),
    ("    slope, intercept, r_value, p_value, std_err = stats.__(market_returns, stock_returns)", "linregress", "Perform linear regression"),
    ("    return __", "slope", "Return the slope, which represents beta"),
    
    ("stock_symbol = __(\"Enter the stock symbol: \")", "input", "Get user input for stock symbol"),
    ("market_symbol = input(\"Enter the market index symbol: \") or \"__\"", "^GSPC", "Get market symbol with default S&P 500"),
    
    ("end_date = datetime.____()", "now", "Get current date and time"),
    ("start_date = end_date - timedelta(days=__*365)", "5", "Set start date to 5 years ago"),
    
    ("returns = fetch_data(__, __, __, __)", "stock_symbol, market_symbol, start_date, end_date", "Fetch returns data"),
    
    ("if returns.__:", "empty", "Check if the returns DataFrame is empty"),
    ("    print(\"No data available for the given symbols and date range.\")", None, "Print error message if no data"),
    ("    return", None, "Exit the function if no data"),
    
    ("beta = calculate_beta(returns[__], returns[__])", "stock_symbol, market_symbol", "Calculate beta using stock and market returns"),
    
    ("r_squared = stats.__(returns[market_symbol], returns[stock_symbol])[0]**2", "pearsonr", "Calculate R-squared using Pearson correlation"),
    
    ("print(f\"Beta: {__:.4f}\")", "beta", "Print calculated beta value"),
    ("print(f\"R-squared: {__:.4f}\")", "r_squared", "Print calculated R-squared value"),
    
    ("plt.figure(figsize=(__, __))", "10, 6", "Create a new figure with specified size"),
    ("plt.scatter(returns[__], returns[__], alpha=0.5)", "market_symbol, stock_symbol", "Create scatter plot of returns"),
    
    ("x = np.__(returns[market_symbol])", "array", "Convert market returns to numpy array"),
    ("y = beta * x + stats.linregress(returns[market_symbol], returns[stock_symbol]).__", "intercept", "Calculate y-values for regression line"),
    ("plt.plot(x, y, color='red')", None, "Plot regression line"),
    
    ("plt.xlabel(f'{__} Returns')", "market_symbol", "Set x-axis label"),
    ("plt.ylabel(f'{__} Returns')", "stock_symbol", "Set y-axis label"),
    ("plt.title(f'Beta Calculation: {__} vs {__}')", "stock_symbol, market_symbol", "Set plot title"),
    ("plt.__()", "show", "Display the plot")
]

def run_game():
    print("Welcome to the Quant Code Learning Game!")
    print("Fill in the blanks in the code snippets. Type 'hint' for a hint, or 'quit' to exit.")
    print("The goal is to understand the structure and purpose of each line, not just memorize the code.")
    
    score = 0
    total_questions = 0

    for snippet, answer, hint in code_snippets:
        if answer is None:
            print(f"\nContext: {hint}")
            print(snippet)
            input("Press Enter to continue...")
            continue

        print(f"\nComplete this code snippet:")
        print(snippet)
        print(f"Context: {hint}")

        while True:
            user_input = input("> ").strip()

            if user_input.lower() == 'quit':
                print(f"\nGame over! Final score: {score}/{total_questions}")
                return
            elif user_input.lower() == 'hint':
                print(f"Hint: The answer involves {answer.count(',') + 1} part(s).")
                continue

            total_questions += 1

            if user_input == answer:
                print("Correct!")
                score += 1
                break
            else:
                print(f"Not quite. The correct answer was: {answer}")
                print(f"Explanation: {hint}")
                break
        
        print(f"Current score: {score}/{total_questions}")

    print(f"\nCongratulations! You've completed all questions.")
    print(f"Final score: {score}/{total_questions}")
    if total_questions > 0:
        print(f"Accuracy: {(score/total_questions)*100:.2f}%")

if __name__ == "__main__":
    run_game()