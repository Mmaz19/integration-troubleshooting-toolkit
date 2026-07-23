# JSON Payload Comparator

## Overview

A troubleshooting utility designed to compare two JSON payloads and identify structural and value differences.

---

## Business Scenario

During API integrations, payload changes can introduce unexpected behaviours.

Common situations:

- An API request worked previously but now fails
- A new application version changes the request structure
- Different environments send different data

This tool helps technical teams quickly identify what changed between two JSON payloads.

---

## Features

- Detect added fields
- Detect removed fields
- Detect modified values
- Support nested JSON structures

---

## Usage

Example:

```bash
python payload_comparator.py examples/original_payload.json examples/updated_payload.json
```

## Example Output
PAYLOAD COMPARISON REPORT

Modified fields:

customer.status
ACTIVE -> INACTIVE

Added fields:

customer.email

Removed fields:

customer.phone

## Technologies
Python
JSON
CLI utilities
Troubleshooting Use Cases

## Useful when investigating:
API regression issues
Environment differences
Integration failures after changes
Data transformation problems

