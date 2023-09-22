import pandas as pd
import copy
import openpyxl

# google sheet from which tabela is downloaded https://docs.google.com/spreadsheets/d/1HBOfNbwByrxFHhqKOJdDzycWjjmSYfPSDk-HEOt4k0A/edit#gid=1173186980

# Load the Excel file
excel_file = pd.ExcelFile('tabela.xlsx')

# Get the sheet names
sheet_names = [ 'Grupa 1' , 'Grupa 2', 'Grupa 3', 'Grupa 4' ]

# Create a dictionary to hold DataFrames
dfs = {}

# Iterate through the sheets and convert them to DataFrames
for sheet_name in sheet_names:
    df = excel_file.parse(sheet_name)
    df = df.fillna('')
    dfs[sheet_name] = df

# Now, dfs dictionary contains DataFrames with sheet names as keys
# You can access them like dfs['Sheet1'], dfs['Sheet2'], etc.




for sheet_name, df in dfs.items():
 
    # Empty new dict
    newdf = {
    "Igrac":[],
    "Odigrane":[],
    "Pobeda":[],
    "Poraz":[],
    "Osvojeni gemovi":[],
    "Izgubljeni gemovi":[],
    "Razlika gemova":[]
    }
    i=0
    while(i<len(df)):
         
        played=0
        victory=0
        defeat=0
        wingames=0
        losgames=0
        diff=0
    
        # Calculate the correct values
        for j in range(1,len(df.iloc[0])):
            if df.iloc[i,j]:
                played+=1
                victory+=int(df.iloc[i+1,j]>df.iloc[i,j])
                defeat+=int(df.iloc[i+1,j]<df.iloc[i,j])
                wingames+=int(df.iloc[i+1,j])
                losgames+=int(df.iloc[i,j])
        diff = wingames-losgames

        # Special Case
        #if played == 0:
            #i+=2
            #continue

        # Assign the values to the dict
        newdf["Name"].append(df.iloc[i,0])
        newdf["Odigrane"].append(played)
        newdf["Pobeda"].append(victory)
        newdf["Poraz"].append(defeat)
        newdf["Osvojeni gemovi"].append(wingames)
        newdf["Izgubljeni gemovi"].append(losgames)
        newdf["Razlika gemova"].append(diff)

                
        i+=2

    # Create a DataFrame from the dict
    result = pd.DataFrame(newdf).sort_values(by=["Pobeda","Razlika gemova"],ascending=[False, False]).reset_index(drop=True)
    result.index += 1
    print(result)  # if you use jupyter run display(result)
        
    print("\n\n")
