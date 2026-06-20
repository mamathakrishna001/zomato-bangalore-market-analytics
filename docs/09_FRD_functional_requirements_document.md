# Functional Requirements Document (FRD)

| | |
|---|---|
| **Project** | Zomato Bangalore Restaurant Market Analysis |
| **Traces to** | `08_BRD_business_requirements_document.md` |
| **Related documents** | `02_data_understanding.md`, `05_powerbi_design_and_build_guide.md` |

## 1. Purpose

Translates the business requirements (BRD) into functional specifications: what the data pipeline must do, what the data model must look like, and what the dashboard must expose. Each functional requirement traces to one or more business requirements.

## 2. Functional Requirements — Data Pipeline

| ID | Requirement | Traces to | Implementation |
|---|---|---|---|
| FR-1 | System shall load the raw CSV with correct encoding (latin-1) without data loss | BR-8 | `scripts/01_clean_data.py` |
| FR-2 | System shall parse the `rate` field from text (`"4.1/5"`, `'NEW'`, `'-'`) into a nullable numeric `rating` field | BR-2, BR-8 | `01_clean_data.py` → `parse_rating()` |
| FR-3 | System shall parse `approx_cost(for two people)` from comma-formatted text into numeric `cost_for_two` | BR-2 | `01_clean_data.py` |
| FR-4 | System shall derive a single `primary_cuisine` and `primary_rest_type` from each multi-valued field | BR-2 | `01_clean_data.py` |
| FR-5 | System shall flag each row as belonging to a unique restaurant (`is_unique_restaurant`) based on first occurrence of `name` + `address` | BR-6 | `01_clean_data.py` |
| FR-6 | System shall derive `rating_band` (Excellent/Good/Average/Poor/Not Rated) and `cost_bucket` (Budget/Mid/Premium/Luxury) categorical fields | BR-2 | `01_clean_data.py` |
| FR-7 | System shall output a cleaned dataset and a run log documenting every transformation applied | BR-8 | `01_clean_data.py` → `docs/03_data_cleaning_log.md` |
| FR-8 | System shall reshape the cleaned dataset into a star schema: one fact table plus bridge tables for multi-valued cuisine and restaurant-type fields | BR-1–BR-5, BR-7 | `scripts/03_prepare_bi_data.py` |

## 3. Functional Requirements — Data Model (Star Schema)

| ID | Requirement | Object |
|---|---|---|
| FR-9 | Fact table shall carry one row per listing with a surrogate `listing_id` key | `Fact_Listings` |
| FR-10 | Bridge table shall map each `listing_id` to every individual cuisine it serves (many-to-many) | `Bridge_Cuisines` |
| FR-11 | Bridge table shall map each `listing_id` to every individual restaurant type it carries | `Bridge_RestTypes` |
| FR-12 | Dimension table shall pre-aggregate locality-level metrics (listing count, unique restaurants, avg rating/cost/votes, online order %, book table %) | `Dim_Location_Summary` |
| FR-13 | Relationships between Fact and bridge/dimension tables shall be one-to-many with single-direction filtering | Power BI data model |

## 4. Functional Requirements — Dashboard / Reporting Layer

| ID | Requirement | Traces to |
|---|---|---|
| FR-14 | Dashboard shall expose Total Listings, Unique Restaurants, Avg Rating, Avg Cost for Two, Total Votes, Online Order %, and Book Table % as reusable measures | BR-1, BR-2, BR-3, BR-4 |
| FR-15 | Dashboard shall provide a ranked view of listing count by locality (Top 15) | BR-1 |
| FR-16 | Dashboard shall provide a breakdown of listings by listing type (Delivery, Dine-out, Cafes, etc.) | BR-2 |
| FR-17 | Dashboard shall provide average rating by restaurant type and by cuisine, filtered to types/cuisines with a minimum sample size (≥ 50 listings) to avoid small-sample distortion | BR-2, BR-5 |
| FR-18 | Dashboard shall provide a side-by-side comparison of Avg Rating and Avg Votes for Online Order = Yes/No | BR-3 |
| FR-19 | Dashboard shall provide a side-by-side comparison of Avg Rating and Avg Votes for Book Table = Yes/No | BR-4 |
| FR-20 | Dashboard shall provide a full sortable table of all localities with listing count, unique restaurant count, avg rating, avg cost, avg votes, online order %, and book table % | BR-1, BR-2, FR-12 |
| FR-21 | Dashboard shall provide a single consolidated "Executive Summary" page combining the headline KPIs and top charts from the detail pages | BR-7 |
| FR-22 | Dashboard shall be navigable as multiple pages/views, each scoped to one analytical theme, rather than a single cluttered page | BR-7 |

## 5. Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-1 | The cleaning pipeline must be re-runnable end-to-end on a fresh copy of the raw CSV without manual steps |
| NFR-2 | All numeric KPIs must be defined once as a DAX measure, not hard-coded per visual |
| NFR-3 | All filters applied to a visual (e.g., minimum listing count) must be visible/documented, not silently hidden |
| NFR-4 | Documentation must allow the dashboard to be rebuilt from scratch using only the docs folder, without referring back to chat history or code comments |

## 6. Out of Scope (Functional)

- Real-time or scheduled data refresh (source is a static file).
- Row-level security / user access control (single-user analytical use case).
- Predictive modeling or forecasting (current scope is descriptive analytics; see `07_final_report.md` future-work section for proposed predictive extensions).

## 7. Requirements Traceability

See `11_RTM_requirements_traceability_matrix.md` for the full BRD → FRD → deliverable mapping.
