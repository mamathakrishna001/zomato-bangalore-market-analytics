# 02 — Data Understanding

## Source
- Dataset: [Zomato Bangalore Restaurants](https://www.kaggle.com/datasets/rajeshrampure/zomato-dataset) (Kaggle)
- File: `data/raw/zomato.csv`
- Size: ~574 MB, **51,717 rows × 17 columns**
- Encoding: `latin-1` (not UTF-8 — contains non-ASCII characters in names/addresses)
- Granularity: 1 row = 1 restaurant listing on Zomato (Bangalore)
- No time dimension — this is a single scraped snapshot, not a time series.

## Data Dictionary

| Column | Type (raw) | Description | Quality Notes |
|---|---|---|---|
| `url` | text | Zomato listing URL | 0 duplicates — reliable unique key |
| `address` | text | Full street address | Free text |
| `name` | text | Restaurant name | Some duplicate names = different branches (kept, since `url` is unique) |
| `online_order` | Yes/No | Accepts online orders | Clean, 2 values only |
| `book_table` | Yes/No | Accepts table booking | Clean, 2 values only |
| `rate` | text, e.g. `4.1/5` | Customer rating | 7,775 nulls; `'NEW'` (2,208 rows, not-yet-rated) and `'-'` placeholders mixed in; inconsistent spacing (`'3.9/5'` vs `'3.9 /5'`) → must be parsed to float |
| `votes` | int | Number of votes/reviews | Clean |
| `phone` | text | Phone number(s) | 1,208 nulls; not analytically useful — drop |
| `location` | text | Neighborhood/locality (93 unique) | 21 nulls |
| `rest_type` | text | Restaurant type, sometimes multi-valued e.g. `"Cafe, Casual Dining"` | 227 nulls; 93 raw unique combos — needs primary-type split |
| `dish_liked` | text | Comma-separated popular dishes | 28,078 nulls (54%) — too sparse for core KPIs, useful only for text/keyword analysis |
| `cuisines` | text | Comma-separated cuisines, e.g. `"North Indian, Chinese"` | 45 nulls; multi-valued — needs a primary-cuisine split for grouping |
| `approx_cost(for two people)` | text (numeric w/ commas) | Approx. cost for two, in ₹ | 346 nulls; stored as text with thousand-separator commas (e.g. `"1,200"`) → must clean and cast to numeric |
| `reviews_list` | text (stringified list of tuples) | Raw review text + per-review rating | Very large/free text; used only for optional NLP, not core KPIs |
| `menu_item` | text (stringified list) | Menu items listed | Mostly empty lists; low value for KPIs |
| `listed_in(type)` | text, 7 categories | Listing category: Buffet, Cafes, Delivery, Desserts, Dine-out, Drinks & nightlife, Pubs and bars | Clean — a restaurant can appear multiple times under different `listed_in(type)` (this is why `name`/`address` repeat — **not true duplicates**, each row is a distinct listing context) |
| `listed_in(city)` | text, 30 categories | Zomato's city-area grouping used for browsing | Clean, distinct from `location` (93 finer-grained localities) |

## Key Structural Finding
Restaurants can appear multiple times in the dataset — once per `listed_in(type)` they're listed under
(e.g., a restaurant offering both "Delivery" and "Dine-out" gets 2 rows). **`url` is the true unique
identifier per listing-context row; the same restaurant (by name+address) can legitimately repeat.**
This must be documented clearly so dashboard "restaurant count" KPIs are not silently double-counted —
we will provide both a "listing count" KPI and a "unique restaurant count" KPI (distinct `name`+`address`).

## Data Quality Issues Summary
| Issue | Column(s) | Resolution Plan |
|---|---|---|
| Rating stored as string with `/5`, inconsistent spacing, `'NEW'`/`'-'` placeholders | `rate` | Strip suffix, convert to float, treat `NEW`/`-` as null (not-yet-rated) |
| Cost stored as text with commas | `approx_cost(for two people)` | Remove commas, cast to int |
| Multi-valued categorical fields | `cuisines`, `rest_type` | Derive `primary_cuisine`, `primary_rest_type` (first listed) + keep full list for filtering |
| High null % | `dish_liked` (54%), `phone` (2%) | Keep `dish_liked` for optional text mining; drop `phone` (not needed for analysis) |
| Row-level pseudo-duplication by design (`listed_in(type)`) | whole table | Document clearly; add `is_unique_restaurant` flag (first occurrence by name+address) |
| Encoding | whole table | Read with `latin-1`, re-save cleaned file as UTF-8 |
| Irrelevant to KPIs | `url`, `phone`, `menu_item`, `reviews_list` | Retain `url` as ID; drop or archive the rest for the core model (kept in a separate text table for optional NLP) |

## Final Column Roles for the Cleaned Model
- **Identifiers:** `url` (row id), `name`, `address`
- **Dimensions:** `location`, `listed_in(city)`, `rest_type`, `primary_rest_type`, `cuisines`, `primary_cuisine`, `listed_in(type)`, `online_order`, `book_table`
- **Measures:** `rate` (→ `rating`), `votes`, `approx_cost(for two people)` (→ `cost_for_two`)
- **Derived:** `rating_band`, `cost_bucket`, `is_unique_restaurant`
