"""Import Statements"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def file_name(file):
    '''
    This function reads the csv files and also filters the dataframe \
    and returns two dataframe one with transposed data and one with
    non transposed data.

    Parameters
    ----------
    file : TYPE
        This is pandas dataframe.

    Returns
    -------
    yr_wdf : TYPE
        Returns the transposed dataframe.
    cr_wdf : TYPE
        Returns non transposed dataframe.

    '''
    # reading csv files and selecting specific years.
    wdf = agriculture_land = \
        pd.read_csv(file, skiprows=3, usecols=["Country Name", "1990", "1991",
                                               "1992", "1993", "1994", "1995",
                                               "1996", "1997", "1998", "1999",
                                               "2000", "2001", "2002", "2003",
                                               "2004", "2005", "2006", "2007",
                                               "2008", "2009", "2010", "2011",
                                               "2012", "2013", "2014", "2015",
                                               "2016", "2017", "2018", "2019",
                                               "2020"])
    # setting country name as index.
    wdf.index = wdf["Country Name"]
    wdf = agriculture_land.iloc[:, 1:]

    # filtering data.
    countires = ["France", "India", "Russian Federation", "Netherlands",
                 "Hungary", "Germany", "Australia"]
    cleaned_agriculture = wdf.loc[countires, :]

    # setting years as intengers.
    cleaned_agriculture.columns = cleaned_agriculture.columns.astype(int)

    # Separate the data into two dataframes: one with years as columns
    # and one with countries as columns
    yr_wdf = cleaned_agriculture.T
    cr_wdf = cleaned_agriculture

    return yr_wdf, cr_wdf


def stats_functions(heading, df_stats):
    '''
    This function explores the statistical properties such as describe.
    skewness,kurtosis and median.

    Parameters
    ----------
    heading : TYPE
        Name of the dataframe used.
    yr_pop : TYPE
        This is pandas dataframe.

    Returns
    -------
    None.

    '''
    # Prints the heading.
    print("================="+heading+"=================")

    # Using Describe Method.
    print("**********Describe**********")
    print(df_stats.describe())

    # Using Skewness Method.
    print("**********Skewness**********")
    print(df_stats.skew())

    # Using Kurtosis Method.
    print("**********Kurtosis**********")
    print(df_stats.kurtosis())

    # Using Median Method.
    print("**********Median**********")
    print(df_stats.median())


def plot_line(data_f, title, x_axis, y_axis):
    '''
    This function will return line plots for given dataframes
    with specific countries.

    Parameters
    ----------
    df : TYPE
        This is pandas dataframe.
    title : TYPE
        Name of the graph.
    x : TYPE
         Label of the x-axis.
    y : TYPE
        Label of the y-axis.

    Returns
    -------
    None.

    '''
    # Plotting the figure.
    plt.figure()

    # Plotting the data.
    plt.plot(data_f.index, data_f["France"])
    plt.plot(data_f.index, data_f["India"])
    plt.plot(data_f.index, data_f["Hungary"])
    plt.plot(data_f.index, data_f["Netherlands"])
    plt.plot(data_f.index, data_f["Australia"])
    plt.plot(data_f.index, data_f["Germany"])

    # Adding the legend and labels.
    plt.legend(["France", "India", "Hungary", "Netherlands", "Australia",
                "Germany"], loc="center left", bbox_to_anchor=(1, 0.5))
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    # Adding Title.
    plt.title(title)

    # Saving the plot.
    plt.savefig(title+".png", dpi=300, bbox_inches="tight")

    # Displaying the plot.
    plt.show()


def bar_plot(data_frame, xlabel, ylabel, title):
    '''
    This function will return bar plots for given dataframes
    with specific countries and selected years.

    Parameters
    ----------
    data_frame : TYPE
       This is pandas dataframe.
    xlabel : TYPE
        Label of the x-axis.
    ylabel : TYPE
       Label of the y-axis.
    title : TYPE
        Name of the graph.

    Returns
    -------
    None.

    '''
    # Filtering Years.
    years = [2005, 2010, 2015, 2020]

    # Cleaned dataframe.
    data_frame_clean = data_frame.loc[years, :]
    plt.figure()

    # location of labels.
    x_bar = np.arange(len(data_frame_clean.columns))

    # bar width.
    width = 0.1
    multiplier = 0

    # subplots
    fig, ag_pl = plt.subplots(layout='constrained')

    # for loop giving the bar plot.
    for i in data_frame_clean.index:
        offset = width * multiplier
        ag_pl.bar(x_bar + offset, data_frame_clean.loc[i].values.flatten(),
                  width, label=i)
        multiplier = multiplier + 1

    # Setting labels and title, legend.
    ag_pl.set_xlabel(xlabel)
    ag_pl.set_ylabel(ylabel)
    ag_pl.set_title(title)
    ag_pl.set_xticks(x_bar + width, data_frame_clean.columns, rotation=45)
    ag_pl.legend()

    # Saving the figure.
    plt.savefig(title+".png", dpi=300, bbox_inches="tight")
    plt.show()


def heat_map(countires, cr_1, cr_2, cr_3, cr_4, cr_5,
             cr_6, cmap):
    '''
    This function gives the correlation heatmap for specified indicators
    for selected countries.

    Parameters
    ----------
    countires : TYPE
        Name of the countries.
    cr_1 : TYPE
        This is a pandas dataframe.
    cr_2 : TYPE
       This is a pandas dataframe.
    cr_3 : TYPE
        This is a pandas dataframe.
    cr_4 : TYPE
        This is a pandas dataframe.
    cr_5 : TYPE
        This is a pandas dataframe.
    cr_6 : TYPE
        This is a pandas dataframe.
    cmap : TYPE
        colourmap.

    Returns
    -------
    None.

    '''
    # Corelation heatmap indicators.
    cor = pd.DataFrame()
    cor["Agriculture"] = cr_1.loc[countires, :].values
    cor["forest"] = cr_2.loc[countires, :].values
    cor["co2"] = cr_3.loc[countires, :].values
    cor["urban population"] = cr_4.loc[countires, :].values
    cor["Renewable Energy"] = cr_5.loc[countires, :].values
    cor["Mortality rate"] = cr_6.loc[countires, :].values

    # correlation calculation.
    cor = cor.corr().round(3)
    # plotting the figure.
    plt.figure()
    # colour map.
    plt.imshow(cor, cmap=cmap)
    # adding colour bar.
    plt.colorbar()
    # adding x-ticks and y-ticks.
    plt.xticks(np.arange(len(cor.columns)), labels=cor.columns,
               rotation=90)
    plt.yticks(np.arange(len(cor.columns)), labels=cor.columns)

    plt.title(countires)
    for (i, j), ra_r in np.ndenumerate(cor):
        plt.text(i, j, ra_r, ha="center", va="center")
    # Saving the figure.
    plt.savefig(countires+".png", dpi=300, bbox_inches="tight")
    plt.show()


def print_all_line():
    '''
    Implementation of line plots for agriculture and forest land.

    Returns
    -------
    None.

    '''
    plot_line(yr_agriculture, "Agriculture land  graph", "Years",
              "Percentage of land")
    plot_line(yr_forest, "Forest land graph", "Years", "Percentage of land")


def print_all_bar():
    '''
    Implementation of bar plots for  co2 emission and urban population.

    Returns
    -------
    None.

    '''
    bar_plot(yr_co2, "Years", "Co2 emission",
             "co2 emission by countries by year")
    bar_plot(yr_pop, "Years", "Urban Population", "Urban population by year")


def print_all_heat():
    """
    Implementation of Correlation Heatmap for specified countries.

    Returns
    -------
    None.

    """
    heat_map("India", cr_agriculture, cr_forest, cr_co2, cr_pop, cr_energy,
             cr_mortality, "rainbow")
    heat_map("Germany", cr_agriculture, cr_forest, cr_co2, cr_pop, cr_energy,
             cr_mortality, "cividis")
    heat_map("Australia", cr_agriculture, cr_forest, cr_co2, cr_pop, cr_energy,
             cr_mortality, "viridis")


##################################Main#########################################
# Reading csv files
yr_agriculture, cr_agriculture = file_name(
    "API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5995314.csv")
yr_forest, cr_forest = file_name(
    "API_AG.LND.FRST.ZS_DS2_en_csv_v2_5994693.csv")
yr_co2, cr_co2 = file_name("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5994970.csv")
yr_pop, cr_pop = file_name("API_SP.URB.TOTL_DS2_en_csv_v2_5996761.csv")
yr_energy, cr_energy = file_name(
    "API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_5995541.csv")
yr_mortality, cr_mortality = file_name(
    "API_SH.DYN.MORT_DS2_en_csv_v2_5996359.csv")
# Printing statistical methods.
stats_functions("Urban Population", yr_pop)
# line plot.
print_all_line()
# bar plot.
print_all_bar()
# Heatmap.
print_all_heat()
