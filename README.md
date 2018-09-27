# Extracting-data-from-911-calls-Python-Pandas




The project deals with .csv file of 911 calls which is downloaded from Kaggle

The data contains the following fields:
lat : String variable, Latitude
lng: String variable, Longitude
desc: String variable, Description of the Emergency Call
zip: String variable, Zipcode
title: String variable, Title
timeStamp: String variable, YYYY-MM-DD HH:MM:SS
twp: String variable, Township
addr: String variable, Address
e: String variable, Dummy variable (always 1)


First what we have done is to create a seperate column called 'Reason' which contains the data extracted from column 'title'.
Various columns called 'Hour', 'Month', 'Day of Week' are also created. The corresponding plots are plotted to get a better
understanding of the data.
