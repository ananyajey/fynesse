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

def credential_info_fyn():
  @interact_manual(username=Text(description="Username:"), 
                  password=Password(description="Password:"))
  def write_credentials(username, password):
      with open("credentials.yaml", "w") as file:
          credentials_dict = {'username': username, 
                              'password': password}
          yaml.dump(credentials_dict, file)

def data():
    """Read the data from the web or local file, returning structured format such as a data frame"""
    raise NotImplementedError

