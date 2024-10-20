import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col('date')


# Clean data
df_values = df[
(df['values'] >= df['values'].quantile(0.025)) &
(df['values'] <= df['values'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    
    plt.plot(df.index, df['values'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019.')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    plt.show()
    



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df.unstack()
    
   
    # Draw bar plot

    fig = df.plot.bar(legend=True, xlabel='Years', ylabel='Average Page Views').figure
    plt.legend (['Januray', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])    



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    sns.boxplot(x=year['Year']) 



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

