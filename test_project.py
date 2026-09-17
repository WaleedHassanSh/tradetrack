import csv

import pytest

from project import (
    calculate_profit_loss,
    calculate_r_multiple,
    load_trades,
    summarize_trades,
)

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


def test_calculate_profit_loss():
    assert calculate_profit_loss("long", 100, 110, 2) == 20
    assert calculate_profit_loss("short", 100, 90, 2) == 20
    assert calculate_profit_loss("long", 100, 95, 2) == -10

    with pytest.raises(ValueError):
        calculate_profit_loss("buy", 100, 110, 2)


def test_calculate_r_multiple():
    assert calculate_r_multiple("long", 100, 110, 95) == 2
    assert calculate_r_multiple("short", 100, 90, 105) == 2
    assert calculate_r_multiple("long", 100, 95, 95) == -1

    with pytest.raises(ValueError):
        calculate_r_multiple("buy", 100, 110, 95)
    with pytest.raises(ValueError):
        calculate_r_multiple("long", 100, 110, 100)


def test_summarize_trades():
    trades = [
        {"profit_loss": 20, "r_multiple": 2},
        {"profit_loss": -10, "r_multiple": -1},
        {"profit_loss": 30, "r_multiple": 3},
    ]

    summary = summarize_trades(trades)

    assert summary["total_trades"] == 3
    assert summary["winning_trades"] == 2
    assert summary["losing_trades"] == 1
    assert summary["total_profit_loss"] == 40

    assert summary["win_rate"] == pytest.approx(66.666, rel=1e-3)
    assert summary["average_r"] == pytest.approx(1.333, rel=1e-3)


def test_summarize_empty_trades():
    summary = summarize_trades([])

    assert summary["total_trades"] == 0
    assert summary["win_rate"] == 0
    assert summary["average_r"] == 0


def test_load_trades(tmp_path):
    file_path = tmp_path / "trades.csv"

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerow(
            {
                "date": "2026-05-02",
                "symbol": "BTCUSDT",
                "side": "long",
                "entry": 100.0,
                "exit_price": 110.0,
                "stop_loss": 95.0,
                "position_size": 2.0,
                "profit_loss": 20.0,
                "r_multiple": 2.0,
                "strategy": "breakout",
                "mistake_tag": "none",
                "notes": "clean breakout trade",
            }
        )

    trades = load_trades(file_path)

    assert len(trades) == 1
    assert trades[0]["symbol"] == "BTCUSDT"
    assert trades[0]["side"] == "long"
    assert trades[0]["profit_loss"] == 20.0
    assert trades[0]["r_multiple"] == 2.0
