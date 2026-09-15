# Income Inequality Breakdown by Region Project

This program provides a report to the user regarding income inequality for each country in a region specified by the user. The report provides basic demographic details, a gini-coefficient breakdown for all years with inputted data, and a synopsis as to whether or not the income inequality has worsened or improved.

## API

This project uses the [REST COUNTRIES](https://api.restcountries.com/countries/v5) API.

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

Run python main.py alongside a specified region value (example shown below). The accepted values include: Europe, Oceania, Americas, Antarctic, Asia, Africa

```bash
python main.py Europe
```

Upon input of a valid value for region, the user will see an outputted Income Inequality report in the console detailing the trend of inequality in each country, as specified by the gini coefficients, in the region chosen.
If an unexpected value is inputted, the user will receive the following output in the console: "No results found from inquiry. Please try again."

## CLI Interactions

- **Filter by region** — enter a region name to generate an income inequality report for each country in the specified region

## Visualization

Running this code produces a line graph showing each country's gini coefficients by year in the region searched by the user. The x axis contains the years corresponding to the gini coefficient data collected. The y axis corresponds to the gini coefficient. This image answers the question: How does income inequality fluctuate over time for countries in a given region?

<c:\Users\lswag\Downloads\Figure_1.png/>

The main takeaway of this graph is both to visually show how inequality fluctutates in countries throughout time, and how countries compare to one another in terms of inequality. A second takeaway is to show how the lack of consistently collected data can skew results.

This chart type was chosen because I believe it most clearly demonstrates changes in income inequality over time, especially considering data for multiple countries are plotted onto the same graph.

Quick Note: In order for the terminal to progress, you must exit out of the pop up graph after the following code is run!:
```bash
plt.show()
```