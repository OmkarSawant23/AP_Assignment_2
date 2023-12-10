#Import Statements 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#defining a function to reaf file name as argument and read dataframe in world bank format.
def file_name(file) :
    #reading all files
    wdf =     agriculture_land = pd.read_csv(file, skiprows= 3, 
                                       usecols=["Country Name","1990","1991","1992","1993","1994",
                                                "1995","1996","1997","1998","1999","2000","2001","2002",
                                                "2003","2004","2005","2006","2007","2008",
                                                "2009","2010","2011","2012","2013","2014",
                                                "2015","2016","2017","2018","2019","2020"])
    
    wdf.index = wdf["Country Name"]
    wdf = agriculture_land.iloc[:,1:]
    #cleaning data
    countires = ["France", "India", "Russian Federation", "Netherlands", "Hungary", "Germany", "Australia"]
    cleaned_agriculture = wdf.loc[countires,:]
    
    #setting years as intengers
    cleaned_agriculture.columns = cleaned_agriculture.columns.astype(int)
   
    # Separate the data into two dataframes: one with years as columns and one with countries as columns
    yr_wdf = cleaned_agriculture.T
    cr_wdf = cleaned_agriculture
    return yr_wdf, cr_wdf
    
def stats_functions(heading,yr_pop) :
    print("========"+heading+"========")
    print("--Describe--")
    print(yr_pop.describe())
    print("--Skewness--")
    print(yr_pop.skew())
    print("--Kurtosis--")
    print(yr_pop.kurtosis())
    print("--Median--")
    print(yr_pop.median())
    plt.show()
    
def plot_line(df,title,y):
    plt.figure()
    
    plt.plot(df.index, df["France"])
    plt.plot(df.index, df["India"])
    plt.plot(df.index, df["Hungary"])
    plt.plot(df.index, df["Netherlands"])
    plt.plot(df.index, df["Australia"])
    plt.plot(df.index, df["Germany"])
    
    plt.legend(["France", "India", "Hungary", "Netherlands", "Australia","Germany"],loc="center left", bbox_to_anchor=(1, 0.5))
    plt.ylabel(y)
    plt.title(title)
    plt.show()

def bar_plot(df,xlbl,ylbl,title) :
    
    years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]
   
    df_filter = df.loc[years,:]
    print(df_filter)
    plt.figure()
    
    x = np.arange(len(df_filter.columns))
    
    width = 0.1
    multiplier = 0
    
    fig, ax = plt.subplots(layout = 'constrained')
    
    for i in df_filter.index:
        offset = width * multiplier
        reacts = ax.bar(x + offset, df_filter.loc[i].values.flatten(), width,label = i )
        multiplier = multiplier + 1
    
    ax.set_xlabel(xlbl)
    ax.set_ylabel(ylbl)
    ax.set_title(title)
    ax.set_xticks(x + width, df_filter.columns)
    ax.legend()
    
    plt.show()
    
def heat_map(countires, cr_agriculture, cr_forest, cr_co2, cr_pop, cr_energy, yr_mortality,cmap) :
    cor = pd.DataFrame()
    cor["Agriculture"] = cr_agriculture.loc[countires,:].values
    cor["forest"] = cr_forest.loc[countires,:].values
    cor["co2"] = cr_co2.loc[countires,:].values
    cor["urban population"] = cr_pop.loc[countires,:].values
    cor["Renewable Energy"] = cr_energy.loc[countires,:].values
    cor["Mortality rate"] = yr_mortality.loc[countires,:].values
    
    cor = cor.corr().round(3)
    print(cor)
    plt.figure()
    plt.imshow(cor, cmap=cmap)
    plt.colorbar()
    plt.xticks(np.arange(len(cor.columns)), labels = cor.columns, rotation = 90)
    plt.yticks(np.arange(len(cor.columns)), labels = cor.columns)
    
    plt.title(countires)
    for (i, j), r in np.ndenumerate(cor):
        plt.text(i, j, r, ha = "center", va = "center")
        
    plt.show()
    
        
def print_all_line():
    plot_line(yr_agriculture,"Agriculture land  graph","Percentage of land")
    plot_line(yr_forest,"Forest land graph","Percentage of land")

######Main##########
yr_agriculture, cr_agriculture = file_name("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5995314.csv")
yr_forest, cr_forest = file_name("API_AG.LND.FRST.ZS_DS2_en_csv_v2_5994693.csv")
yr_co2,cr_co2 = file_name("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5994970.csv")
yr_pop,cr_pop = file_name("API_SP.URB.TOTL_DS2_en_csv_v2_5996761.csv")
yr_energy,cr_energy = file_name("API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_5995541.csv")
yr_mortality,yr_mortality = file_name("API_SH.DYN.MORT_DS2_en_csv_v2_5996359.csv")

stats_functions("yr_agriculture",yr_agriculture)
stats_functions("yr_forest",yr_forest)
print_all_line()
bar_plot(yr_co2,"Years", "Co2 emission", "co2 emission by countries by year")
bar_plot(yr_energy,"Years", "Renewable enegry", "Renewable enegry by year")
heat_map("India", cr_agriculture, cr_forest, cr_co2, cr_pop, cr_energy, yr_mortality, "plasma")
heat_map("Germany", cr_agriculture, cr_forest, cr_co2, cr_pop, cr_energy, yr_mortality, "Oranges")

plt.show()

    

