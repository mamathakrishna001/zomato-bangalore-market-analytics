# Requirements Traceability Matrix (RTM)

| | |
|---|---|
| **Project** | Zomato Bangalore Restaurant Market Analysis |
| **Purpose** | Trace every business requirement through functional requirements to the deliverable(s) that satisfy it, and the test/verification evidence |

| BRD ID | Business Requirement | FRD ID(s) | Deliverable / Implementation | Verified By |
|---|---|---|---|---|
| BR-1 | Listing density by locality | FR-15, FR-12 | Power BI: "Total Listings by location" bar chart (Market Overview, Executive Summary); `Dim_Location_Summary.listing_count` | UAT-04 |
| BR-2 | Avg rating/cost/votes by locality, cuisine, restaurant type | FR-14, FR-17, FR-20 | Power BI: Ratings & Quality page, Locality Deep Dive table; DAX measures Avg Rating / Avg Cost for Two | UAT-05, UAT-06 |
| BR-3 | Online ordering vs. rating/votes | FR-18 | Power BI: Service Features Impact page | UAT-07 |
| BR-4 | Table booking vs. rating/votes | FR-19 | Power BI: Service Features Impact page | UAT-07 |
| BR-5 | Top-performing restaurants and shared attributes | FR-17 | `docs/04_eda_insights.md` §9 (Top Performers table); Service Features Impact top-10-by-votes table | UAT-08 |
| BR-6 | Distinguish true duplicates from repeated listing-type rows | FR-5 | `is_unique_restaurant` flag in cleaned dataset and `Fact_Listings`; DAX measure "Unique Restaurants" | UAT-01 |
| BR-7 | Deliver as interactive, filterable dashboard | FR-21, FR-22 | `powerbi/Zomato_Bangalore_Dashboard.pbix` (5 pages) | UAT-09 |
| BR-8 | Document data quality issues and cleaning rules | FR-1–FR-7 | `docs/02_data_understanding.md`, `docs/03_data_cleaning_log.md` | UAT-02, UAT-03 |

## Coverage Check

- All 8 business requirements (BR-1 to BR-8) map to at least one functional requirement and one concrete deliverable. ✅
- All functional requirements in `09_FRD_functional_requirements_document.md` trace back to at least one business requirement. ✅
- No orphaned requirements (functional requirements with no business justification) identified. ✅

## Open Items

| Item | Status |
|---|---|
| Revenue/commission impact quantification | Not yet covered by any BR — flagged as a future-scope item in `07_final_report.md` |
| Locality opportunity-scoring model | Not yet covered by any BR — flagged as a future-scope item |
