# This is a graphing example page

    This is a graphing example page from kaggle.com about a survey from kaggle users
    
## Python Code:


    # This is using data that can be found at:
    # https://www.kaggle.com/ahmedatta/who-said-data-science-is-boring/data?select=kaggle_survey_2020_responses.csv


    import pandas as pd
    import numpy as np
    import seaborn as sb
    import matplotlib.pyplot as plt
    import warnings
    import os
    warnings.filterwarnings(action = 'ignore')

    # %%

    df =pd.read_csv('input/kaggle_survey_2020_responses.csv')

    # %%

    df_sample = df.iloc[0:20]

    #print(df.keys())
    #print(df.__dict__)


    df = df.iloc[1:,:]

    #print(df.__dict__)

    # %% Distrobution of Age

    plt.xkcd(scale=.9,length=90,randomness=0.9)
    #Preparing the data
    age_data = df['Q1'].value_counts().sort_index()
    #ploting the graph
    custom_color =sb.cubehelix_palette(10, rot=-.25, light=.7)
    plt.figure(figsize=(12,8))
    plt.style.use('seaborn')
    sb.countplot(x="Q1", data=df, palette = custom_color,order=age_data.index)
    #Decorating the plot
    plt.title('Distribution of Age',fontsize=16,weight = 'bold')
    plt.xticks(rotation=45,fontsize=14)
    plt.xlabel('Age',fontsize=14)

    # %% Age and Gender for distroubution of age

    #Let's narrow the genders to only men and women to facilitate the analysis(as they are the main categories)
    #filter df to man or woman answers only
    gender_df = df[df['Q2'].isin(['Man','Woman'])]
    # group by dist of age and gender adding how many results for each, then create a pivot table of the results
    table = gender_df.groupby(['Q1', 'Q2']).size().reset_index().pivot(columns='Q2', index='Q1', values=0)
    # apply seaborn settings to plot style
    plt.style.use('seaborn')
        
    # show plot, stacked
    ax=table.plot(stacked=True,kind='barh',figsize=(12,10),alpha=.7)

    # list of age distrobutions (index)
    index_list = table.index.values
    # total value of all participants that are man or woman
    total = table.values.sum()

    #ploting the annotation text
    for i in table.index :
        tot_x = 0
        for j in table.columns:
            
            # ratio between man and woman
            ratio = (table.loc[(i)][j])/ total
            # keeping position as we loop
            x_pos = table.loc[(i)][j]+ tot_x
            # keeping running total
            tot_x += table.loc[(i)][j]
            
            # if ratio is worth mentioning
            if(ratio >= 0.001):
                plt.text(x = x_pos - table.loc[(i)][j]/2, y = np.where(index_list == i)[0][0]
                         ,s= '%.1f'%(ratio*100)+'%' ,va='center', ha='center', size=12)
                
    #Decorating the plot
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left',prop={'size': 12})
    plt.xlabel('Count',fontsize=16)
    plt.xticks(fontsize=12)
    plt.title('Distribution of Age and Gender',fontsize=15,weight='bold')
    plt.annotate('20s Men are ruling the field' , xy =(1700,7),fontsize=24);

    # %% Top 10 countries

    #Here we specify the largest 10 countries for data science developers
    countries_with_most_developers = df['Q3'].value_counts().nlargest(10).sort_values(ascending=True)
    plt.figure(figsize=(12,8))
    countries_with_most_developers.plot(kind='barh',color=custom_color)
    #Decorating the plot
    plt.title('Countries with the most developers',fontsize=15,weight='bold')
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14)
    plt.xlabel('Count',fontsize=14)
    #Make a annotation to show the most obvious result
    plt.annotate('Indian Developers are the most' , xy =(2000,4),fontsize=24,color='navy');

    # %% World Map

    #make a new dataframe for residence country and count
    country_df = df['Q3'].value_counts().rename_axis('country').reset_index(name='counts')
    country_df = country_df[country_df['country'] != 'Other']

    #use geopy library to get location of countries
    from geopy.geocoders import Nominatim
    #import folium library to plot a geo map
    import folium
    from folium.plugins import MarkerCluster

    geolocator = Nominatim(user_agent='world_map')
    def geolocate(country):
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(country)
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        except:
            # Return missing value
            return np.nan

    # replace mislabeled Iran and North Korea
    country_df['country'].replace({'Iran, Islamic Republic of...' : 'Iran','Republic of Korea':'North Korea'},inplace=True)
     
    # add and split lat/long
    country_df['coord'] = country_df['country'].apply(lambda x : geolocate(x))
    #split the coordinates to latitude and longitude
    country_df['latitude']=  [x[0] for x in country_df['coord']]
    country_df['longitude'] = [x[1] for x in country_df['coord']]

    # get count of all users
    all_users = country_df.counts.sum()

    #create empty map
    world_map= folium.Map(tiles="cartodbpositron")
    marker_cluster = MarkerCluster().add_to(world_map)
    #for each coordinate, create circlemarker of user percent
    for i in range(len(country_df)):
            lat = country_df.iloc[i]['latitude']
            long = country_df.iloc[i]['longitude']
            radius=5
            popup_text = """
                        {}% of all Users <br>"""
            popup_text = popup_text.format('{:.2f}'.format(country_df.iloc[i]['counts']*100/country_df.counts.sum()))
            folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)
    #show the map
    world_map

    world_map.save("output/countries.html")

    import webbrowser
    webbrowser.open('C:\devel\Python\DontMatter\Kaggle\output/countries.html'.replace('\\','/'))

    # %% Education Background

    #preparing the data sort by counts
    education_df = df['Q4'].value_counts().sort_values(ascending=True)
    #ploting the graph
    plt.figure(figsize=(12,8))
    education_df.plot(kind='barh',color=custom_color)
    #Decorating the plot
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14)
    plt.title('Education Background',fontsize=15,weight='bold')
    plt.xlabel('Count',fontsize=14);


    # %% Years Experience

    #here we make a treemap using squarify library
    import squarify

    # Prepare Data
    years_order =  ['I have never written code', '< 1 years', '1-2 years', '3-5 years', '5-10 years', '10-20 years', '20+ years']
    exp_yrs_df = df['Q6'].value_counts()[years_order]
    perc = [str('{:5.1f}%'.format(i/exp_yrs_df.values.sum()*100)) for i in exp_yrs_df.values]
    labels = [el[0] + " \n " + el[1] for el in zip(exp_yrs_df.index, perc)]
    sizes = exp_yrs_df.values.tolist()

    # Draw Plot
    plt.figure(figsize=(12,8), dpi= 80)
    squarify.plot(sizes=sizes, label=labels, color=sb.color_palette('viridis'), alpha=.8,  text_kwargs={'fontsize':12,'linespacing':2})

    # Decorate
    plt.axis('off')
    plt.title('Experience Years',fontsize=15,weight='bold')
    plt.show();
