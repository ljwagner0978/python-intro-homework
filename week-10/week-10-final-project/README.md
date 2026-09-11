# Income Inequality Breakdown by Region Project

This program provides a report to the user regarding income inequality for each country in a region specified by the user. The report provides basic demographic details, a gini-coefficient breakdown for all years with inputted data, and a synopsis as to whether or not the income inequality has worsened or improved.

## API

This project uses the [REST COUNTRIES API](https://api.restcountries.com/countries/v5) API.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ljwagner0978/python-intro-final-project.git
   cd python-intro-final-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   # .venv\Scripts\activate       # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py
```

When this program runs, add a specified region value. The accepted values include: Europe, Oceania, Americas, Antarctic, Asia, Africa
Upon input of a valid value for region, the user will see an outputted Income Inequality report in the console detailing the trend of inequality in each country, as specified by the gini coefficients, in the region chosen.
If an unexpected value is inputted, the user will receive the following output in the console: "No results found from inquiry. Please try again."

## CLI Interactions

- **Filter by region** — enter a region name to see all matching records for income inequality report generation

