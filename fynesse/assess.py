import yaml
import pymysql
import scipy as sp
import pandas as pd
import osmnx as ox
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np
import mlai
import mlai.plot as plot


from ipywidgets import interact_manual, Text, Password
from sklearn.decomposition import PCA
from numpy.core.fromnumeric import transpose
from sklearn import linear_model


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



def get_pois(conn, size, tags):
  """
  Returns a 1x4 array containing the minimum lattitude, maximum lattitude, minimum longitude, and maximum longitude present in the prices_coordinates_data table
  """

  cur = conn.cursor()

  cur.execute("""
              SELECT MIN(lattitude), MAX(lattitude), MIN(longitude), MAX(longitude) FROM prices_coordinates_data
              """)

  rows = cur.fetchall()
  result = (np.array(rows[0])).astype(float)

  north = result[1] + size/2
  south = result[0] - size/2
  east = result[3] + size/2
  west = result[2] - size/2

  pois = ox.geometries_from_bbox(north, south, east, west, tags)

  return pois, [north, south, east, west]





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
