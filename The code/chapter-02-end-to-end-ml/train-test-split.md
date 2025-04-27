---
title: "Train/Test Split"
foam_id: project-02-train-test-split
tags: [train-test-split]
---

See hub: [[02: End-to-End ML Project|project-02-end-to-end-ml]]

## Functions

```python
def split_train_test(data: pd.DataFrame, test_ratio: float) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Randomly split into train & test sets."""
```

```python
def is_id_in_test_set(identifier: int, test_ratio: float) -> bool:
    """Deterministic CRC32-based test-set assignment."""
```

## Variables

- `housing_with_id`  
- `strat_train_set`, `strat_test_set`

Next ▶ [[feature-engineering|project-02-feature-engineering]]
