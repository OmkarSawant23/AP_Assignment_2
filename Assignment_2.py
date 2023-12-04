#Import Statements 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#defining a function to reaf file name as argument and read dataframe in world bank format.
def file_name(file) :
    #reading all files
    agriculture_land = pd.read_csv("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5995314.csv", skiprows= 3, usecols=["Country Name","2000","2001","2002","2003","2004"])
    forest_area = pd.read_csv("API_AG.LND.FRST.ZS_DS2_en_csv_v2_5994693.csv", skiprows= 3)
    Nuclear_energy = pd.read_csv("API_EG.ELC.NUCL.ZS_DS2_en_csv_v2_5995539.csv", skiprows= 3)
    oil_electricity = pd.read_csv("API_EG.ELC.PETR.ZS_DS2_en_csv_v2_5995543.csv", skiprows= 3)
    renewable_enenrgy = pd.read_csv("API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_5995541.csv", skiprows= 3)
    co2_emission = pd.read_csv("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5994970.csv", skiprows= 3)
    mortality_rate = pd.read_csv("API_SH.DYN.MORT_DS2_en_csv_v2_5996359.csv", skiprows= 3)
    urban_population = pd.read_csv("API_SP.URB.TOTL_DS2_en_csv_v2_5996761.csv", skiprows= 3)
    
    #cleaning data
    countires = ["China", "India", "Russian Federation", "United States"]
   
    
    cleaned_agriculture = agriculture_land[agriculture_land["Country Name"].isin(countires)]
    
    
    #transposing all dataframes.
    agriculture_land_transpose = agriculture_land.T
    forest_area_transpose = forest_area.T
    Nuclear_energy_transpose = Nuclear_energy.T
    oil_electricity_transpose = oil_electricity.T
    renewable_enenrgy_transpose = renewable_enenrgy.T
    co2_emission_transpose = co2_emission.T
    mortality_rate_transpose = mortality_rate.T
    urban_population_transpose = urban_population.T
    
    #first column
    index_agriculture = agriculture_land_transpose.iloc[0]
    index_forest = forest_area_transpose.iloc[0]
    index_nuclear = Nuclear_energy_transpose.iloc[0]
    index_oil = oil_electricity_transpose.iloc[0]
    index_renewable = renewable_enenrgy_transpose.iloc[0]
    index_co2 = co2_emission_transpose.iloc[0]
    index_mortality = mortality_rate_transpose.iloc[0]
    index_urban = urban_population_transpose.iloc[0]
    
    #removing first row
    agriculture_land_transpose = agriculture_land_transpose[1:]
    forest_area_transpose = forest_area_transpose[1:]
    Nuclear_energy_transpose = Nuclear_energy_transpose[1:]
    oil_electricity_transpose = oil_electricity_transpose[1:]
    renewable_enenrgy_transpose = renewable_enenrgy_transpose[1:]
    co2_emission_transpose = co2_emission_transpose[1:]
    mortality_rate_transpose = mortality_rate_transpose[1:]
    urban_population_transpose = urban_population_transpose[1:]
    
    #setting new column 
    agriculture_land_transpose.columns = index_agriculture
    forest_area_transpose.columns = index_forest
    Nuclear_energy_transpose.columns = index_nuclear
    oil_electricity_transpose.columns = index_oil
    renewable_enenrgy_transpose.columns = index_renewable
    co2_emission_transpose.columns = index_co2
    mortality_rate_transpose.columns = index_mortality
    urban_population_transpose.columns = index_urban
    
    #reset the index
    agriculture_land_transpose.reset_index(inplace = True)
    forest_area_transpose.reset_index(inplace = True)
    Nuclear_energy_transpose.reset_index(inplace = True)
    oil_electricity_transpose.reset_index(inplace = True)
    renewable_enenrgy_transpose.reset_index(inplace = True)
    co2_emission_transpose.reset_index(inplace = True)
    mortality_rate_transpose.reset_index(inplace = True)
    urban_population_transpose.reset_index(inplace = True)
    
    # Rename the columns
    agriculture_land_transpose.rename(columns={'index': 'Country Name'}, inplace=True)
    forest_area_transpose.rename(columns={'index': 'Country Name'}, inplace=True)
    Nuclear_energy_transpose.rename(columns={'index': 'Country Name'}, inplace=True)
    oil_electricity_transpose.rename(columns={'index': 'Country Name'}, inplace=True)
    renewable_enenrgy_transpose.rename(columns={'index': 'Country Name'}, inplace=True)
    co2_emission_transpose.rename(columns={'index': 'Country Name'}, inplace=True)
    mortality_rate_transpose.rename(columns={'index': 'Country Name'}, inplace=True)
    urban_population_transpose.rename(columns={'index': 'Country Name'}, inplace=True)
    
    # Separate the data into two dataframes: one with years as columns and one with countries as columns
    yr_agriculture = agriculture_land_transpose.set_index('Country Name').apply(pd.to_numeric, errors='coerce')
    yr_forest = forest_area_transpose.set_index('Country Name').apply(pd.to_numeric, errors='coerce')
    yr_nuclear = Nuclear_energy_transpose.set_index('Country Name').apply(pd.to_numeric, errors='coerce')
    yr_oil = oil_electricity_transpose.set_index('Country Name').apply(pd.to_numeric, errors='coerce')
    yr_renewabel = renewable_enenrgy_transpose.set_index('Country Name').apply(pd.to_numeric, errors='coerce')
    yr_co2 = co2_emission_transpose.set_index('Country Name').apply(pd.to_numeric, errors='coerce')
    yr_mortality = mortality_rate_transpose.set_index('Country Name').apply(pd.to_numeric, errors='coerce')
    yr_urban = urban_population_transpose.set_index('Country Name').apply(pd.to_numeric, errors='coerce')
    
    cr_agriculture = agriculture_land_transpose.set_index('Country Name').transpose().apply(pd.to_numeric, errors='coerce')
    cr_forest = forest_area_transpose.set_index('Country Name').transpose().apply(pd.to_numeric, errors='coerce')
    cr_nuclear = Nuclear_energy_transpose.set_index('Country Name').transpose().apply(pd.to_numeric, errors='coerce')
    cr_oil = oil_electricity_transpose.set_index('Country Name').transpose().apply(pd.to_numeric, errors='coerce')
    cr_renewable = renewable_enenrgy_transpose.set_index('Country Name').transpose().apply(pd.to_numeric, errors='coerce')
    cr_co2 = co2_emission_transpose.set_index('Country Name').transpose().apply(pd.to_numeric, errors='coerce')
    cr_mortality = mortality_rate_transpose.set_index('Country Name').transpose().apply(pd.to_numeric, errors='coerce')
    cr_urban = urban_population_transpose.set_index('Country Name').transpose().apply(pd.to_numeric, errors='coerce')
    
    return yr_agriculture,yr_forest,yr_nuclear,yr_oil,yr_renewabel,yr_co2,yr_mortality,yr_urban,cr_agriculture,cr_forest,cr_nuclear,cr_oil,cr_renewable,cr_co2,cr_mortality,cr_urban,cleaned_agriculture
    
    
    
yr_agriculture,yr_forest,yr_nuclear,yr_oil,yr_renewabel,yr_co2,yr_mortality,yr_urban,cr_agriculture,cr_forest,cr_nuclear,cr_oil,cr_renewable,cr_co2,cr_mortality,cr_urban,cleaned_agriculture = file_name("file")
   
    
print(yr_agriculture.head())
print(cr_agriculture.head())
print(cleaned_agriculture)
print(cr_oil.head())

    
    