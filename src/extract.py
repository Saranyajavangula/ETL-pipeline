import pandas as pd
import sqlite3

def extract_data():
#connecting db
  conn = sqlite3.connect('../Week17/Data/bootcamp_db')

# writing the query
  query="""select ot.*,
             CASE
                when description IS NULL then 'Unknown'
                else description
                end as description
             from online_transactions ot 
             left join (select * 
                          from stock_description 
                            where description <> '?' ) sd on ot.stock_code = sd.stock_code
             where  ot.customer_id <> ''
             and ot.stock_code not in ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')"""

  ot_cleaned=pd.read_sql(query,conn)
  print('the shape of the dataframe is:',ot_cleaned.shape)
  return ot_cleaned
