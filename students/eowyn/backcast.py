import pandas as pd
import numpy as np
from tabulate import tabulate

fname = 'M426_Processed_Data.txt'
metdf = pd.read_table(fname, skiprows=1,
                      index_col=0,
                      parse_dates=True,
                      infer_datetime_format=True)
metdf.index.name = 'DateTime'

"""
Parse column names to determine sensor info: measurement height,
sensor type, and field type (mean, max, etc.) handling the existance
of fields like "St Dev" that need to be combined to "StDev" and
retaining only the numeric component of the sensor height (in m or ft)
"""
colnames = list(metdf)
sensorInfo = []
for col in colnames:
    sensor = col.split(' ')
    unitIndex, conversion = sensor[0].lower().find('m'), 1.0
    if unitIndex == -1:
        unitIndex, conversion = sensor[0].lower().find('ft'), 0.3048
    sensorInfo.append([float(sensor[0][:unitIndex]) * conversion,
                       sensor[1],
                       "".join(sensor[2:])])

# Locate column name index of highest mean anemometer sensor
windAve = [(item[2] == "Mean" and item[1] == "Anemometer")
           for item in sensorInfo]  # Boolean where field is ave wind
heights = [item[0] for item in sensorInfo]
meanWindHeights = [a * b for a, b in zip(windAve, heights)]
mxInd = meanWindHeights.index(max(meanWindHeights))

# Drop all other columns from dataframe
dropcols = colnames[:mxInd] + colnames[mxInd + 1:]
metdf.drop(dropcols, axis=1, inplace=True)

# Replace invalid data with nan
metdf.iloc[:, 0] = metdf.iloc[:, 0].replace(-99.99, np.nan)
# Drop rows with missing values
metdf = metdf.dropna(axis=0, how='any')



#  Given a pandas series, return series with outliers replaced by nan
#  For series with few unique variables, do nothing and return the series
#  The hepatitis dataset has many columns with 2 or 3 unique variables
def replace_outliers_with_na(x):
    if len(x.unique()) < 5:
        return x
    xbar = np.mean(x) # Mean, ignoring NA
    xsd = np.std(x) # Standard deivation, ignoring NA
    LL = xbar - 2*xsd # Lower limit for outlier detection
    UL = xbar + 2*xsd # Upper limit for outlier detection
    return x.map(lambda y: y if y > LL and y < UL else np.nan) # Change outliers to NA

# Given a pandas series x, replace any NA with median of non-NA values
def replace_na_with_median(x):
    return x.fillna(np.mean(x))

fname = 'Power_data.txt'
powerdf = pd.read_table(fname, skiprows=0,
                        index_col=0,
                        parse_dates=True,
                        infer_datetime_format=True)
powerdf.index.name = 'DateTime'
colnames = list(powerdf)
#powerdf = powerdf.apply(replace_outliers_with_na)
#powerdf = powerdf.apply(replace_na_with_median)

"""
Read power curve data
Store as a dict with keys = wind speed, 
values = power generation
"""

fname = "PowerCurve.txt"
pclist = []
for line in open(fname):
    pclist.append(line.split('\t'))
pclist = pclist[1:] # Remove headers
power_curve = {float(i[0]):float(i[1].replace('\n','')) for i in pclist}

"""
Construct a time series (dataframe) of power generation.
For each wind speed time step, check if power is above or below
the cut-in or cut-out (max, min of power curve) - if so, generation=0
Otherwise, round windspeed to the nearest 0.5m/s and select generation
value from power curve dictionary. 
"""

# https://stackoverflow.com/questions/4265546/python-round-to-nearest-05
def round_to_05(n, precision=0.5):
    correction = 0.5 if n >= 0 else -0.5
    return int( n/precision+correction ) * precision

metdf = metdf.applymap(round_to_05)
# Create a new column with the power generation. IF the map fails 
# to find a matching wind speed, the Generation is nan
metdf["Generation"] = metdf.iloc[:,0].map(power_curve)
# Replace nan generation with zero for ws < cut-int or > cut-out
metdf["Generation"] = metdf["Generation"].replace(np.nan, 0.0)


"""
Create 10-min power generation data from
10-min wind speed and the power curve dict
"""

"""
Determine time step for both and resample 
to hourly, as needed.
"""
power_hour = powerdf.resample('60min').mean()
met_hour = metdf.resample('60min').mean()
"""
Determine start and end time of both
IF there are 12month overlap, truncate to those 12 months
IF not, align date/time but not year
"""
# Set up empty data frame to contain aligned data
aligned_data = pd.DataFrame()

# Check amount of overlap
mstart, mend = met_hour.index.min(), met_hour.index.max()
pstart, pend = power_hour.index.min(), power_hour.index.max()
if mstart <= pstart:
    print("met data starts first")
    if mend <= pstart:
        print("met data starts and ends before power data. No overlap")
        overlap = False
    else:
        print("met data starts first but doesn't end til after power starts")
        overlap = True
