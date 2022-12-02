from .config import *

"""These are the types of import we might expect in this file
import httplib2
import oauth2
import tables
import mongodb
import sqlite"""

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

# This file accesses the data

"""Place commands in this file to access the data electronically. Don't remove any missing values, or deal with outliers. Make sure you have legalities correct, both intellectual property and personal data privacy rights. Beyond the legal side also think about the ethical issues around this data. """

def credential_info():
  @interact_manual(username=Text(description="Username:"), 
                  password=Password(description="Password:"))
  def write_credentials(username, password):
      with open("credentials.yaml", "w") as file:
          credentials_dict = {'username': username, 
                              'password': password}
          yaml.dump(credentials_dict, file)



def create_connection(user, password, host, database, port=3306):
    conn = None
    try:
        conn = pymysql.connect(user=user,
                               passwd=password,
                               host=host,
                               port=port,
                               local_infile=1,
                               db=database
                               )
    except Exception as e:
        print(f"Error connecting to the MariaDB Server: {e}")
    return conn



def load_into(conn, file_path, table_name):
  cur = conn.cursor()

  cur.execute("""
              LOAD DATA LOCAL INFILE '{}' INTO TABLE `{}`
              FIELDS TERMINATED BY ',' 
              OPTIONALLY ENCLOSED BY '"'
              LINES STARTING BY '' TERMINATED BY '\n';
              """.format(file_path, table_name))

  conn.commit()
  print(cur.lastrowid)
  
  
  
def select_pcd(conn, from_date, to_date, min_lat = None, max_lat = None, min_long = None, max_long = None, town_city = None, district = None, county = None, country = None, property_type = None):
    conditions = ""
    if (min_lat != None):
      conditions = conditions + "\n AND lattitude >= '{}'".format(min_lat)
    
    if (max_lat != None):
      conditions = conditions + "\n AND lattitude <= '{}'".format(max_lat)
    
    if (min_long != None):
      conditions = conditions + "\n AND longitude >= '{}'".format(min_long)
    
    if (max_long != None):
      conditions = conditions + "\n AND longitude <= '{}'".format(max_long)
    
    if (town_city != None):
      conditions = conditions + "\n AND town_city = '{}'".format(town_city)
    
    if (district != None):
      conditions = conditions + "\n AND district = '{}'".format(district)
    
    if (county != None):
      conditions = conditions + "\n AND county = '{}'".format(county)
    
    if (country != None):
      conditions = conditions + "\n AND country = '{}'".format(country)
    
    if (property_type != None):
      conditions = conditions + "\n AND property_type = '{}'".format(property_type)


    cur = conn.cursor()

    cur.execute("""
                 INSERT INTO prices_coordinates_data(price, date_of_transfer, postcode, property_type, new_build_flag, tenure_type, locality, town_city, district, county, country, lattitude, longitude)
                    (SELECT pp_data.price, pp_data.date_of_transfer, pp_data.postcode, pp_data.property_type, pp_data.new_build_flag, pp_data.tenure_type, pp_data.locality, pp_data.town_city, pp_data.district, pp_data.county, postcode_data.country, postcode_data.lattitude, postcode_data.longitude
                    FROM `pp_data`
                    INNER JOIN `postcode_data` ON pp_data.postcode = postcode_data.postcode
                    WHERE date_of_transfer >= DATE '{}'
                    AND date_of_transfer <= DATE '{}'{});
                """.format(from_date, to_date, conditions))

    conn.commit()
    print(cur.lastrowid)


def data():
    """Read the data from the web or local file, returning structured format such as a data frame"""
    raise NotImplementedError

