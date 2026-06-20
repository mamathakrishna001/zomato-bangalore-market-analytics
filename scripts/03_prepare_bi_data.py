"""
Prepare BI-ready, star-schema-style tables for Power BI from the
cleaned dataset. Mirrors what a BA/DA would hand off to a BI developer:
one Fact table + dimension/bridge tables for multi-valued fields.
"""
import pandas as pd

df = pd.read_csv("data/cleaned/zomato_cleaned.csv")

# Surrogate key for the fact table (1 row per listing)
df = df.reset_index(drop=True)
df["listing_id"] = df.index + 1

fact_cols = [
    "listing_id", "url", "name", "address", "location", "listing_city",
    "online_order", "book_table", "votes", "rating", "cost_for_two",
    "primary_cuisine", "primary_rest_type", "listing_type",
    "rating_band", "cost_bucket", "is_unique_restaurant",
]
fact = df[fact_cols]
fact.to_csv("data/cleaned/Fact_Listings.csv", index=False)
print(f"Fact_Listings.csv: {fact.shape}")

# Bridge table: listing_id <-> each individual cuisine (handles multi-valued cuisines)
cuisine_bridge = (
    df[["listing_id", "cuisines"]]
    .dropna(subset=["cuisines"])
    .assign(cuisine=lambda d: d["cuisines"].str.split(","))
    .explode("cuisine")
)
cuisine_bridge["cuisine"] = cuisine_bridge["cuisine"].str.strip()
cuisine_bridge = cuisine_bridge[["listing_id", "cuisine"]]
cuisine_bridge.to_csv("data/cleaned/Bridge_Cuisines.csv", index=False)
print(f"Bridge_Cuisines.csv: {cuisine_bridge.shape}, unique cuisines: {cuisine_bridge['cuisine'].nunique()}")

# Bridge table: listing_id <-> each individual rest_type
type_bridge = (
    df[["listing_id", "rest_type"]]
    .dropna(subset=["rest_type"])
    .assign(rtype=lambda d: d["rest_type"].str.split(","))
    .explode("rtype")
)
type_bridge["rtype"] = type_bridge["rtype"].str.strip()
type_bridge = type_bridge[["listing_id", "rtype"]].rename(columns={"rtype": "rest_type_single"})
type_bridge.to_csv("data/cleaned/Bridge_RestTypes.csv", index=False)
print(f"Bridge_RestTypes.csv: {type_bridge.shape}, unique types: {type_bridge['rest_type_single'].nunique()}")

# Dimension: Location summary (one row per locality)
dim_location = (
    df.groupby("location")
    .agg(
        listing_count=("listing_id", "count"),
        unique_restaurant_count=("is_unique_restaurant", "sum"),
        avg_rating=("rating", "mean"),
        avg_cost_for_two=("cost_for_two", "mean"),
        avg_votes=("votes", "mean"),
        online_order_pct=("online_order", lambda s: (s == "Yes").mean() * 100),
        book_table_pct=("book_table", lambda s: (s == "Yes").mean() * 100),
    )
    .reset_index()
    .round(2)
)
dim_location.to_csv("data/cleaned/Dim_Location_Summary.csv", index=False)
print(f"Dim_Location_Summary.csv: {dim_location.shape}")

print("\nAll BI-ready tables written to data/cleaned/")
