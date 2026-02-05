# Bitcoin Transaction Decoder

A simple Python tool to decode and inspect raw Bitcoin transactions.
This project was built as part of my learning journey into Bitcoin
protocol internals and transaction structure.

## Why I Built This
I wanted to understand how Bitcoin transactions are structured at
the byte level — including inputs, outputs, scripts, and values —
instead of treating them as black boxes.

## What This Tool Does
- Takes a raw Bitcoin transaction (hex)
- Parses transaction fields
- Displays inputs, outputs, and values in a readable format

## Concepts Covered
- Raw Bitcoin transactions
- Transaction inputs and outputs
- ScriptPubKey basics
- Endianness in Bitcoin
- UTXO model (high-level)

## How It Works (High-Level)
The decoder reads the raw transaction hex, converts it into bytes,
and sequentially parses each field based on the Bitcoin protocol
specification.

## How to Run
```bash
python decoder.py
