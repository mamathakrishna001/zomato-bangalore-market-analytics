# Business Requirements Document (BRD)

| | |
|---|---|
| **Project** | Zomato Bangalore Restaurant Market Analysis |
| **Document owner** | Business Analyst |
| **Status** | Approved (self-directed project — see Sign-off) |
| **Related documents** | `01_business_understanding.md`, `09_FRD_functional_requirements_document.md` |

## 1. Purpose

This BRD captures the business need, scope, stakeholders, and success criteria for an analysis of the Bangalore restaurant market on Zomato. It is the reference point against which the functional requirements (FRD) and the final deliverables are validated.

## 2. Background

Zomato's Bangalore restaurant listings represent a large, varied, and partially messy dataset (51,717 rows) covering pricing, ratings, cuisine, service features, and location. No structured analysis currently exists that ties these attributes back to a decision a restaurant operator, an expansion team, or Zomato itself could act on. This project closes that gap.

## 3. Business Objectives

| ID | Objective |
|---|---|
| BO-1 | Understand competitive density and market concentration across Bangalore localities |
| BO-2 | Identify which restaurant attributes (cuisine, format, service features, price) correlate with higher ratings and engagement |
| BO-3 | Quantify the relationship between service features (online ordering, table booking) and customer engagement |
| BO-4 | Produce a reusable, interactive reporting layer (dashboard) rather than a one-off analysis |
| BO-5 | Translate findings into specific, actionable recommendations for restaurant operators and the platform |

## 4. Stakeholders

| Stakeholder | Interest |
|---|---|
| Business Expansion / Strategy team | Where to open or expand a new outlet |
| Marketing team | Which cuisines/localities to target with campaigns |
| Restaurant partners | How to improve their own listing's performance |
| Zomato Product/Ops | Impact of online ordering and table booking features on engagement |

## 5. Scope

### In scope
- Single-city analysis: Bangalore.
- Cross-sectional analysis (the dataset is a single scrape, not a time series — no trend-over-time analysis is possible).
- Restaurant-listing-level attributes: location, cuisine, cost, rating, votes, online order, table booking, restaurant type.
- Deliverables: cleaned dataset, EDA chart pack, interactive Power BI dashboard, written findings/recommendations.

### Out of scope
- Delivery time / logistics data (not present in source).
- Customer-level / order-level data (not present in source).
- Financial or revenue data (not present in source — any revenue discussion is a modeled estimate, not actuals).
- Multi-city comparison (source is Bangalore-only).

## 6. Business Requirements

| ID | Requirement | Priority |
|---|---|---|
| BR-1 | Provide a breakdown of restaurant listing density by locality | Must |
| BR-2 | Provide average rating, cost, and votes segmented by locality, cuisine, and restaurant type | Must |
| BR-3 | Quantify the difference in rating/votes between restaurants with and without online ordering | Must |
| BR-4 | Quantify the difference in rating/votes between restaurants with and without table booking | Must |
| BR-5 | Identify the top-performing restaurants and the attributes they share | Should |
| BR-6 | Distinguish true duplicate restaurants from repeated listing-type rows so counts are not inflated | Must |
| BR-7 | Deliver the analysis as an interactive, filterable dashboard, not a static report only | Must |
| BR-8 | Document data quality issues and the cleaning rules applied, for auditability | Should |

## 7. Assumptions

- The Kaggle snapshot is reasonably representative of the live Zomato Bangalore listings at time of scrape.
- "Votes" is an acceptable proxy for customer engagement in the absence of order-volume data.
- A listing's `rate` field reflects genuine customer feedback rather than manipulated reviews.

## 8. Constraints

- No live database or API access — analysis is based on a static CSV export.
- No revenue, commission, or order-volume data is available, so any business-impact estimate must be clearly labeled as a model/estimate, not measured fact.
- Single-city scope limits generalizability to other Zomato markets.

## 9. Success Criteria

| Criterion | Measure |
|---|---|
| Data quality issues resolved | All issues logged in data understanding doc have a corresponding fix in the cleaning log |
| KPIs reportable | All KPIs in section 6 are present as DAX measures / calculated fields in the dashboard |
| Actionable output | Final report ties every recommendation to a specific quantified finding |
| Reusability | Star-schema tables can be refreshed from a new CSV export without re-deriving the model |

## 10. Sign-off

| Role | Name | Date |
|---|---|---|
| Business Sponsor | (self-directed project) | — |
| Business Analyst | Mude Mamatha | 2026-06-20 |
