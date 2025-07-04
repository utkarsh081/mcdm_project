import pandas as pd

class MCDMScorer:
    def __init__(self, weights: dict, feature_types: dict):
        self.weights = weights
        self.feature_types = feature_types
        self._validate_inputs()

    def _validate_inputs(self):
        if set(self.weights.keys()) != set(self.feature_types.keys()):
            raise ValueError("Keys in weights and feature_types must match.")
        for ft in self.feature_types.values():
            if ft not in ["benefit", "cost"]:
                raise ValueError("feature_types must be 'benefit' or 'cost'.")

    def normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        norm_df = pd.DataFrame(index=df.index)
        for col in df.columns:
            values = df[col]
            if self.feature_types[col] == "benefit":
                norm_df[col] = (values - values.min()) / (values.max() - values.min())
            elif self.feature_types[col] == "cost":
                norm_df[col] = (values.max() - values) / (values.max() - values.min())
        return norm_df

    def score(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        norm_df = self.normalize(df)
        for col in self.weights:
            norm_df[col] *= self.weights[col]
        df["score"] = norm_df.sum(axis=1)
        df["rank"] = df["score"].rank(ascending=False).astype(int)
        return df.sort_values("score", ascending=False)
