# Stakeholder Register & RACI Matrix

| | |
|---|---|
| **Project** | Zomato Bangalore Restaurant Market Analysis |
| **Related documents** | `08_BRD_business_requirements_document.md` |

## 1. Stakeholder Register

| Stakeholder | Role / Interest | Influence | Engagement approach |
|---|---|---|---|
| Business Expansion / Strategy team | Decide where to open or expand new outlets | High | Dashboard (Locality Deep Dive page), final report recommendations |
| Marketing team | Target campaigns by cuisine/locality | Medium | Dashboard (Ratings & Quality, Market Overview pages) |
| Restaurant partners | Improve own listing performance | Medium | Final report recommendations, service-feature findings |
| Zomato Product/Ops | Validate impact of online order / table booking features | High | Service Features Impact page, recommendation to run a controlled experiment |
| Business Analyst (this project) | Deliver the analysis end-to-end | High | N/A — project owner |

## 2. RACI Matrix

R = Responsible, A = Accountable, C = Consulted, I = Informed

| Activity | Business Analyst | Expansion Team | Marketing | Restaurant Partners | Product/Ops |
|---|---|---|---|---|---|
| Define business requirements (BRD) | A/R | C | C | I | C |
| Data profiling & quality assessment | A/R | I | I | I | I |
| Data cleaning pipeline | A/R | I | I | I | I |
| Star-schema data modeling | A/R | I | I | I | I |
| EDA & insight generation | A/R | C | C | I | C |
| Dashboard design (Power BI) | A/R | C | C | I | C |
| Dashboard build | A/R | I | I | I | I |
| UAT / sign-off | A/R | C | I | I | C |
| Final recommendations | A/R | A | C | I | C |
| Acting on recommendations (e.g. new-outlet decision, feature experiment) | C | A/R | A/R | A/R | A/R |

## 3. Communication Plan

| Audience | Artifact | Frequency (in a real engagement) |
|---|---|---|
| Expansion / Marketing teams | Power BI dashboard (self-serve) | Continuous / on-demand |
| Product/Ops | Service Features Impact findings + experiment recommendation | One-time briefing at project close |
| All stakeholders | Final report (`07_final_report.md`) | One-time at project close |
