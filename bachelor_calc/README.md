# Bachelor Contestant Scoring Tool

A simple Python-based tool to score and rank top ten lists of contestants on The Bachelor/Bachelorette.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Data Format](#data-format)
  - [Contestant Status List](#contestant-status-list)
  - [Ranking List](#ranking-list)

## Installation

1. Prerequisites:
   - Python 3.11
2. Clone this repository to your local machine.
3. There are no additional dependencies required.

## Usage

1. Prepare/update your ranking and contestant lists in the format as mentioned in the Data Format section.
2. Run the tool: `python bachelor-calc.py`
3. Check the console for the scores.

## Features

- Calculates min and max scores for each list submission  

## Data Format

### Contestant Status List
Anna-out
April
Christina
...

suffixes can be added in any order
- "-out" denotes a contestant that has been eliminated
- "-FIR" denotes a contestant received the first impression rose
- "-next" denotes a contestant will be the next bachelor/bachelorette
- "-##" denotes a contestant was eliminated in a particular position (e.g. "-9" contestant was the 9th to last person to be not receive a rose)


### Ranking List
name: Owner's Name
Contestant
Contestant
...

The 11th contestant is who an individual picked for the next bachelor/bachelorette
