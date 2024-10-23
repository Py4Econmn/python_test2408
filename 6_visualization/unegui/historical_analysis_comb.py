import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px

def plot_date_orig(df):

    date = df['date_long'].unique()[0] if len(df['date_long'].unique()) == 1 else 'Бүгд'

    # Calculate median price for each location
    median_prices = df.groupby(location)[price].median().sort_values()
    num_ads = df[location].value_counts()[median_prices.index]
    sorted_locations = median_prices.index
    sorted_names = []
    for loc in median_prices.index:
        num_ad = num_ads[loc]
        space = '' if int(num_ad) > 1000 else ' '
        formattted_str = f'{loc}{space}({num_ad})'
        sorted_names.append(formattted_str)


    # Create the boxplot
    plt.figure(figsize=(10, 6))
    boxplot = plt.boxplot([df[df[location] == loc][price] for loc in sorted_locations], labels=sorted_names)
    plt.ylabel('сая төгрөгөөр')
    plt.xlabel('Байршил (зарын тоо)')
    plt.title(f'Орон сууцны м2-ын үнэ ({date} өдрийн {len(df)} ширхэг зар, медиан үнэ {df[price].median():.2f} сая төгрөг)')
    # plt.text(0.5,3.1,'Ерөнхий медиан 3.4 сая төг')
    plt.grid(True)
    plt.xticks(rotation=90)
    plt.text(1,-6,'Өгөгдлийн эх сурвалж: unegui.mn')
    plt.axhline(y=3.4, color='gray', linestyle='--')
    for line in boxplot['medians']:
        line.set_color('black')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.4)
    # plt.show()
    fname = date.replace('/','_')
    plt.savefig(f'figures/fig_date_{fname}.png')


def plot_date(df,date='бүгд'):
    
    if date == 'бүгд':
        df = df 
    else:
        df = df[df['date_long'] == date] 

    df = df[~df['mylocation'].isna()]
    median_price = df['price_m2'].median()
    median_price_loc = df.groupby('mylocation')['price_m2'].median().sort_values()
    sorted_loc = median_price_loc.index
    num_ads_loc = df['mylocation'].value_counts()
    sorted_label = []
    for loc in sorted_loc:
        sorted_label.append(f'{loc} ({num_ads_loc[loc]})')

    plt.figure(figsize=(16,9))
    ax = sns.boxplot(data=df,x='mylocation',y='price_m2',order=sorted_loc, color='black',medianprops={'color': 'white'})
    ax.set_xticklabels([sorted_label[i] for i in range(len(sorted_loc))], rotation=90)

    plt.title(f'Орон сууцны үнэ (м2, байршлаар), өдөр: {date}, зарын тоо: {len(df)}, медиан үнэ: {median_price:.2f}₮')
    plt.xlabel('Байршил (зарын тоо)')
    plt.ylabel('Үнэ (м2, сая төгрөгөөр)')
    plt.xticks(rotation=90,fontsize=6)
    plt.axhline(median_price,color='r',linestyle='--')

    # Highlight a specific location
    match_string = 'Яармаг'
    highlight_color = 'red'
    # Find the matching location from sorted_loc
    matching_location_index = None
    for i, loc in enumerate(sorted_loc):
        if match_string in sorted_label[i]:
            matching_location_index = i
            break
    # Highlight the specific location if found
    if matching_location_index is not None:
        ax.get_xticklabels()[matching_location_index].set_color(highlight_color)
        ax.get_xticklabels()[matching_location_index].set_fontweight('bold')


    plt.grid(True)
    plt.subplots_adjust(bottom=0.3)
    # plt.show()
    plt.savefig(f'figures\price_date_{date}.png')

