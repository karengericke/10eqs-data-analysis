# 10EQS Data Analysis Project

## Overview
This project is designed to help small business owners track their product pricing against market conditions. It integrates internal pricing data with external pricing sources and generates actionable insights.
Since it's for a Challenge, it gathers the information from a dummy site (having limitations on the retrieved information insights and the actual calculations made for the recommendations)

## Setup Instructions
### Prerequisites
- Python 3.7+
- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Ensure `products.csv` is placed in the correct directory:
  ```
  C:/Users/Kmger/OneDrive/Bureau/karenina/10eqs-data-analysis/data/products.csv
  ```

### Running the Script
To execute the analysis and generate insights, run:
```bash
python analysis.py
```
This will:
1. Load internal pricing data from `products.csv`.
2. Fetch external product pricing data from an API.
3. Compare internal vs. external pricing and generate insights.
4. Save results to `report.md`.

## Required API Keys/Credentials
No API keys are required for the current external data source (`https://dummyjson.com/products`). If using a real-world API, ensure API keys are stored in a `.env` file and loaded securely.

## Approach
1. **Data Ingestion**: Load internal product pricing from a CSV.
2. **External Data Integration**: Fetch product pricing from an API.
3. **Data Cleaning & Processing**: Normalize and clean product names.
4. **Price Comparison**: Calculate the difference between internal and external prices.
5. **Reporting**: Save insights into a structured markdown file.

## Known Issues & Limitations
- **Dummy Data Source**: Since this project is developed as part of a challenge, it retrieves information from a placeholder API. This may limit the depth of insights and the accuracy of recommendations, as the external data does not reflect real-world market conditions.
- **Product Name Mismatch**: If external product names differ significantly, matching accuracy may be reduced.
- **API Data Variability**: External pricing may change over time, affecting analysis consistency.
- **Assumption on Price Calculation**: External pricing is assumed to be correct but may have inaccuracies.
- **Performance Consideration**: For larger datasets, fuzzy matching can slow down execution.

## Time Spent on Each Component
| Component                     | Time Spent |
|--------------------------------|------------|
| CSV Data Handling             | 10 min     |
| Data Cleaning & Preprocessing | 35 min     |
| Price Comparison & Insights   | 30 min     |
| Report Generation             | 15 min     |
| Debugging & Testing           | 50 min     |
| Documentation & README        | 20 min     |
| **Total**                     | **3 hrs**  |

## Future Enhancements
- API integration

---
Developed as part of the 10EQS Technical Evaluation Challenge 🚀
