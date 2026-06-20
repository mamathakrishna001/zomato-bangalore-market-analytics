# 07 — Final Report: Zomato Bangalore Restaurant Market Analysis

## Executive Summary
This project analyzed 51,717 Zomato restaurant listings across Bangalore (51,696 after cleaning,
representing 12,490 unique restaurants) to answer a core business question for restaurant
operators and Zomato's strategy team: **where and how should a restaurant be positioned to
maximize rating and customer engagement in the Bangalore market?**

The analysis followed a full data-analyst workflow: business understanding → data understanding →
cleaning → exploratory analysis (Python) → dashboarding (Power BI) → insight
synthesis. All deliverables are version-controlled in this project folder.

## Key Findings

1. **Market concentration.** Competition is heavily concentrated in tech-corridor localities —
   BTM (5,124 listings), HSR, Koramangala, JP Nagar, Whitefield, Indiranagar. These are saturated;
   smaller localities may offer lower-competition entry points but lack demand signals in this
   dataset (no footfall/population data available).

2. **Table booking is the single strongest performance signal.** Restaurants offering table
   booking average **4.14★ vs 3.62★** for those that don't, and **~7x the votes** (1,147 vs 161
   average). This dwarfs the effect of online ordering (3.72★ vs 3.66★). Table booking strongly
   correlates with premium, full-service dine-in formats.

3. **Format and cuisine quality vary widely.** Quick Bites (the most common format, 14,266
   listings) rates lowest among major formats (3.55★); Pubs, Bars, and Dessert Parlors rate
   highest (3.89–4.10★). Niche/premium cuisines (Modern Indian 4.31★, European 4.26★, Japanese
   4.19★) outrate mass-market staples (North Indian, South Indian) despite far lower volume.

4. **Price correlates with quality, moderately.** Avg rating rises from 3.56★ (Budget, <₹300) to
   4.06★ (Luxury, ₹1000+) — a real but moderate relationship (r ≈ 0.39 cost↔rating). Premium
   pricing is associated with — not a guarantee of — higher ratings.

5. **Top performers share a profile.** The most-voted restaurants (Byg Brewski Brewing Company,
   Toit, Truffles, AB's Absolute Barbecues) are large-format breweries/dine-out venues: premium
   pricing (₹900–2,000 for two), table booking enabled, 4.4★+ ratings.

6. **19% of listings are unrated** ("NEW" on Zomato) — a meaningful population of fresh entrants
   not yet reflected in rating-based benchmarks.

## Recommendations

| For | Recommendation |
|---|---|
| **New restaurant launch (expansion)** | Avoid the most saturated localities (BTM, HSR, Koramangala) unless differentiating strongly; consider table booking + a premium or niche-cuisine positioning from day one — it's the single biggest lever found in the data. |
| **Existing Quick Bites / Delivery-only operators** | Quality ceiling is structurally lower for this format; consider adding a dine-in or booking option to lift perceived quality and engagement. |
| **Marketing / cuisine strategy** | Promote niche cuisines (Japanese, European, Modern Indian, BBQ) as premium differentiators rather than competing head-on in North/South Indian volume segments. |
| **Zomato product team** | Investigate whether promoting table-booking adoption among mid-tier restaurants lifts their engagement — the correlation here is strong enough to justify a controlled experiment. |
| **Further analysis** | This dataset lacks footfall, revenue, and time-series data. A valuable follow-up would pair this with delivery-time data, review-text sentiment (the `reviews_list` field, unused here), or city-area demographic data to validate causal hypotheses. |

## Methodology Recap
1. **Business Understanding** — `docs/01_business_understanding.md`
2. **Data Understanding & Dictionary** — `docs/02_data_understanding.md`
3. **Data Cleaning** — `scripts/01_clean_data.py`, log in `docs/03_data_cleaning_log.md`
4. **EDA** — `scripts/02_eda.py`, insights in `docs/04_eda_insights.md`, charts in
   `dashboards/eda_charts/`
5. **BI Data Prep (star schema)** — `scripts/03_prepare_bi_data.py` → `data/cleaned/Fact_Listings.csv`,
   `Bridge_Cuisines.csv`, `Bridge_RestTypes.csv`, `Dim_Location_Summary.csv`
6. **Power BI Dashboard** — built live in Power BI Desktop, 5 pages (Executive Summary, Market
   Overview, Ratings & Quality, Service Features Impact, Locality Deep Dive), saved at
   `powerbi/Zomato_Bangalore_Dashboard.pbix`. Design spec: `docs/05_powerbi_design_and_build_guide.md`

## Deliverables Checklist
- [x] Raw and cleaned datasets
- [x] Data dictionary and cleaning log
- [x] Python EDA with chart pack
- [x] Star-schema BI-ready tables
- [x] Power BI interactive dashboard (5 pages, working DAX measures)
- [x] This executive summary

## Limitations
- Single-snapshot dataset — no trend/time-series analysis possible.
- `location` field is self-reported on Zomato and may not perfectly reflect formal locality
  boundaries.
- Listings repeat per `listing_in(type)` by design (see `docs/02_data_understanding.md`) — all KPIs
  in this report distinguish "listings" from "unique restaurants" where relevant.
- No cost/revenue/footfall ground truth — recommendations are directional, not causal.