else:
    print("power data starts first")
    if pend <= mstart:
        print("pwr data stars and ends before met data. No overlap")
        overlap = False
    else:
        print("pwr data starts first but doesn't end til after met starts")
        overlap = True

if overlap:
    timesInCommon = powerdf.index.intersection(metdf.index)
    enough = overlap.max() - overlap.min() >= pd.Timedelta('360 days')
    if enough:
        print("enough overlap to work with")
        # truncate both df to later start and earlier end
        met_hour = met_hour.truncate(before=min(mstart, pstart),
                                     after=max(mend, pend))
        power_hour = power_hour.truncate(before=min(mstart, pstart),
                                         after=max(mend, pend))
        aligned_data = pd.concat([met_hour, power_hour],axis = 1)
        # TO DO: Decide, should this data also go through typical year?

"""
If not enough overlap, calculate "typical year" for both.
At this point, the datetime axis is no longer available. 
We will deal with leap-years then re-create the TimeStamp index.
"""

if aligned_data.empty:
    met_yr = met_hour.groupby([met_hour.index.month,
                               met_hour.index.day,
                               met_hour.index.hour]).mean()
    pwr_yr = power_hour.groupby([power_hour.index.month,
                                 power_hour.index.day,
                                 power_hour.index.hour]).mean()


    """
    Deal with leap years. A normal year has 8760 hours, and a leap year
    has 8784; hours 1416 through 1439, inclusive, are Feb 29. 
    Drop all Feb 29 rows:
    temp2 = temp.drop(temp.index[1416:1440], axis = 0)
    """
    if len(met_yr.index) == 8784:
        print("removing leap day from met year")
        met_yr = met_yr.drop(met_yr.index[1416:1440], axis=0)
    if len(pwr_yr.index) == 8784:
        print("removing leap day from power year")
        pwr_yr = pwr_yr.drop(pwr_yr.index[1416:1440], axis=0)

    # Construct a dummy TimeStamp index for the typical year
    typical_year = pd.date_range('2015-01-01', periods=8760, freq='H')
    met_yr.index, met_yr.index.names = typical_year, ["TimeStamp"]
    pwr_yr.index, pwr_yr.index.names = typical_year, ["TimeStamp"]

    # Concatenate the data together to form a single data frame
    aligned_data = pd.concat([met_yr, pwr_yr],axis=1)

"""
In [168]: y = pd.date_range('2015-08-03', periods=1000, freq='H')
use that to help write tests

temp = met_hour.truncate('2009-01-01 00:00:00','2009-12-31 23:00:00').index

"""

"""
Determine profit for a given substation, in this case, Brown.
Add Profit column to aligned_data
TO DO: Make choice of substation (or ave of all stations) an option
"""
aligned_data["Revenue"] = 1e-4*aligned_data["Generation"]*aligned_data["Brown"]

"""
Generate monthly averages of peak and off-peak revenue
Print tables
TO DO: Take args for peak/off-peak hours
"""

# Filter aligned_data into peakdf and offpeakdf
peakHours = pd.Series([i for i in range(0, 12)])  # 0..11
offPeakHours = pd.Series([i for i in range(12, 24)])  # 12..23
peakTimes = pd.Series(aligned_data.index.hour).isin(peakHours)  # Boolean
peakTimes.index, peakTimes.index.names = typical_year, ["TimeStamp"]
offPeakTimes = pd.Series(aligned_data.index.hour).isin(offPeakHours)  # Boolean
offPeakTimes.index, offPeakTimes.index.names = typical_year, ["TimeStamp"]
peakTimes = peakTimes.apply(lambda x: 1 if x else np.nan)
offPeakTimes = offPeakTimes.apply(lambda x: 1 if x else np.nan)


peakDF = aligned_data.mul(peakTimes, axis=0)
peakDF = peakDF.drop(['North','West','South','Red Creek','Brown'],axis=1)
offPeakDF = aligned_data.mul(offPeakTimes, axis=0)
offPeakDF = offPeakDF.drop(['North','West','South','Red Creek','Brown'],axis=1)

# Finally, pretty print tables for peak and off mean monthly means.
# Done: group wind by MEAN and generation, revenue by SUM
# Done: Write results to file with full precision
windname = peakDF.columns[0]  
print(60*'-')
print('Peak Hours Monthly Sum')
result = peakDF.groupby(peakDF.index.month).agg({windname: np.mean, "Generation": sum, "Revenue":sum})
result.index.names=["Month"]
print(tabulate(result,headers = 'keys'))
result.to_csv('PeakHours-Revenue.txt', sep='\t')
print(60*'-')
print('Off Peak Hours Monthly Sum')
result = offPeakDF.groupby(offPeakDF.index.month).agg({windname: np.mean, "Generation": sum, "Revenue":sum})
result.index.names=["Month"]
print(tabulate(result,headers = 'keys'))
result.to_csv('OffPeakHours-Revenue.txt', sep='\t')





