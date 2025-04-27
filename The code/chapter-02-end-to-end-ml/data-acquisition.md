---
title: "Data Acquisition"
foam_id: project-02-data-acquisition
tags: [data-acquisition]
---

See hub: [[02: End-to-End ML Project|project-02-end-to-end-ml]]

## Functions

```python
def fetch_housing_data(data_url: str, output_path: str) -> None:
    """Download and extract the housing dataset."""
    ...
```

```python
def load_housing_data(housing_path: str) -> pd.DataFrame:
    """Load housing CSV into pandas DataFrame."""
    ...
```

## Variables

- `HOUSING_PATH`: Local data directory.  
- `housing`: Raw DataFrame.

Next ▶ [[data-exploration|project-02-data-exploration]]
