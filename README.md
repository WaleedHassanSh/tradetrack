# TradeTrack

#### Video Demo: https://youtu.be/-YzMhaj9vw0

#### Description:

TradeTrack is a command-line trading journal and performance analysis program written in Python. The purpose of the project is to help a trader record completed trades, save them in a CSV file, and review basic performance statistics such as total trades, winning trades, losing trades, win rate, total profit or loss, and average R-multiple.

I built this project because trading is not only about finding entries and exits, but also about tracking decisions, reviewing mistakes, and measuring performance over time. Many beginner traders focus only on whether a trade won or lost, but a better trading journal should also record risk, strategy, mistake tags, and notes. TradeTrack is designed to be simple, practical, and easy to run from the terminal.

When the program starts, it displays a small menu with two options. The first option allows the user to add a new trade. The program asks for the trade symbol, side, entry price, exit price, stop loss, position size, strategy, mistake tag, and notes. It automatically records the current date using Python's datetime module. After collecting the trade details, the program calculates the trade's profit or loss and R-multiple, then saves the full trade record into trades.csv.

The second option allows the user to view a performance summary. The program loads all saved trades from the CSV file, converts numeric values back into floats, and calculates summary statistics. These statistics include the total number of trades, number of winning trades, number of losing trades, win rate percentage, total profit/loss, and average R-multiple. If no trade file exists yet, the program handles that case safely and returns an empty summary instead of crashing.

The main file of the project is project.py. It contains the main() function, which controls the menu, and several helper functions. The add_trade() function handles the process of getting a trade, calculating its performance values, and saving it to the CSV file. The get_trade() function collects user input and returns a dictionary representing one trade. The calculate_profit_loss() function calculates profit or loss differently depending on whether the trade is long or short. The calculate_r_multiple() function calculates reward divided by risk and validates that the stop loss creates a valid risk amount. The load_trades() function reads saved trades from trades.csv, and summarize_trades() calculates the summary statistics. The print_summary() function displays the final summary in a clean format.

The test_project.py file contains pytest tests for the main calculation and summary functions. I tested calculate_profit_loss(), calculate_r_multiple(), and summarize_trades() because these functions contain the most important logic and do not depend on user input. The tests check long trades, short trades, losing trades, invalid trade sides, invalid stop losses, normal summaries, and empty summaries.

I chose CSV as the storage format because it is simple, readable, and suitable for a beginner-level Python project. It also allows the trade journal to be opened later in spreadsheet software if needed. I chose a command-line interface instead of a graphical interface because the goal of this project is to focus on Python fundamentals, file handling, functions, error handling, testing, and clean program structure.

One design choice I made was to calculate profit/loss and R-multiple automatically instead of asking the user to enter them manually. This reduces user error and makes the journal more useful. Another design choice was to use dictionaries for trades because each trade has clearly named fields such as symbol, entry, exit_price, stop_loss, and profit_loss.

This project does not provide trading signals, financial advice, or market predictions. It is only a journaling and analysis tool for trades that the user has already taken. In the future, this project could be improved by adding features such as listing all trades, exporting a Markdown report, filtering trades by symbol or strategy, showing the most common mistake tag, and creating charts from the saved trading data.

To run the program, use:

    python project.py

To run the tests, use:

    pytest test_project.py

The project uses Python's standard libraries, including csv and datetime. The tests use pytest.
