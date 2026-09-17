# TradeTrack

TradeTrack is a command-line trading journal and performance analysis tool built with Python.

It allows users to record completed trades in a CSV file and review basic performance statistics such as total trades, winning and losing trades, win rate, total profit/loss, and average R-multiple.

This project was originally built as my final project for **Harvard's CS50's Introduction to Programming with Python (CS50P)** and represents the main project from the Python programming phase of my CS/AI/ML learning roadmap.

## Demo

Video demonstration:

[Watch the TradeTrack demo on YouTube](https://youtu.be/-YzMhaj9vw0)

## Features

- Record completed trades
- Automatically store the current date
- Support long and short trades
- Calculate profit or loss automatically
- Calculate R-multiple automatically
- Store trade records in a CSV file
- Load previously saved trades
- Generate a performance summary
- Calculate:
  - Total trades
  - Winning trades
  - Losing trades
  - Win rate
  - Total profit/loss
  - Average R-multiple

- Handle a missing trade file safely
- Unit tests for the main calculation and summary functions

## Trade Data

Each trade contains the following fields:

- Date
- Symbol
- Side
- Entry price
- Exit price
- Stop loss
- Position size
- Profit/loss
- R-multiple
- Strategy
- Mistake tag
- Notes

Example:

```text
BTCUSDT
Side: long
Entry: 100
Exit: 110
Stop Loss: 95
Position Size: 2
```

For this trade:

```text
Profit/Loss = (110 - 100) × 2 = 20
```

and:

```text
Risk = 100 - 95 = 5
Reward = 110 - 100 = 10

R-multiple = 10 / 5 = 2.0
```

## How It Works

TradeTrack currently provides two main operations:

```text
1. Add trade
2. View summary
```

### Add Trade

The program collects the trade details from the user.

It then calculates:

```text
Profit/Loss
R-multiple
```

and stores the complete trade record in:

```text
trades.csv
```

### View Summary

The program loads all stored trades and calculates aggregate performance statistics.

Example output:

```text
Total Trades: 3
Winning Trades: 2
Losing Trades: 1
Win Rate: 66.67%
Total Profit/Loss: 40.00
Average R: 1.33
```

## Project Structure

```text
tradetrack/
├── README.md
├── project.py
├── test_project.py
├── requirements.txt
├── trades.csv
└── .gitignore
```

### `project.py`

Contains the main application and core functions:

- `main()`
- `add_trade()`
- `get_trade()`
- `calculate_profit_loss()`
- `calculate_r_multiple()`
- `load_trades()`
- `summarize_trades()`
- `print_summary()`

### `test_project.py`

Contains pytest tests for the main business logic.

### `trades.csv`

Stores the recorded trades.

### `requirements.txt`

Contains the testing dependency:

```text
pytest
```

The application itself uses only Python standard-library modules.

## Installation

Clone the repository:

```bash
git clone https://github.com/WaleedHassanSh/tradetrack.git
```

Move into the project directory:

```bash
cd tradetrack
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python project.py
```

Then choose one of the available options:

```text
1. Add trade
2. View summary
3. Exit
```

## Testing

The project uses `pytest`.

Run the tests with:

```bash
pytest
```

The tests currently cover:

- Profit/loss calculations for long trades
- Profit/loss calculations for short trades
- Losing trades
- Invalid trade sides
- R-multiple calculations
- Invalid stop-loss conditions
- Performance summaries
- Empty trade summaries
- Floating-point summary calculations
- Loading trade data correctly from a CSV file

## Technologies

- Python
- CSV
- `datetime`
- pytest
- Git
- GitHub

## Design Decisions

### CSV Storage

CSV was chosen because it is simple, human-readable, and appropriate for a small Python project.

It also makes the stored data easy to inspect or open in spreadsheet software.

### Separate Calculation Functions

Profit/loss, R-multiple, and summary calculations are implemented as separate functions instead of being placed directly inside the user-interface logic.

This keeps the program easier to understand and makes the core logic independently testable.

### Automatic Calculations

Profit/loss and R-multiple are calculated automatically from the trade data instead of being entered manually.

This reduces repeated manual calculations and keeps the stored results consistent with the supplied trade values.

## What I Learned

This project helped me practice and reinforce:

- Python functions
- Conditionals and control flow
- Dictionaries
- File I/O
- CSV handling
- Exceptions
- Working with numeric data
- Separating program logic into reusable functions
- Unit testing with pytest
- Designing a small command-line application
- Organizing and documenting a Python project

## Limitations

TradeTrack is intentionally a small command-line project focused on Python fundamentals.

Current limitations include:

- No graphical or web interface
- No database
- No authentication or multiple users
- No charts or visual analytics
- No filtering by symbol or strategy
- Breakeven trades are included in total trades but are not classified as wins or losses

TradeTrack does **not** provide trading signals, financial advice, or market predictions.

It only records and summarizes trades supplied by the user.

## Future Improvements

Possible future improvements include:

- List and inspect individual trades
- Filter trades by symbol or strategy
- Analyze mistake tags
- Export performance reports
- Add charts and visual summaries
- Improve test coverage for CSV loading and file operations

## Project Context

TradeTrack was originally developed as my final project for **CS50's Introduction to Programming with Python**.

It also serves as the main showcase project from **Phase 1 — Python Programming** of my broader CS/AI/ML learning roadmap.

Roadmap repository:

[View my CS/AI/ML roadmap](https://github.com/WaleedHassanSh/ai-ml-roadmap)

The purpose of this phase was to build a strong Python foundation before progressing into data analysis, machine learning, deep learning, and modern AI systems.
