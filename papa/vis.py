import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from sklearn.preprocessing import LabelEncoder

import warnings

def  num_fmt(x, pos=None):
    sign = '-' if x < 0 else ''
    x = abs(float(x))
    if x >= 1_000_000:
        return f'{sign}{x / 1_000_000:.1f}M'
    if x >= 1_000:
        return f'{sign}{x / 1_000:.0f}K'
    return f'{sign}{x:,.0f}'

def vis_corr_dep(df, y:str, hue=None):
    warnings.filterwarnings('ignore')
    
    object_col = df.select_dtypes(include=['object','str']).columns
    for i in object_col:
        le = LabelEncoder()
        df[i] = le.fit_transform(df[i])
    
    corr = df.corr()
    corr = corr[[y]].sort_values(by=y, ascending=False)
    plt.figure(figsize=(3,len(corr)*0.25))
    sns.heatmap(corr, cmap='Blues', annot=True, fmt='.2f')
    plt.title(f'Correlationt {y} vs All Features', fontsize=10)
    plt.show()
 
    num_feature = corr.drop(y,axis=0).index
    n_col = 3
    n_row = (len(num_feature) + n_col -1) // n_col
    df_corr = pd.DataFrame(corr).reset_index(names='feature')
    
    fig, ax = plt.subplots(n_row, n_col, figsize=(15, n_row*4))
    ax = ax.flatten()    
    
    for i, col in enumerate(num_feature):
        current_corr = df_corr.loc[df_corr['feature'] == col, y].values[0]
        sns.scatterplot(data=df, x=col, y=y, ax=ax[i], hue=hue, palette='Set2')
        ax[i].set_title(f'{col} vs {y} ({current_corr:.2f})', fontsize=14)
        ax[i].yaxis.set_major_formatter(mtick.FuncFormatter(num_fmt))
        ax[i].xaxis.set_major_formatter(mtick.FuncFormatter(num_fmt))
        
    for j in range(i + 1, len(ax)):
        fig.delaxes(ax[j])
    
    plt.tight_layout()
    plt.show()