def plot_date_week(df,date='бүгд'):

    df = df[~df['mylocation'].isna()]
    median_price = df['price_m2'].median()
    median_price_loc = df.groupby('mylocation')['price_m2'].median().sort_values()
    sorted_loc = median_price_loc.index
    num_ads_loc = df['mylocation'].value_counts()
    sorted_label = []
    for loc in sorted_loc:
        sorted_label.append(f'{loc} ({num_ads_loc[loc]})')

    plt.figure(figsize=(16,9))
    ax = sns.boxplot(data=df,x='mylocation',y='price_m2',order=sorted_loc, color='black',medianprops={'color': 'white'})
    ax.set_xticklabels([sorted_label[i] for i in range(len(sorted_loc))], rotation=90)

    plt.title(f'Зураг 4. Орон сууцны үнэ (м2, байршлаар), өдөр: Сарын сүүлийн 7 хоног, зарын тоо: {len(df)}, медиан үнэ: {median_price:.2f}₮')
    plt.xlabel('Байршил (зарын тоо)')
    plt.ylabel('Үнэ (м2, сая төгрөгөөр)')
    plt.xticks(rotation=90,fontsize=6)
    plt.axhline(median_price,color='r',linestyle='--')

    # Highlight a specific location
    match_string = 'Яармаг'
    highlight_color = 'red'
    # Find the matching location from sorted_loc
    matching_location_index = None
    for i, loc in enumerate(sorted_loc):
        if match_string in sorted_label[i]:
            matching_location_index = i
            break
    # Highlight the specific location if found
    if matching_location_index is not None:
        ax.get_xticklabels()[matching_location_index].set_color(highlight_color)
        ax.get_xticklabels()[matching_location_index].set_fontweight('bold')


    plt.grid(True)
    plt.subplots_adjust(bottom=0.3)
    # plt.show()
    plt.savefig(f'figures\price_week_{date}.png')

def plot_loc(df):

    loc = df[location].unique()[0] if len(df[location].unique()) == 1 else 'Бүгд'
    # Calculate median price for each location
    sorted_date = np.sort(df['date_long'].unique())
    num_ads = df['date_long'].value_counts()[sorted_date]
    sorted_names = []
    for date in sorted_date:
        num_ad = num_ads[date]
        formattted_str = f'{date}({num_ad})'
        space_length = 13 - len(formattted_str)
        spaces = ' ' * space_length
        formattted_str = f'{date}{spaces}({num_ad})'
        sorted_names.append(formattted_str)


    # Create the boxplot
    plt.figure(figsize=(10, 6))
    boxplot = plt.boxplot([df[df['date_long'] == date][price] for date in sorted_date], labels=sorted_names)
    plt.ylabel('сая төгрөгөөр')
    plt.xlabel('Өдөр (зарын тоо)')
    plt.title(f'Орон сууцны м2-ын үнэ, медиан үнэ {df[price].median():.2f} сая төгрөг. Байршил: {loc}, зарын тоо: {len(df)}')
    plt.grid(True)
    plt.xticks(rotation=90)
    plt.text(1,-5,'Өгөгдлийн эх сурвалж: unegui.mn')
    plt.axhline(y=3.4, color='gray', linestyle='--')
    for line in boxplot['medians']:
        line.set_color('black')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3)
    # plt.show()
    plt.savefig(f'figures/fig_loc_{loc}.png')

def plot_hist(df,date = '24-05-31'):
    if date == 'бүгд':
        df = df 
    else:
        df = df[df['date_long'] == date] 

    plt.figure(figsize=(16,9))
    plt.hist(df['price_m2'],bins=25,color = "skyblue") # ,density=True  df['price_m2'].plot.hist(bins=50)
    plt.title(f'Үнэ (м2) тархалт, өдөр: {date}, зарын тоо: {len(df)}')
    # plt.show()
    plt.savefig('figures\price_hist.png')


def plot_hist_mult(df):

    # Define colors for each month
    colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '']  # Modify colors as needed
    plt.figure(figsize=(10, 6))
    # Plot each month's histogram
    for (month, group), color in zip(df.groupby('month'), colors):
         sns.kdeplot(group['price_m2'], label=str(month), color=color, linewidth=2)

    plt.title('Зураг 3. Үнийн тархалтын хөдөлгөөн')
    plt.xlabel('Үнэ (м2)')
    plt.ylabel('Харьцангуй давтамж')
    plt.legend(title='Сар')
    plt.grid(True)
    # plt.show()
    plt.savefig('figures\price_hist_mult.png')


def plot_hour(df):
    df['weekday'] = df['date_dt'].dt.strftime('%a')
    pt = df.pivot_table(index=['date','weekday'],columns='hour',values='ad_id',aggfunc='count',fill_value=0)
    plt.figure(figsize=(16,9))
    sns.heatmap(pt,cmap='YlGnBu',annot=True,fmt='d', annot_kws={"size": 6})
    plt.ylabel('Өдөр ба гараг')
    plt.xlabel('Цаг')
    plt.title(f'Зураг 5. Зарын тоо (нийт: {len(df)})')
    # plt.text(5, 5, 'Custom text below the heatmap', ha='center', va='center', fontsize=12)
    plt.text(-3,72,'Өгөгдлийн эх сурвалж: unegui.mn')
    plt.subplots_adjust(bottom=0.15)
    # plt.show()
    plt.savefig('figures\day_hour.png')

