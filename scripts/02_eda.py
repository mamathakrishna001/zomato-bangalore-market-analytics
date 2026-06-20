"""
Zomato Bangalore — Exploratory Data Analysis
Reads data/cleaned/zomato_cleaned.csv, saves chart pack to dashboards/eda_charts/
and prints key numbers used to write docs/04_eda_insights.md
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
CHART_DIR = "dashboards/eda_charts"

df = pd.read_csv("data/cleaned/zomato_cleaned.csv")
print(f"Loaded cleaned data: {df.shape[0]:,} rows x {df.shape[1]} columns")

uniq = df[df["is_unique_restaurant"]]
print(f"Unique restaurants: {len(uniq):,}")

# ---------- 1. Top 15 localities by restaurant count ----------
top_loc = df["location"].value_counts().head(15)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_loc.values, y=top_loc.index, color="#cb202d")
plt.title("Top 15 Localities by Number of Listings")
plt.xlabel("Listings")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/01_top_localities.png", dpi=150)
plt.close()
print("\nTop 10 localities by listings:\n", top_loc.head(10))

# ---------- 2. Rating distribution ----------
plt.figure(figsize=(8, 5))
sns.histplot(df["rating"].dropna(), bins=20, color="#cb202d", kde=True)
plt.title("Distribution of Ratings")
plt.xlabel("Rating (out of 5)")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/02_rating_distribution.png", dpi=150)
plt.close()
print("\nRating stats:\n", df["rating"].describe())

# ---------- 3. Rating band distribution ----------
band_order = ["Excellent (4.0+)", "Good (3.5-3.9)", "Average (3.0-3.4)", "Poor (<3.0)", "Not Rated"]
band_counts = df["rating_band"].value_counts().reindex(band_order)
plt.figure(figsize=(8, 5))
sns.barplot(x=band_counts.index, y=band_counts.values, color="#cb202d")
plt.title("Restaurant Count by Rating Band")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/03_rating_band.png", dpi=150)
plt.close()
print("\nRating band counts:\n", band_counts)

# ---------- 4. Cost distribution ----------
plt.figure(figsize=(8, 5))
sns.histplot(df["cost_for_two"].dropna(), bins=30, color="#cb202d")
plt.title("Distribution of Cost for Two (₹)")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/04_cost_distribution.png", dpi=150)
plt.close()
print("\nCost stats:\n", df["cost_for_two"].describe())

# ---------- 5. Online order / Book table vs rating ----------
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="online_order", y="rating", palette=["#999999", "#cb202d"])
plt.title("Rating by Online Order Availability")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/05_online_order_vs_rating.png", dpi=150)
plt.close()

plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="book_table", y="rating", palette=["#999999", "#cb202d"])
plt.title("Rating by Table Booking Availability")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/06_book_table_vs_rating.png", dpi=150)
plt.close()

oo = df.groupby("online_order")[["rating", "votes"]].mean()
bt = df.groupby("book_table")[["rating", "votes"]].mean()
print("\nOnline order -> avg rating/votes:\n", oo)
print("\nBook table -> avg rating/votes:\n", bt)

# ---------- 6. Top cuisines ----------
top_cuisine = df["primary_cuisine"].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cuisine.values, y=top_cuisine.index, color="#cb202d")
plt.title("Top 10 Primary Cuisines by Listing Count")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/07_top_cuisines.png", dpi=150)
plt.close()
print("\nTop 10 cuisines:\n", top_cuisine)

cuisine_rating = (
    df.groupby("primary_cuisine")["rating"].agg(["mean", "count"])
    .query("count >= 50")
    .sort_values("mean", ascending=False)
    .head(10)
)
print("\nTop 10 highest-rated cuisines (min 50 listings):\n", cuisine_rating)

# ---------- 7. Restaurant type performance ----------
type_stats = (
    df.groupby("primary_rest_type")["rating"].agg(["mean", "count"])
    .query("count >= 50")
    .sort_values("count", ascending=False)
    .head(10)
)
print("\nTop 10 restaurant types by count (with avg rating):\n", type_stats)

plt.figure(figsize=(10, 6))
sns.barplot(x=type_stats["count"], y=type_stats.index, color="#cb202d")
plt.title("Top 10 Restaurant Types by Listing Count")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/08_top_rest_types.png", dpi=150)
plt.close()

# ---------- 8. Cost vs rating relationship ----------
plt.figure(figsize=(8, 6))
sample = df.dropna(subset=["cost_for_two", "rating"]).sample(min(5000, len(df)), random_state=42)
sns.scatterplot(data=sample, x="cost_for_two", y="rating", alpha=0.3, color="#cb202d")
sns.regplot(data=sample, x="cost_for_two", y="rating", scatter=False, color="black")
plt.title("Cost for Two vs Rating")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/09_cost_vs_rating.png", dpi=150)
plt.close()
corr = df[["cost_for_two", "rating", "votes"]].corr()
print("\nCorrelation matrix (cost, rating, votes):\n", corr)

# ---------- 9. Cost bucket vs rating ----------
bucket_order = ["Budget (<300)", "Mid (300-599)", "Premium (600-999)", "Luxury (1000+)"]
bucket_stats = df[df["cost_bucket"] != "Unknown"].groupby("cost_bucket")["rating"].mean().reindex(bucket_order)
plt.figure(figsize=(8, 5))
sns.barplot(x=bucket_stats.index, y=bucket_stats.values, color="#cb202d")
plt.title("Average Rating by Cost Bucket")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/10_cost_bucket_vs_rating.png", dpi=150)
plt.close()
print("\nAvg rating by cost bucket:\n", bucket_stats)

# ---------- 10. Listing type mix ----------
lt = df["listing_type"].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(lt.values, labels=lt.index, autopct="%1.1f%%", colors=sns.color_palette("Reds", len(lt)))
plt.title("Listing Type Mix")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/11_listing_type_mix.png", dpi=150)
plt.close()
print("\nListing type mix:\n", lt)

# ---------- 11. Top 10 restaurants by votes (unique restaurants) ----------
top_voted = uniq.sort_values("votes", ascending=False)[["name", "location", "votes", "rating", "cost_for_two"]].head(10)
print("\nTop 10 most-voted unique restaurants:\n", top_voted.to_string(index=False))

# ---------- 12. Locality-level summary table (for BI cross-check) ----------
loc_summary = df.groupby("location").agg(
    listings=("name", "count"),
    avg_rating=("rating", "mean"),
    avg_cost=("cost_for_two", "mean"),
    avg_votes=("votes", "mean"),
).sort_values("listings", ascending=False)
loc_summary.to_csv("dashboards/eda_charts/locality_summary.csv")
print("\nSaved locality_summary.csv. Top 5 rows:\n", loc_summary.head())

print("\nAll charts saved to", CHART_DIR)
