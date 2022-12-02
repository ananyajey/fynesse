
from .config import *

#import .access

def db_to_df(conn, table_name, column_names = None):
  sql_query = pd.read_sql_query ('''SELECT * FROM {}'''.format(table_name), conn)
  if (column_names == None):
    df = pd.DataFrame(sql_query)
  else:
    df = pd.DataFrame(sql_query, columns = column_names)
  df.set_index('db_id')
  
  return df



def data():
    """Load the data from access and ensure missing values are correctly encoded as well as indices correct, column names informative, date and times correctly formatted. Return a structured data structure such as a data frame."""
    #df = access.data()
    raise NotImplementedError

def query(data):
    """Request user input for some aspect of the data."""
    raise NotImplementedError

def view(data):
    """Provide a view of the data that allows the user to verify some aspect of its quality."""
    raise NotImplementedError

def labelled(data):
    """Provide a labelled set of data ready for supervised learning."""
    raise NotImplementedError
