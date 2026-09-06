def assert_columns(df, expected_columns):
    missing = [c for c in expected_columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
