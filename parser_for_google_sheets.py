import pandas as pd
import copy


dfs = {}

# https://docs.google.com/spreadsheets/d/1PYq9Run8wV6526g2WMpueoWDyPu2cPsD8XodhmuJKH0/edit?usp=sharing

googleSheetId = '1PYq9Run8wV6526g2WMpueoWDyPu2cPsD8XodhmuJKH0'
for worksheetName in ["Grupa1","Grupa2","Grupa3","Grupa4"]:

    URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId,
        worksheetName
    )

    df = pd.read_csv(URL, on_bad_lines='skip',usecols = list(range(1,8)) + list(range(1,8)))
    df = df.fillna('')
    dfs[worksheetName] = df



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
            if df.iloc[i,j] != '':
                played+=1
                victory+=int(df.iloc[i+1,j]>df.iloc[i,j])
                defeat+=int(df.iloc[i+1,j]<df.iloc[i,j])
                wingames+=int(df.iloc[i+1,j])
                losgames+=int(df.iloc[i,j])
        diff = wingames-losgames

        # Special Case Uncomment the following code when you don't want teams that never played.
        # if played == 0:
        #     i+=2
        #     continue

        # Assign the values to the dict
        newdf["Igrac"].append(df.iloc[i,0])  
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
    print(result)
        
    print("\n\n")
    
