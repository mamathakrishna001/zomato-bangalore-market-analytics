# 04 — EDA Insights

Generated from `scripts/02_eda.py` on the cleaned dataset (51,696 rows / 12,490 unique restaurants).
Chart pack: `dashboards/eda_charts/`.

## 1. Market Concentration (Geography)
Top localities by listing count: **BTM (5,124)**, HSR (2,523), Koramangala 5th Block (2,504),
JP Nagar (2,235), Whitefield (2,144), Indiranagar (2,083).

**Insight:** Demand/competition is heavily concentrated in South & East Bangalore tech-corridor
localities (BTM, HSR, Koramangala, Whitefield, Marathahalli) — these are saturated markets.
Lower-listing localities may represent under-served micro-markets worth investigating for expansion,
but should be cross-checked for population/footfall data (not in this dataset).

Chart: `01_top_localities.png`

## 2. Ratings Landscape
- Mean rating (rated restaurants only): **3.70 / 5**, median 3.70, std 0.44.
- 10,031 listings (19%) are `Not Rated` ("NEW" on Zomato) — a sizeable chunk of fresh entrants.
- Rating band split (of all 51,696): Excellent (4.0+) 24%, Good (3.5–3.9) 34%, Average (3.0–3.4) 18%,
  Poor (<3.0) 4%, Not Rated 19%.

**Insight:** Most established restaurants cluster in the "Good" band — a 4.0+ rating is a genuine
differentiator, not the norm. Charts: `02_rating_distribution.png`, `03_rating_band.png`.

## 3. Cost Landscape
- Mean cost for two: **₹555**, median ₹400, range ₹40–₹6,000.
- 25th percentile ₹300, 75th percentile ₹650 → the bulk of the market is budget/mid-range dining.

Chart: `04_cost_distribution.png`

## 4. Service Features Drive Engagement
| Feature | Avg Rating | Avg Votes |
|---|---|---|
| Online Order = No | 3.66 | 251 |
| Online Order = Yes | 3.72 | 307 |
| Book Table = No | 3.62 | 161 |
| **Book Table = Yes** | **4.14** | **1,147** |

**Insight:** Table booking availability shows a striking gap — restaurants offering it average
**4.14 vs 3.62** rating and **~7x the votes**. This is the single strongest engagement signal in the
dataset, almost certainly because table-booking restaurants tend to be more premium, full-service
dine-in establishments (correlation, not necessarily pure causation). Online ordering shows a smaller
but consistent lift. Charts: `05_online_order_vs_rating.png`, `06_book_table_vs_rating.png`.

## 5. Cuisine Trends
- Most listed primary cuisines: **North Indian (12,299)**, South Indian (5,010), Cafe (4,330),
  Chinese (3,066), Biryani (3,055).
- Highest **average-rated** cuisines (min. 50 listings): Modern Indian (4.31), European (4.26),
  Mediterranean (4.20), Japanese (4.19), American (4.16).

**Insight:** Volume leaders (North Indian, South Indian) are mass-market staples but not the top
rated. Niche/premium cuisines (Modern Indian, European, Japanese) consistently rate higher — likely
tied to the premium dining experience and price tier. Chart: `07_top_cuisines.png`.

## 6. Restaurant Type Mix
- Most common types: **Quick Bites (14,266)**, Casual Dining (11,310), Cafe (3,997),
  Dessert Parlor (2,282).
- Best average rating among high-volume types: **Pub (4.10)**, Bar (3.89), Dessert Parlor (3.88),
  Cafe (3.87) — vs. Quick Bites at just 3.55, the lowest among major formats.

**Insight:** Bars/Pubs/Cafes outperform fast, low-engagement formats (Quick Bites, Takeaway, Delivery)
on rating — sit-down, experience-driven formats earn better reviews. Chart: `08_top_rest_types.png`.

## 7. Cost vs. Rating Relationship
- Correlation: cost↔rating = **0.39**, cost↔votes = 0.38, rating↔votes = 0.43 — moderate positive
  relationships, not strong linear ones.
- Avg rating by cost bucket: Budget 3.56 → Mid 3.59 → Premium 3.76 → **Luxury 4.06**.

**Insight:** "You get what you pay for" holds directionally — pricier restaurants average meaningfully
higher ratings — but the relationship is moderate, not deterministic; plenty of budget options rate
well too. Charts: `09_cost_vs_rating.png`, `10_cost_bucket_vs_rating.png`.

## 8. Listing Type Mix
Delivery (50%) and Dine-out (34%) dominate listing contexts; Desserts, Cafes, Drinks & Nightlife,
Buffet, Pubs & Bars are smaller niches. Chart: `11_listing_type_mix.png`.

## 9. Top Performers (Benchmarks)
Top 10 most-voted unique restaurants — dominated by breweries/large-format dine-out venues:
**Byg Brewski Brewing Company** (16,345 votes, 4.9★, Sarjapur Road), **Toit** (14,956, 4.7★),
**Truffles** (14,654, 4.7★), **AB's – Absolute Barbecues** (12,121, 4.8★), **The Black Pearl** (10,413, 4.7★).

**Insight:** The most engaged restaurants are large experiential dine-out/brewery formats with table
booking, premium pricing (₹900–₹2,000 for two), and very high ratings — reinforcing the table-booking
and premium-format findings above.

## Summary of Cross-Cutting Findings (feeds dashboard KPIs & recommendations)
1. Market is concentrated in a handful of tech-corridor localities — high competition there.
2. Table booking is the strongest differentiator for rating + engagement; cuisine and format matter more
   than raw online-order availability.
3. Niche/premium cuisines and experiential formats (Pubs, Bars, fine dining/breweries) outperform
   mass-market Quick Bites on quality perception.
4. Cost correlates moderately with rating — premium positioning is associated with, not a guarantee of,
   better reviews.