def plot_price_evolll(df):
    # Calculate median price for each location by month
    df = df[df['month'].isin([4, 8])]
    monthly_median = df.groupby(['mylocation', 'month'])['price_m2'].median().unstack()
    monthly_median = monthly_median[[4, 8]].dropna()

    monthly_median['pct_change'] = (monthly_median[8] - monthly_median[4]) / monthly_median[4] * 100
    monthly_median = monthly_median[monthly_median['pct_change'].abs() <= 20]
    monthly_median = monthly_median.drop(columns='pct_change')

    # Calculate overall median price for each location
    overall_median = monthly_median[[4, 8]].median(axis=1).sort_values()
    
    # Sort locations by overall median price
    sorted_locations = overall_median.index
    
    
    # Define markers for each month
    markers = ['s', '^'] #, '0','D', 'P']  # Different markers for each month
    colors = ['b', 'r'] # ,'g', 'c', 'm']
    months = monthly_median.columns.astype(str)  # Extract month names

    plt.figure(figsize=(12, 6))
    
    for i, loc in enumerate(sorted_locations):
        for j, month in enumerate(months):
            plt.scatter(i, monthly_median.loc[loc, int(month)], marker=markers[j], color=colors[j], s=50, label=month if i == 0 else "")
    
    # Set x-axis to location names
    plt.xticks(range(len(sorted_locations)), sorted_locations, rotation=90,fontsize=8)
    
    # Labels and title
    plt.ylabel('сая төгрөгөөр')
    plt.xlabel('Байршил')
    plt.title(f'Зураг 2. Орон сууцны м2-ын үнэ (медиан үнэ, сүүлийн 5 сар)')
    
    # Add legend
    plt.legend(title="Month", loc='upper left', bbox_to_anchor=(1, 1))
    
    # Grid and other details
    plt.grid(True)
    plt.text(-1, -6, 'Өгөгдлийн эх сурвалж: unegui.mn')
    
    plt.tight_layout()
    plt.subplots_adjust(right=0.8, bottom=0.3)
    plt.show()


def plot_price_evol(df,first = 4, last = 8):
    # Filter for only April and August
    df = df[df['month'].isin([first, last])]
    
    # Calculate median price for each location by month
    monthly_median = df.groupby(['mylocation', 'month'])['price_m2'].median().unstack()
    
    # Keep only July (first) and August (last), and drop rows with NaN in either month
    monthly_median = monthly_median[[first, last]].dropna()
    
    # Calculate the percentage change between April and July
    monthly_median['pct_change'] = (monthly_median[last] - monthly_median[first]) / monthly_median[first] * 100
    
    # Filter out locations with a percentage change greater than 20%
    monthly_median = monthly_median[monthly_median['pct_change'].abs() <= 20]
    
    # Calculate overall median price for each location
    overall_median = monthly_median[[first, last]].median(axis=1).sort_values()
    
    # Sort locations by overall median price
    sorted_locations = overall_median.index
    monthly_median = monthly_median.loc[sorted_locations]
    
    # Define markers and colors for each month
    markers = ['s', '^']  # Different markers for April and July
    colors = ['b', 'r']  # Colors for April and July
    months = [first, last]      # April and July
    
    # Plotting setup
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Plot the median prices for each location with different markers and colors
    for i, loc in enumerate(sorted_locations):
        for j, month in enumerate(months):
            ax1.scatter(i, monthly_median.loc[loc, month], marker=markers[j], color=colors[j], s=50, label=f'{first}-р сар' if month == first and i == 0 else f'{last}-р сар' if month == last and i == 0 else "")
    
    # Adding a secondary y-axis for the percentage change
    pattern = '*' #'/'
    ax2 = ax1.twinx()
    ax2.bar(range(len(sorted_locations)), monthly_median['pct_change'], color='brown', alpha=0.8, width=0.3, align='center', label='Өөрчлөлт %') # , hatch=pattern
    ax2.set_ylabel('өөрчлөлт (%)')
    # ax2.set_ylim(monthly_median['pct_change'].min() - 10, monthly_median['pct_change'].max() + 10)
    ax2.set_ylim(-40, 20)
    
    # Set x-axis to location names
    ax1.set_xticks(range(len(sorted_locations)))
    ax1.set_xticklabels(sorted_locations, rotation=90, fontsize=8)
    
    # Labels and title for the scatter plot
    ax1.set_ylabel('сая төгрөг')
    ax1.set_xlabel('Байршил')
    ax1.set_title(f'Зураг 2. Орон сууцны м2-ын үнэ ба өөрчлөлт (медиан үнэ, 2024 оны {first} болон {last} сар)')
    
    # Add legend for scatter plot and percentage change
    lines, labels = ax1.get_legend_handles_labels()
    bars, bar_labels = ax2.get_legend_handles_labels()
    ax1.legend(lines + bars, labels + bar_labels, loc='lower right')
    
    # Grid and other details
    # ax1.grid(True)
    # Add vertical grid lines at every third location
    for i in range(0, len(sorted_locations), 5):
        ax1.axvline(x=i, color='gray', linestyle='--', linewidth=0.8)
    plt.text(-1, -60, 'Өгөгдлийн эх сурвалж: unegui.mn')
    
    plt.tight_layout()
    plt.subplots_adjust(right=0.8, bottom=0.3)
    # plt.show()
    plt.savefig(f'figures/price_change_dynamic.png')



