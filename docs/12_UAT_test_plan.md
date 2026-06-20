# UAT Test Plan & Test Cases

| | |
|---|---|
| **Project** | Zomato Bangalore Restaurant Market Analysis |
| **Scope** | Verify the cleaning pipeline, star-schema outputs, and dashboard against the BRD/FRD before sign-off |
| **Related documents** | `11_RTM_requirements_traceability_matrix.md` |

## Test Cases

| ID | Test Case | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| UAT-01 | Unique restaurant flag is correct | Run `01_clean_data.py`; count rows where `is_unique_restaurant = True` | Count reflects first-occurrence-by-(name, address) logic, materially less than total row count | 12,499 unique of 51,696 total rows | ✅ Pass |
| UAT-02 | Rating field fully numeric or null | Inspect cleaned `rating` column dtype and value range | All non-null values between 1.0 and 5.0; no string artifacts (`/5`, `NEW`, `-`) remain | dtype float64, range 1.8–4.9, 10,031 nulls (was 'NEW'/blank) | ✅ Pass |
| UAT-03 | Cost field fully numeric | Inspect cleaned `cost_for_two` column | No commas or non-numeric characters; dtype numeric | dtype float64, range ₹40–₹6,000 | ✅ Pass |
| UAT-04 | Locality listing counts reconcile | Sum `listing_count` across `Dim_Location_Summary` | Sum equals total row count of `Fact_Listings` (51,696) | Confirmed via groupby sum | ✅ Pass |
| UAT-05 | Cuisine bridge table is exploded correctly | Spot-check a multi-cuisine listing (e.g. "North Indian, Chinese") in `Bridge_Cuisines` | Two rows exist for that `listing_id`, one per cuisine, no leading/trailing whitespace | Verified on sample listing_id | ✅ Pass |
| UAT-06 | Minimum sample-size filter applied on rating-by-type/cuisine charts | Open Power BI "Avg Rating by primary_rest_type" visual; inspect visual-level filter | Filter present: Total Listings ≥ 50 | Filter confirmed in Filters pane | ✅ Pass |
| UAT-07 | Online order / book table comparison renders both categories | Open Service Features Impact page | Both "Yes" and "No" bars present for each feature with non-zero values | Confirmed visually | ✅ Pass |
| UAT-08 | Top-10-by-votes table matches EDA findings | Compare Power BI table to `docs/04_eda_insights.md` §9 | Same top 5 restaurants (Byg Brewski, Toit, Truffles, AB's, The Black Pearl) appear in both | Confirmed | ✅ Pass |
| UAT-09 | Dashboard is navigable across all pages without broken visuals | Click through all 5 Power BI pages | Every page loads, every visual renders data (no "Visual has errors" or blank fields) | Confirmed | ✅ Pass |
| UAT-10 | KPI cards on Executive Summary match Market Overview page | Compare card values: Total Listings, Unique Restaurants, Avg Rating, Avg Cost for Two, Online Order %, Book Table % | Identical values on both pages (52K / 12K / 3.70 / 555.43 / 58.89% / 12.47%) | Confirmed | ✅ Pass |
| UAT-11 | Re-running cleaning pipeline is idempotent | Run `01_clean_data.py` twice in a row | Second run produces identical output file (same row/column counts) and does not error | Confirmed | ✅ Pass |

## Defects Log

| ID | Description | Severity | Resolution |
|---|---|---|---|
| DEF-01 | Initial restaurant-type chart was sorted by average rating instead of listing volume, surfacing statistically tiny categories (e.g. single-listing types) at the top | Medium | Added a "Total Listings ≥ 50" visual-level filter (see UAT-06) before sign-off |
| DEF-02 | Cards briefly showed cross-filtered values instead of grand totals when a bar was left selected | Low | Confirmed as expected Power BI cross-filter behavior, not a defect; documented for dashboard users |

## Sign-off

All test cases passed. No open defects of Medium or higher severity remain unresolved. Dashboard and cleaned data approved for use as the basis of `07_final_report.md`.
