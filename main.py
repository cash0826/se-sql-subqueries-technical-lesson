import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# Substituting JOIN w subqueries

# q = """
# SELECT lastName, firstName, officeCode
# FROM employees
# JOIN offices
#     USING(officeCode)
# WHERE country = "USA"
# ;"""

# subquery

# q = """
# SELECT lastName, firstName, officeCode
# FROM employees
# WHERE officeCode IN (SELECT officeCode
#                      FROM offices 
#                      WHERE country = "USA")
# ;
# """

# Subqueries for filtering based on aggregation
# what if you wanted to find all of the employees from offices with at least 5 employees?

# q = """
# SELECT lastName, firstName, officeCode
# FROM employees
# WHERE officeCode IN (
#   SELECT officeCode
#   FROM offices
#   JOIN employees
#     USING(officeCode)
#   GROUP BY 1
#   HAVING COUNT(employeeNumber) >= 5
# )
# """

# Chaining aggregates
# Find the average of individual customers' average payments

q = """
SELECT AVG(customerAvgPayment) AS averagePayment
FROM (
  SELECT AVG(amount) AS customerAvgPayment
  FROM payments
  JOIN customers
    USING(customerNumber)
  GROUP BY customerNumber
);
"""

# Foreign Key Reference. Here we can use employee number in employees, and sales rep number in the customers table

q = """
SELECT lastName, firstName, employeeNumber
FROM employees
WHERE employeeNumber IN (
  SELECT salesRepEmployeeNumber
  FROM customers
  WHERE country = "USA"
);
"""

df = pd.read_sql(q, conn)
print(df)

conn.close()