# JSON Payload Validator

## Overview

A lightweight Python utility designed to validate JSON payload structures and quickly identify formatting issues during API troubleshooting activities.

---

## Business Scenario

During API integrations, incorrect payload formats are a common source of failures.

Examples:

- Missing brackets
- Invalid JSON syntax
- Incorrect separators
- Malformed structures

This tool helps technical teams validate payloads before further investigation.

---

## Features

- JSON syntax validation
- Clear error reporting
- File-based validation
- Troubleshooting-oriented output

---

## Usage

Run:

```bash
python json_validator.py examples/valid_payload.json
```

Example output:

JSON validation successful
Payload structure is valid

For invalid JSON:

JSON validation failed

Error:
Expecting ',' delimiter
Line: 5
Column: 10

## Technologies
- Python
- JSON
- Command Line Interface