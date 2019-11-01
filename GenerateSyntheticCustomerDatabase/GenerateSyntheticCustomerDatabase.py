from mimesis import Person, Address, Business, Payment, Text

from scipy.stats import pareto
import pandas as pd
import numpy as np

import sqlite3
import os

# Note: we don't ever store user passwords as clear text!!!
# To emulate salting and hashing the user passwords:
import hashlib
import uuid

# However, we should really use a dedicated password hashing
# package, such as passlib. However, this is out of scope
# for this script e.g:
# import passlib

np.random.seed(42)  # To make our analysis reproducible

person = Person()
address = Address()
business = Business()
payment = Payment()
text = Text()

##################################################
### Define a couple of convenience functions:
##################################################


def hashed_passwd(passwd):
    """We should never entertain the idea of storing users' passwords
    as plaintext. This function performs a basic salting and hashing
    of a password input. This function should *never* be used in a
    production setting; if you need to securely store salted and hashed
    passwords, use a dedicated package such as passlib."""
    salt = uuid.uuid4().hex
    return hashlib.sha512(passwd.encode('utf-8')
                          + salt.encode('utf-8')).hexdigest()


def account_balance():
    """Generate account balances according to a Pareto distribution.
    We should expect balances to be distributed as with other income
    distributions.  The power exponent is chosen here to replicate
    the 80-20 rule."""
    return pareto.rvs(1.161)


def generate_sales(df, age='age', account_balance='account_balance',
                   marketing_level='marketing_level', min_age=25,
                   max_age=35, noise_ampl=10):
    """Generate sales as a linear function of age (as a weak power), account
    balance and the interaction between a marketing campaign and the age
    bracket it was intended for, plus a small amount of noise."""
    noise = noise_ampl*np.random.normal(0.01, 1.7, df.shape[0])
    gated_age = np.heaviside(df[age] - min_age, 0.5) - np.heaviside(df[age] - max_age, 0.5)
    return 0.01*pow(np.abs(df[age] - 30), 2.5) + df[age] + 50*df[marketing_level]*gated_age + 2*df[account_balance] + noise


##################################################

##################################################
### Generate a DataFrame of user information
##################################################
# Generate 10,000 rows of the following:
# user_id, first_name, last_name, email, password, address,
# birth_date, credit_card_num, credit_card_exp, security_answer,
# account_balance

user_df = pd.DataFrame([[x, person.name(), person.surname(), person.gender(),
                        person.email(), hashed_passwd(person.password()),
                        address.address(), person.age(),
                        payment.credit_card_number(),
                        payment.credit_card_expiration_date(), text.word(),
                        account_balance(), np.random.randint(1, 11)]
                        for x in range(10000)])

user_df.columns = ["user_id", "first_name", "last_name",
                   "gender", "email", "password_hashed", "address",
                   "age", "credit_card_num", "credit_card_exp",
                   "security_answer", "account_balance",
                   "marketing_level"]

# Generate sales, based on a noisy linear model
user_df['sales'] = generate_sales(user_df)
user_df['sales'] = user_df['sales'] - user_df['sales'].min()
user_df['sales'] /= 40

print("Summary statistics on numerical data:")
print(user_df.describe())

##################################################

##################################################
### Scuff the data up a bit!
##################################################
# We'll 'disappear' 10% of some columns, and create
# some dupes


def makeDataMissing(df, col_name, frac=0.1):
    """Randomly assign a fraction of a column, col_name,
    of a dataframe, df, as missing (np.nan).
    This makes use of the sample method associated with
    Series and DataFrame objects.

    A copy of the column is returned."""
    rnd_Idx = df.sample(frac=frac).index
    col_out =  df[col_name].copy()
    col_out[rnd_Idx] = np.nan
    return col_out


def makeDupes(df, frac=0.1):
    """Take a DataFrame, df, and randomly append
    a fraction of its own rows."""
    rnd_Idx = df.sample(frac=frac).index
    return df.append(df.loc[rnd_Idx, :])

# Ten percent of customers weren't comfortable with volunteering their gender:
user_df['gender'] = makeDataMissing(user_df, 'gender')

# others couldn't be bothered with the address:
user_df['address'] = makeDataMissing(user_df, 'address')

# We'll apply duplicates later.

##################################################

##################################################
### Perform some Exploratory Data Analysis
##################################################

user_df.sample(5)

user_df.describe()

# Note the median balance is 1.8, while the mean is 5.3
# Recall we generated a heavily skewed distribution!

# We designed it according to the famous "80-20 rule"
# The top twenty percent own 80% of the balances.
# Let's test it. Take the 80th percentile:
critical80 = np.quantile(user_df["account_balance"], 0.8)
## 4.013269256450965

the_few = user_df.loc[user_df["account_balance"] > critical80,
                      "account_balance"].sum()

tot_balance = user_df["account_balance"].sum()

the_few/tot_balance
## 0.7298469832819879
# So here, the top 20% 'only' have 73% of the account balance

# Plot the Pareto distribution
user_df['log_account_balance'] = np.log10(user_df['account_balance'])
user_df['log_account_balance'].hist(bins=20)

# Some limitations of mimesis
# If you want realistic distributions of certain numerical variables
# then you should simulate populations yourself. E.g.:

user_df["age"].plot(kind="kde")

# The way ages are generated are not exactly samples of any real population!
# This will depend on the underlying demographic dynamics.

from pandas.plotting import scatter_matrix
scatter_matrix(user_df[['age', 'account_balance', 'marketing_level', 'sales']])

import seaborn as sns

sns.pairplot(user_df[['age', 'account_balance', 'marketing_level', 'sales']],
             hue='marketing_level')


##################################################


##################################################
### Export data to SQL, Excel and print summary
##################################################

print("Account balance for top 20% of users: {} \nFraction of total \
      balance owned by top 20%: {}%\n".format(critical80,
                                              100*the_few/tot_balance))

# Generate user info, along with 10% dupes:
main_user_df = makeDupes(user_df[['user_id', 'first_name', 'last_name', 'email',
                        'password_hashed', 'gender', 'address', 'age',
                        'credit_card_num', 'credit_card_exp',
                        'security_answer', 'account_balance']])


def df_sql_write(df, file_name="test.sql", table_name="test_table"):
    """Function to generate an sqlite3 database from a pandas dataframe, df,
    with a table name, table_name. This is modified directly from the pandas
    documentation on connecting to databases:
        https://pandas.pydata.org/pandas-docs/stable/io.html#reading-tables"""
    if os.path.exists(file_name):
        os.remove(file_name)
    sql_db = sqlite3.connect(file_name)
    df.to_sql(name=table_name, con=sql_db, index=False)
    sql_db.close()


# Write out user info to SQL database (in random order)
df_sql_write(main_user_df.sample(frac=1.0), 'user_data.sql', table_name='user_accounts')

# Write out campaign data to Excel spreadsheet
campaign_df = user_df[['user_id', 'marketing_level', 'sales']].sample(frac=1.0)

campaign_df.to_excel('advertising_campaign.xlsx', index=False)

## Extract DB thus:
#with sqlite3.connect('user_data.sql') as cnx:
#    df1 = pd.read_sql_query("SELECT * FROM user_accounts", cnx)
#
#cnx.close()
