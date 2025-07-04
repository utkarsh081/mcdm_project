# 🔎 MCDM Scorer – Multi-Criteria Decision Making System

This project provides a **universal, reusable Python module** for solving Multi-Criteria Decision Making (MCDM) problems — such as ranking, prioritizing, or evaluating options based on multiple weighted criteria.

Built using **pandas**, the system is suitable for use cases like:
- Product ranking (based on price, performance, etc.)
- Option selection with cost-benefit trade-offs
- Decision support tools in various domains

---

## ✅ Features

- ✔️ **Reusable Python class** for scoring and ranking
- ✔️ Normalize both:
  - “**The more the better**” (benefit features)
  - “**The less the better**” (cost features)
- ✔️ Accepts **custom weights** per feature
- ✔️ Outputs **final scores** and **rankings**
- ✔️ Exports to CSV (optional)

---

## 📁 Project Structure

mcdm_project/
- │
- ├── mcdm.py # Core scoring logic class (MCDMScorer)
- ├── demo.ipynb # Demo notebook with example usage
- ├── ranked_results.csv # (Optional) Exported ranked output
- └── requirements.txt # Dependencies (pandas, numpy)

---

## 🚀 How to Use

### 1. Install dependencies

```bash```
pip install -r requirements.txt

---

## 📦 Output (CSV Optional)

The output DataFrame will contain normalized scores and ranks:

| Product | Price | Battery Life | Speed (GHz) | score | rank |
| ------- | ----- | ------------ | ----------- | ----- | ---- |
| B       | 800   | 12           | 2.6         | 0.9   | 1    |
| D       | 900   | 11           | 2.8         | 0.8   | 2    |
| A       | 1000  | 10           | 2.4         | 0.4   | 3    |
| C       | 1200  | 9            | 2.2         | 0.0   | 4    |

Results can be exported automatically to ranked_results.csv using export_csv=True.

---

## ✨ Extensibility
This tool is dataset-agnostic. You can plug in:
- Any number of numeric features
- Any mix of cost/benefit criteria
- Custom feature groups and weights

---

## 📄 License
MIT License – free for commercial and personal use.

---

## 🧑‍💻 Author

Built by Utkarsh Pandey, B.Tech CSE (2025)

GitHub: utkarsh081