import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

def plot_monthly_median(df,first=4, last=8):
    # Map month numbers to month names
    month_names = {
        1: '1-р сар', 2: '2-р сар', 3: '3-р сар', 4: '4-р сар', 5: '5-р сар', 6: '6-р сар',
        7: '7-р сар', 8: '8-р сар', 9: '9-р сар', 10: '10-р сар', 11: '11-р сар', 12: '12-р сар'
    }
    
    # Calculate median price for each month across all locations
    monthly_median = df.groupby('month')['price_m2'].median()
    
    # Calculate the number of ads for each month
    monthly_ad_counts = df.groupby('month').size()
    
    # Convert month numbers to month names
    monthly_median.index = monthly_median.index.map(month_names)
    monthly_ad_counts.index = monthly_ad_counts.index.map(month_names)
    
    # Create labels with month names and number of ads
    x_labels = [f'{m} \n ({monthly_ad_counts[m]:,} ш зар)' for m in monthly_median.index]

    # Plotting setup
    plt.figure(figsize=(10, 5))
    
    # Plot median prices as a bar plot
    bars = plt.bar(monthly_median.index, monthly_median.values, color='#010f05', alpha=0.5, edgecolor='black', label='Monthly Median Price')
    
    # Add labels and title
    plt.title('Зураг 1. Медиан үнэ (м2, сая төг, бүх байршил)',fontdict={'fontweight': 'bold'})
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=0, ha='center')
    
    # Set y-axis limits
    plt.ylim(3.4, 3.65)
    plt.gca().set_yticklabels([])
    
    
    # Annotate each bar with its height
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,  # X position
            height + 0.01,  # Y position (slightly above the bar)
            f'{height:.2f}',  # Text (formatted to two decimal places)
            ha='center',  # Horizontal alignment
            va='bottom',  # Vertical alignment
            fontsize=10,  # Font size
            color='black'  # Text color
        )
    
    # Update x-axis labels
    plt.xticks(ticks=plt.xticks()[0], labels=x_labels)
    
    gr      = monthly_median[month_names[last]]/monthly_median[month_names[last-1]]*100-100
    txt_dir = 'өсчээ' if gr >= 0 else 'буурчээ'
    plt.text(-0.5, 3.63, f'{month_names[last-1]}аас {month_names[last]}ын хооронд байрны медиан үнэ {gr:.1f}%-иар {txt_dir}!',color='#010f05',fontsize=12)
    plt.text(-0.5, 3.35, 'Өгөгдлийн эх сурвалж: unegui.mn')

    # Show the plot
    plt.tight_layout()
    # plt.show()
    plt.savefig(f'figures/price_median_dynamic.png')








df3 = pd.read_csv('historical_data/2403/daily_cleaned.csv')
df4 = pd.read_csv('historical_data/2404/daily_cleaned.csv')
df5 = pd.read_csv('historical_data/2405/daily_cleaned.csv')
df6 = pd.read_csv('historical_data/2406/daily_cleaned.csv')
df7 = pd.read_csv('historical_data/2407/daily_cleaned.csv')
df8 = pd.read_csv('historical_data/2408/daily_cleaned.csv')
df9 = pd.read_csv('historical_data/2409/daily_cleaned.csv')
df = pd.concat([df3,df4,df5,df6,df7,df8,df9],ignore_index=True)

df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%d')
df['month'] = df['date'].dt.month
df = df[(df['date'].dt.year == 2024) & (df['date'].dt.month >= 3)]
df = df[(df['date'].dt.year == 2024) & (df['date'].dt.month <= 9)]
df['date_dt'] = df['date']
df['date'] = df['date'].dt.strftime('%b-%d')
df['date_long'] = df['date_dt'].dt.strftime('%y-%m-%d')



