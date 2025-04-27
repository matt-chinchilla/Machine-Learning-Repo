---
title: "Feature Engineering & Preprocessing"
foam_id: project-02-feature-engineering
tags: [feature-engineering]
---

See hub: [[02: End-to-End ML Project|project-02-end-to-end-ml]]

### Custom Ratio Features

```python
def column_ratio(X: np.ndarray) -> np.ndarray:
    return X[:, [0]] / X[:, [1]]
```
- In → two columns (e.g. bedrooms/rooms)  
- Out → single `ratio` column

```python
def ratio_pipeline() -> Pipeline:
    return make_pipeline(
        SimpleImputer(strategy="median"),
        FunctionTransformer(column_ratio, feature_names_out=ratio_name),
        StandardScaler()
    )
```

### Log-Transform Pipeline

```python
log_pipeline: Pipeline = make_pipeline(
    SimpleImputer(strategy="median"),
    FunctionTransformer(np.log, feature_names_out="one-to-one"),
    StandardScaler()
)
```

### Geographic Clustering

```python
cluster_simil = ClusterSimilarity(n_clusters=10, gamma=1., random_state=42)
```

### Categorical Pipeline

```python
cat_pipeline = make_pipeline(
    OneHotEncoder(),
    # …
)
```

### Default Numeric Pipeline

```python
default_num_pipeline = make_pipeline(
    SimpleImputer(strategy="median"),
    StandardScaler()
)
```

### ColumnTransformer Assembly

```python
preprocessing: ColumnTransformer = ColumnTransformer([
  ("bedrooms",        ratio_pipeline(), ["total_bedrooms","total_rooms"]),
  ("rooms_per_house", ratio_pipeline(), ["total_rooms","households"]),
  ("people_per_house",ratio_pipeline(), ["population","households"]),
  ("log",             log_pipeline,    ["total_bedrooms","total_rooms","population","households","median_income"]),
  ("geo",             cluster_simil,   ["latitude","longitude"]),
  ("cat",             cat_pipeline,    make_column_selector(dtype_include=object]),
], remainder=default_num_pipeline)
```

Next ▶ [[modeling|project-02-modeling]]
