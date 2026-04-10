import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import warnings



def  num_fmt(x, pos=None):
    sign = "-" if x < 0 else ""
    x = abs(float(x))
    if x >= 1_000_000:
        return f"{sign}{x / 1_000_000:.1f}M"
    if x >= 1_000:
        return f"{sign}{x / 1_000:.0f}K"
    return f"{sign}{x:,.0f}"

def vis_corr(df, y:str, hue=None):
    warnings.filterwarnings('ignore')
    corr = df.select_dtypes(exclude=['object']).corr()
    corr = corr[[y]].sort_values(by=y, ascending=False)
    sns.heatmap(corr, cmap='Blues', annot=True, fmt='.2f')
    plt.show()
 
    num_feature = df.select_dtypes(exclude=['object']).drop(y,axis=1).columns
    n_col = 4
    n_row = (len(num_feature) + n_col -1) // n_col
    
    fig, ax = plt.subplots(n_row, n_col, figsize=(20, n_row*4))
    ax = ax.flatten()    
    
    for i, col in enumerate(num_feature):
        sns.scatterplot(data=df, x=col, y=y, ax=ax[i], hue=hue, palette='Set2')
        ax[i].set_title(f'{col} vs {y}')
        ax[i].yaxis.set_major_formatter(mtick.FuncFormatter(num_fmt))
        
    for j in range(i + 1, len(ax)):
        fig.delaxes(ax[j])
    
    plt.tight_layout()
    plt.show()
