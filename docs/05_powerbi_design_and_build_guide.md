# 05 — Power BI Dashboard: Design & Build Guide

## Data Source
Folder: `powerbi/` (copies of the BI-ready tables also in `data/cleaned/`)
- `Fact_Listings.csv` — 51,696 rows, 1 row per listing, grain = `listing_id`
- `Bridge_Cuisines.csv` — listing_id ↔ single cuisine (handles multi-cuisine listings)
- `Bridge_RestTypes.csv` — listing_id ↔ single rest type
- `Dim_Location_Summary.csv` — pre-aggregated locality stats (93 rows)

## Data Model (relationships)
- `Fact_Listings[listing_id]` 1 → * `Bridge_Cuisines[listing_id]`
- `Fact_Listings[listing_id]` 1 → * `Bridge_RestTypes[listing_id]`
- `Fact_Listings[location]` * → 1 `Dim_Location_Summary[location]`

All relationships: single direction (Fact filters bridges/dim), cardinality as above.

## Core DAX Measures
```
Total Listings = COUNTROWS(Fact_Listings)

Unique Restaurants = CALCULATE(COUNTROWS(Fact_Listings), Fact_Listings[is_unique_restaurant] = TRUE)

Avg Rating = AVERAGE(Fact_Listings[rating])

Avg Cost for Two = AVERAGE(Fact_Listings[cost_for_two])

Total Votes = SUM(Fact_Listings[votes])

Online Order % =
DIVIDE(
    CALCULATE(COUNTROWS(Fact_Listings), Fact_Listings[online_order] = "Yes"),
    COUNTROWS(Fact_Listings)
)

Book Table % =
DIVIDE(
    CALCULATE(COUNTROWS(Fact_Listings), Fact_Listings[book_table] = "Yes"),
    COUNTROWS(Fact_Listings)
)

Avg Rating (Book Table = Yes) =
CALCULATE([Avg Rating], Fact_Listings[book_table] = "Yes")

Avg Rating (Book Table = No) =
CALCULATE([Avg Rating], Fact_Listings[book_table] = "No")
```

## Dashboard Pages

### Page 1 — Market Overview
- **KPI cards (top row):** Total Listings, Unique Restaurants, Avg Rating, Avg Cost for Two, Online Order %, Book Table %
- **Map or bar chart:** Listings by Location (top 15) — bar chart, sorted descending
- **Donut chart:** Listing Type Mix (`listing_type`)
- **Slicer panel (left):** Location, Online Order, Book Table, Rating Band, Cost Bucket

### Page 2 — Ratings & Quality
- **Histogram (clustered column):** Rating distribution by Rating Band
- **Clustered bar:** Avg Rating by Primary Restaurant Type (top 10 by count)
- **Clustered bar:** Avg Rating by Primary Cuisine (top 10, min count filter)
- **Scatter chart:** Cost for Two (x) vs Avg Rating (y), bubble size = Votes, by Primary Cuisine

### Page 3 — Service Features Impact
- **Side-by-side bar:** Avg Rating & Avg Votes by Online Order (Yes/No)
- **Side-by-side bar:** Avg Rating & Avg Votes by Book Table (Yes/No)
- **Table:** Top 10 restaurants by Votes (unique restaurants only) with Rating, Cost, Location

### Page 4 — Locality Deep Dive
- Built primarily from `Dim_Location_Summary`
- **Table/matrix:** Location, Listing Count, Unique Restaurants, Avg Rating, Avg Cost, Avg Votes,
  Online Order %, Book Table %, sortable
- **Bar chart:** Top 10 localities by Avg Rating (min listing count filter, e.g. >= 100)

## Step-by-Step Build Instructions
1. Open Power BI Desktop → **Get Data → Text/CSV** → import all 4 CSVs from the `powerbi/` folder.
2. In **Power Query Editor**: confirm data types — `rating`, `cost_for_two`, `votes` as Decimal/Whole
   Number; `is_unique_restaurant` as True/False; everything else as Text. Click **Close & Apply**.
3. Go to **Model view**. Drag `listing_id` from `Fact_Listings` to `listing_id` in `Bridge_Cuisines`,
   confirm 1:* . Repeat for `Bridge_RestTypes`. Drag `location` from `Fact_Listings` to `location` in
   `Dim_Location_Summary`, confirm *:1.
4. Go to **Report view → Home → New Measure**, paste in each DAX measure above.
5. Build Page 1: insert Card visuals for each KPI measure; bar chart with `location` (axis) and
   Total Listings (value), sorted descending, top N filter = 15; donut chart with `listing_type`.
   Add slicers for `location`, `online_order`, `book_table`, `rating_band`, `cost_bucket`.
6. Build Page 2–4 per the layout above using the same drag-and-drop pattern: field → axis/value well.
7. Apply Zomato brand color (`#CB202D`) as the theme accent via **View → Themes → Customize current theme**.
8. Save as `powerbi/Zomato_Bangalore_Dashboard.pbix`.

## Status
This guide is the blueprint Claude followed to build the dashboard live in Power BI Desktop via
computer-use (see chat for the build walkthrough and final screenshot).
