# Data Mapping Document (Source → Target)

| | |
|---|---|
| **Project** | Zomato Bangalore Restaurant Market Analysis |
| **Source** | `data/raw/zomato.csv` |
| **Targets** | `data/cleaned/zomato_cleaned.csv`, `Fact_Listings`, `Bridge_Cuisines`, `Bridge_RestTypes`, `Dim_Location_Summary` |
| **Related documents** | `02_data_understanding.md`, `03_data_cleaning_log.md` |

## 1. Source → Cleaned Dataset Mapping

| Source Column | Target Column | Transformation | Notes |
|---|---|---|---|
| `url` | `url` | None (retained as row identifier) | Unique per listing-context row |
| `address` | `address` | Stripped whitespace | — |
| `name` | `name` | Stripped whitespace | — |
| `online_order` | `online_order` | Stripped whitespace | Values: Yes/No |
| `book_table` | `book_table` | Stripped whitespace | Values: Yes/No |
| `rate` | `rating` | Split on `/`, cast to float; `'NEW'`/`'-'`/blank → null | Renamed; e.g. `"4.1/5"` → `4.1` |
| `votes` | `votes` | None | Already clean integer |
| `phone` | *(dropped)* | — | Not needed for analytical KPIs |
| `location` | `location` | None | 21 null rows dropped |
| `rest_type` | `rest_type` (full) + `primary_rest_type` (derived) | Split on `,`, first value → `primary_rest_type` | Multi-valued source field |
| `dish_liked` | *(dropped)* | — | 54% null, not used in core model |
| `cuisines` | `cuisines` (full) + `primary_cuisine` (derived) | Split on `,`, first value → `primary_cuisine` | Multi-valued source field |
| `approx_cost(for two people)` | `cost_for_two` | Remove thousands separators (`,`), cast to numeric | Renamed |
| `reviews_list` | *(dropped)* | — | Free text, reserved for optional NLP extension |
| `menu_item` | *(dropped)* | — | Mostly empty lists |
| `listed_in(type)` | `listing_type` | None (renamed) | 7 categories: Buffet, Cafes, Delivery, Desserts, Dine-out, Drinks & nightlife, Pubs and bars |
| `listed_in(city)` | `listing_city` | None (renamed) | 30 categories, coarser than `location` |
| *(derived)* | `rating_band` | Bucketed from `rating`: Excellent ≥4.0, Good 3.5–3.9, Average 3.0–3.4, Poor <3.0, Not Rated (null) | New field |
| *(derived)* | `cost_bucket` | Bucketed from `cost_for_two`: Budget <300, Mid 300–599, Premium 600–999, Luxury ≥1000 | New field |
| *(derived)* | `is_unique_restaurant` | Boolean: `True` for first occurrence of (`name`, `address`), `False` for repeats | Distinguishes true duplicates from repeated listing-type rows |

**Row-level filter applied:** rows with null `location` are dropped (21 rows). All other rows pass through with nulls retained where the source value was genuinely missing.

## 2. Cleaned Dataset → Star Schema Mapping

### 2.1 `Fact_Listings` (one row per listing)

| Cleaned Column | Fact Column | Notes |
|---|---|---|
| *(generated)* | `listing_id` | Surrogate key = row index + 1 |
| `url`, `name`, `address`, `location`, `listing_city` | same | Direct copy |
| `online_order`, `book_table`, `votes`, `rating`, `cost_for_two` | same | Direct copy |
| `primary_cuisine`, `primary_rest_type`, `listing_type` | same | Direct copy |
| `rating_band`, `cost_bucket`, `is_unique_restaurant` | same | Direct copy |

### 2.2 `Bridge_Cuisines` (one row per listing × individual cuisine)

| Cleaned Column | Bridge Column | Transformation |
|---|---|---|
| `listing_id` | `listing_id` | From Fact_Listings join key |
| `cuisines` | `cuisine` | Split on `,`, explode to one row per cuisine, trim whitespace |

Result: 126,819 rows from 51,696 listings (avg ~2.5 cuisines per listing); 107 unique cuisine values.

### 2.3 `Bridge_RestTypes` (one row per listing × individual restaurant type)

| Cleaned Column | Bridge Column | Transformation |
|---|---|---|
| `listing_id` | `listing_id` | From Fact_Listings join key |
| `rest_type` | `rest_type_single` | Split on `,`, explode to one row per type, trim whitespace |

Result: 59,217 rows; 25 unique restaurant-type values.

### 2.4 `Dim_Location_Summary` (one row per locality)

| Source (aggregated from Fact_Listings) | Target Column | Aggregation |
|---|---|---|
| `listing_id` | `listing_count` | COUNT |
| `is_unique_restaurant` | `unique_restaurant_count` | SUM (of True) |
| `rating` | `avg_rating` | MEAN |
| `cost_for_two` | `avg_cost_for_two` | MEAN |
| `votes` | `avg_votes` | MEAN |
| `online_order` | `online_order_pct` | % rows = "Yes" |
| `book_table` | `book_table_pct` | % rows = "Yes" |

Grouped by `location`. Result: 93 rows, one per locality.

## 3. Join Keys Summary

| Relationship | Cardinality |
|---|---|
| `Fact_Listings.listing_id` → `Bridge_Cuisines.listing_id` | One-to-many |
| `Fact_Listings.listing_id` → `Bridge_RestTypes.listing_id` | One-to-many |
| `Fact_Listings.location` → `Dim_Location_Summary.location` | Many-to-one |

## 4. Reprocessing Instructions

To regenerate all targets from a fresh raw CSV:
```
python scripts/01_clean_data.py      # raw → cleaned
python scripts/03_prepare_bi_data.py # cleaned → star schema CSVs
```
Both scripts are idempotent — re-running overwrites prior outputs without manual cleanup.
