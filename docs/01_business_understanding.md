# 01 — Business Understanding

## Project Title
Zomato Bangalore Restaurants — Market & Performance Analysis

## Background
Zomato is a restaurant discovery and food delivery platform. The dataset contains ~51,700 restaurant
listings scraped from Zomato for the city of Bangalore, covering location, cuisine, cost, ratings,
votes, online ordering, table booking, and restaurant type.

A business / marketing team at a food-tech company (or a restaurant chain deciding where to open a new
outlet) needs to understand the Bangalore restaurant market: where the competition is concentrated,
what drives high ratings, how pricing varies by area and cuisine, and which services (online ordering,
table booking) correlate with better performance.

## Business Problem
"Where and how should a restaurant operator position a new outlet in Bangalore, and what factors
correlate with higher customer ratings and engagement (votes)?"

## Objectives
1. Map the competitive landscape: restaurant density and cuisine mix by locality.
2. Understand pricing patterns (cost for two) across localities, cuisines, and restaurant types.
3. Identify what is associated with higher ratings — service options (online order/table booking),
   restaurant type, cuisine, cost tier.
4. Quantify the impact of online ordering and table booking availability on votes/engagement.
5. Surface top-performing restaurants, cuisines, and localities as benchmarks.

## Key Stakeholders
- Business Expansion / Strategy team (where to open new outlets)
- Marketing team (which cuisines/areas to target campaigns)
- Restaurant partners (how to improve their own listing performance)
- Product/Ops team at Zomato (impact of online order & booking features)

## Key Business Questions (KBQs)
1. Which localities have the most restaurants, and which are under-served (high demand signal,
   low supply)?
2. What is the average cost for two across localities and cuisines?
3. Do restaurants offering online ordering / table booking have higher average ratings and votes?
4. Which cuisines and restaurant types dominate, and which have the highest average ratings?
5. Is there a relationship between cost and rating ("do expensive restaurants rate better")?
6. Who are the top 10 highest-rated / most-voted restaurants, and what do they have in common?
7. Which restaurant types (Casual Dining, Quick Bites, Cafe, etc.) are most common and best rated?

## KPIs / Metrics to Track
| KPI | Definition |
|---|---|
| Restaurant Count | Number of unique listings per locality / cuisine / type |
| Avg Rating | Mean of `rate` (cleaned to numeric out of 5) |
| Avg Cost for Two | Mean of `approx_cost(for two people)` |
| Avg Votes | Mean of `votes` — proxy for engagement/popularity |
| Online Order % | % of restaurants offering online ordering |
| Table Booking % | % of restaurants offering table booking |
| Rating Band Distribution | % of restaurants in Excellent (4+), Good (3.5–4), Average (3–3.5), Poor (<3) |

## Scope
- Geography: Bangalore only (single-city dataset).
- Time: Single snapshot (no historical/time-series field) — analysis is cross-sectional, not trend-based.
- Out of scope: Delivery time data, customer-level data, financial/revenue data (not present in source).

## Deliverables
1. Cleaned, analysis-ready dataset (`data/cleaned/`)
2. Python EDA notebook/scripts + chart pack (`scripts/`, `dashboards/eda_charts/`)
3. Power BI dashboard (.pbix) — interactive
4. Full documentation set (this `docs/` folder)
5. Executive summary report with recommendations
