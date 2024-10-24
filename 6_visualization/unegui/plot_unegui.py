import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px

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
    plt.savefig(f'6_visualization/unegui/figures\price_box_{date}.png')


# plot box plot

df = pd.read_csv('6_visualization/unegui/data/daily_cleaned.csv')

df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%d')
df['date_dt'] = df['date']
df['date'] = df['date'].dt.strftime('%b-%d')
df['date_long'] = df['date_dt'].dt.strftime('%y-%m-%d')

df_ = df[(df['date_dt'] >= '2024-10-17') & (df['date_dt'] <= '2024-10-23')]
plot_date_week(df_)
