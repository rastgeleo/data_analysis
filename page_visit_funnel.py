import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(visits,
                       cart,
                       how='left')

print(visits_cart.head())

# How long is the merged dataframe?
visits_count = visits_cart.shape[0]
print(visits_count)

# How many of the timestamps are null for the column cart_time?
cart_null_count = visits_cart[visits_cart.cart_time.isnull()].shape[0]
print(cart_null_count)

# What percentage of users who visited did not place a t-shirt in their cart?
ratio_nullcart_visits = float(cart_null_count) / float(visits_count)

print(ratio_nullcart_visits)

# What percentage of users put items in their cart did not proceed to checkout?
cart_checkout = pd.merge(cart,
                         checkout,
                         how="left")
cart_count = cart_checkout.shape[0]

checkout_null_count = cart_checkout[cart_checkout.checkout_time.isnull()]\
    .shape[0]
print(float(checkout_null_count)/float(cart_count))

# Merge all four steps of the funnel using left merges

all_data = visits.merge(cart, how='left').merge(checkout, how='left')\
    .merge(purchase, how='left')

print(all_data.head())

# What percentage of users proceeded to checkout but did not purchase a t-shirt
# ?

checkout_count = all_data[all_data.checkout_time.notnull()].shape[0]
print(checkout_count)
purchase_null_count = all_data[(all_data.checkout_time.notnull()) &
                               (all_data.purchase_time.isnull())
                               ].shape[0]
print(purchase_null_count)
print(float(purchase_null_count)/float(checkout_count))

# Which step of the funnel is weakest
# Visits to cart

# Average time from initial visit to final purchase

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
