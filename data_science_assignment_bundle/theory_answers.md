# Data Science Assignment — Theory Answers

## 1. Three daily apps and how they use data

1. **Instagram:** Uses likes, comments, watch time, shares, and interests to personalize the feed and Reels recommendations.
2. **Zomato:** Uses location, previous orders, cuisine preferences, restaurant ratings, and delivery history to recommend restaurants and estimate delivery times.
3. **Paytm:** Uses transaction records and spending patterns to categorize expenses and help detect potentially suspicious transactions.

## 2. Skills important for a Data Scientist

| Statistics | Programming | Domain Knowledge |
|---|---|---|
| **Probability:** Estimates the likelihood of an event. Example: estimating the probability that an online shopper will purchase an item. | **Python:** Cleans and analyzes data. Example: analyzing sales records to find best-selling products. | **Business understanding:** Connects analysis to business goals. Example: investigating why online store sales declined. |
| **Hypothesis testing:** Evaluates whether an observed difference is statistically meaningful. Example: testing whether a new website design improves conversions. | **SQL:** Retrieves and aggregates data from databases. Example: calculating monthly revenue. | **E-commerce knowledge:** Helps interpret shopping behavior. Example: recommending products based on browsing and purchase history. |

## 3. Data-driven music recommendations

A music streaming app can analyze listening history, favorite artists, genres, likes, and skipped songs. A recommendation model can find patterns among users with similar interests. It can then recommend songs that match the listener's preferences. The app can use plays, skips, and likes to evaluate and improve future recommendations.

## 4. Innovative use of data science in e-commerce

E-commerce companies use recommendation systems to personalize shopping. These systems analyze browsing history, previous purchases, product views, and customer preferences to suggest relevant products. For example, a store may recommend running shoes to a customer who often browses fitness products. This can improve product discovery, engagement, and sales.

## 5. Data science project problem definition

**Project:** Personalized Instagram Feed Recommendation

**Business goal:** Improve user engagement by showing posts and Reels relevant to each user.

**Problem definition:** Predict which posts a user is likely to find relevant and engage with.

**Data needed:** User interactions, likes, comments, shares, watch time, post categories, timestamps, and historical engagement.

**Success metrics:** Engagement rate, watch time, likes, shares, and retention.

## 6. Feature engineering for online food orders

1. **Order hour:** Extract the hour from the order timestamp. This helps identify lunch/dinner peaks and forecast demand.
2. **Delivery delay:** Subtract estimated delivery duration from actual duration. This helps analyze delays and predict delivery performance.
3. **Restaurant average rating:** Calculate each restaurant's historical average rating. This can help restaurant recommendations and customer-satisfaction analysis.

## 7. Git and GitHub for notebook version management

Git records changes over time, allowing a developer to inspect earlier versions and revert unwanted changes. GitHub stores a shared remote copy and supports collaboration through branches, reviews, and pull requests. This reduces the need to create confusing files such as `analysis_v1.ipynb`, `analysis_final2.ipynb`, and `analysis_really_final.ipynb`. Jupyter notebooks can be difficult to diff because they contain outputs and metadata, so tools such as nbdime can help compare notebook changes.