# remove duplicates
df = df.sort_values(by=['ad_id','date'])
df = df.drop_duplicates(subset=['ad_id','date'],keep='first')

# df = df.drop_duplicates(subset=['ad_id'],keep='first')

location = 'mylocation'
price = 'price_m2'


# Зураг 1
df_ = df[(df['date_dt'].dt.year == 2024) & (df['date_dt'].dt.month >= 4)]
plot_monthly_median(df_,first=4, last=9)    

# plot_price_evol(df) Зураг 2
plot_price_evol(df,first = 8, last = 9)

# Зураг 3
df_ = df[(df['date_dt'].dt.year == 2024) & (df['date_dt'].dt.month >= 8)]
plot_hist_mult(df_)

# Зураг 4
df_ = df[(df['date_dt'] >= '2024-09-24') & (df['date_dt'] <= '2024-09-30')]
plot_date_week(df_)

# Зураг 5
df_ = df[(df['date_dt'].dt.year == 2024) & (df['date_dt'].dt.month >= 9)]
plot_hour(df_)

# pdate = '24-08-31'
# plot_date(df,pdate)
# plot_loc(df)
# pivot_table = df.pivot_table(index=['date_long','weekday'],columns='hour',values='ad_id',aggfunc='count',fill_value=0)

# plt.figure(figsize=(12, 8))  # Adjust the size as needed
# sns.heatmap(pivot_table, cmap='YlGnBu') # , cbar_kws={'label': 'Count'}, , annot=True, fmt='d',
# plt.title('Зарын тоо (оруулсан цагаар)')
# plt.ylabel('Өдөр ба гараг')
# plt.xlabel('Цаг')
# plt.show()
# # plt.savefig(f'figures/fig_hour.png')
# plt.close()


# # maybe just group by weekday
# df[price] = pd.to_numeric(df[price])
# # df = df[(df[price] < 10) & (df[price] < 14)]

# # price evoluation over time
# df_p = df.groupby([location,'date_long']).agg({price: 'max'}).reset_index()
# fig = px.line(df_p, x='date_long', y=price, color=location, title='Median Price Over Time by Location')
# fig.update_layout(xaxis_title='date', yaxis_title='Median Price')
# fig.show()
# plt.close()

# # price evolution over time in a location
# mylocation = 'Яармаг'
# df_location = df[df[location] == mylocation]
# df_grouped = df_location.groupby('date').agg({
#     price: ['max', 'min', 'median']
# }).reset_index()
# df_grouped.columns = ['date', 'max_price', 'min_price', 'median_price']
# df_melted = df_grouped.melt(id_vars='date', value_vars=['max_price', 'median_price', 'min_price'], 
#                             var_name='Statistic', value_name='Price')
# fig = px.line(df_melted, x='date', y='Price', color='Statistic', title=f'Price Statistics Over Time for Location {mylocation}')
# fig.update_layout(xaxis_title='date', yaxis_title='Price')
# fig.show()
# plt.close()

# pdate = 'May-01'
# df_f = df[df['date'] == pdate]
# plot_date(df_f)

# pdate = 'May-31'
# df_l = df[df['date'] == pdate]
# plot_date(df_l)


# # df1 = df[df[location] == 'Яармаг']
# # plot_loc(df1)
# # # df0329 = df[df['date'] == '3/29/2024']
# # # real_plot(df0329)


# # df1.groupby('date')['date'].count() / df.groupby('date')['date'].count() 
# # df1.groupby('date')['date'].count().mean()


# # import folium
# # import pandas as pd

# # # Sample DataFrame with latitude and longitude coordinates for Ulaanbaatar
# # data = {
# #     'name': ['Location 1', 'Location 2', 'Location 3'],
# #     'latitude': [47.92123, 47.91555, 47.92722],
# #     'longitude': [106.91856, 106.91753, 106.90545]
# # }

# # df = pd.DataFrame(data)

# # # Initialize a folium map centered on Ulaanbaatar
# # ulaanbaatar_map = folium.Map(location=[47.92123, 106.91856], zoom_start=12)

# # # Add points to the map
# # for idx, row in df.iterrows():
# #     folium.Marker(
# #         location=[row['latitude'], row['longitude']],
# #         popup=row['name'],
# #         icon=folium.Icon(color='blue', icon='info-sign')
# #     ).add_to(ulaanbaatar_map)

# # # Save the map to an HTML file
# # ulaanbaatar_map.save('ulaanbaatar_map.html')

# # # Display the map in a Jupyter Notebook (if you are using one)
# # ulaanbaatar_map
