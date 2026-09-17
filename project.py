import csv
from datetime import datetime

FIELDNAMES = [
    "date",
    "symbol",
    "side",
    "entry",
    "exit_price",
    "stop_loss",
    "position_size",
    "profit_loss",
    "r_multiple",
    "strategy",
    "mistake_tag",
    "notes",
]


def main():

    while True:
        print("1. Add trade\n2. View summary\n3. Exit")

        choice = input("\nChoose: ").strip()

        if choice == "1":
            add_trade()

        elif choice == "2":
            trades = load_trades()
            summary = summarize_trades(trades)
            print_summary(summary)

        elif choice == "3":
            print("\nExiting...\n")
            break

        else:
            print("\nInvalid choice. Please choose 1, 2, or 3.\n")
            continue


def add_trade():
    trade = get_trade()

    profit_loss = calculate_profit_loss(
        trade["side"], trade["entry"], trade["exit_price"], trade["position_size"]
    )

    r_multiple = calculate_r_multiple(
        trade["side"], trade["entry"], trade["exit_price"], trade["stop_loss"]
    )

    trade["profit_loss"] = profit_loss
    trade["r_multiple"] = r_multiple

    with open("trades.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(trade)
        print("\nTrade saved.\n")


def get_trade():
    while True:
        try:
            entry = float(input("\nEntry Price: "))
            exit_price = float(input("Exit Price: "))
            stop_loss = float(input("Stop Loss: "))
            position_size = float(input("Position Size: "))

            if entry <= 0 or exit_price <= 0 or stop_loss <= 0 or position_size <= 0:
                print("\nPrices and position size must be greater than zero.")
                continue

            if entry == exit_price:
                print("\nEntry price and exit price cannot be the same.")
                continue

        except ValueError:
            print("\nInvalid input. Please enter numeric values.")
            continue

        date = str(datetime.now().astimezone().date())

        symbol = input("Symbol: ").strip().upper()
        if len(symbol) == 0:
            print("\nSymbol cannot be empty.")
            continue

        side = input("Side: ").strip().lower()
        if side not in ["long", "short"]:
            print("\nInvalid side. Please enter 'long' or 'short'.")
            continue

        if side == "long" and exit_price <= stop_loss:
            print("\nFor long trades, exit price should be greater than stop loss.")
            continue

        elif side == "short" and exit_price >= stop_loss:
            print("\nFor short trades, exit price should be less than stop loss.")
            continue

        if side == "long" and entry <= stop_loss:
            print("\nFor long trades, entry price should be greater than stop loss.")
            continue
        elif side == "short" and entry >= stop_loss:
            print("\nFor short trades, entry price should be less than stop loss.")
            continue

        strategy = input("Strategy: ").strip().lower()
        if strategy == "":
            print("\nStrategy cannot be empty.")
            continue

        mistake_tag = input("Mistake Tag: ").strip().lower()
        if mistake_tag == "":
            print("\nMistake tag cannot be empty.")
            continue

        notes = input("Notes: ").strip()
        if notes == "":
            print("\nNotes cannot be empty.")
            continue

        return {
            "date": date,
            "symbol": symbol,
            "side": side,
            "entry": entry,
            "exit_price": exit_price,
            "stop_loss": stop_loss,
            "position_size": position_size,
            "strategy": strategy,
            "mistake_tag": mistake_tag,
            "notes": notes,
        }


def calculate_profit_loss(side, entry, exit_price, position_size):
    if side == "long":
        return (exit_price - entry) * position_size
    elif side == "short":
        return (entry - exit_price) * position_size


def calculate_r_multiple(side, entry, exit_price, stop_loss):
    if side == "long":
        reward = exit_price - entry
        risk = entry - stop_loss
    else:
        reward = entry - exit_price
        risk = stop_loss - entry

    return reward / risk


def load_trades(filename="trades.csv"):
    trades = []

    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["entry"] = float(row["entry"])
                row["exit_price"] = float(row["exit_price"])
                row["stop_loss"] = float(row["stop_loss"])
                row["position_size"] = float(row["position_size"])
                row["profit_loss"] = float(row["profit_loss"])
                row["r_multiple"] = float(row["r_multiple"])

                trades.append(row)

    except FileNotFoundError:
        return []

    return trades


def summarize_trades(trades):

    total_trades = len(trades)

    if total_trades == 0:
        return {
            "total_trades": 0,
            "winning_trades": 0,
            "losing_trades": 0,
            "win_rate": 0,
            "total_profit_loss": 0,
            "average_r": 0,
        }

    total_profit_loss = sum(trade["profit_loss"] for trade in trades)
    winning_trades = len([trade for trade in trades if trade["profit_loss"] > 0])
    losing_trades = len([trade for trade in trades if trade["profit_loss"] < 0])
    win_rate = (winning_trades / total_trades) * 100
    average_r = sum(trade["r_multiple"] for trade in trades) / total_trades

    return {
        "total_trades": total_trades,
        "winning_trades": winning_trades,
        "losing_trades": losing_trades,
        "win_rate": win_rate,
        "total_profit_loss": total_profit_loss,
        "average_r": average_r,
    }


def print_summary(summary):
    print("\nSummary:")
    print("Total Trades: ", summary["total_trades"])
    print("Winning Trades: ", summary["winning_trades"])
    print("Losing Trades: ", summary["losing_trades"])
    print(f"Win Rate: {summary['win_rate']:.2f}%")
    print(f"Total Profit/Loss: {summary['total_profit_loss']:.2f}")
    print(f"Average R: {summary['average_r']:.2f}")
    print()


if __name__ == "__main__":
    main()
