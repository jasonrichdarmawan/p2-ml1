import matplotlib.pyplot as plt
import seaborn as sns
import requests
import pandas as pd

def __histplot(features, target, df):
    """
    Usage: features parameter should be nominal features.
    """
    fig, axes = plt.subplots(4,4, figsize=(12,8), layout='constrained')

    for feature, ax in zip(features, axes.ravel()):
        sns.histplot(data=df, x=feature, hue=target, multiple='dodge', 
            stat='percent', common_norm=False, 
        ax=ax)
        if feature != 'gender':
            ax.get_legend().set_visible(False)
        if feature in [
            'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
            'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaymentMethod',
            'Contract'
        ]:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels(ax.get_xticklabels(), rotation=15, ha='right')
            
    return fig

def plot_categorical_features(df):
    return __histplot(
        features=[
            'gender', 'SeniorCitizen', 'Partner', 'Dependents', 
            'PhoneService', 'MultipleLines', 'InternetService', 
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
            'TechSupport', 'StreamingTV', 'StreamingMovies', 
            'PaperlessBilling', 'PaymentMethod', 'Contract'
        ],
        target='Churn',
        df=df
    )
    
def plot_numerical_features(df):
    df_c = df.copy()
    df_c['TotalCharges'] = pd.to_numeric(df_c['TotalCharges'], errors='coerce')
    
    return sns.pairplot(
        data=df_c[['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']], 
        hue='Churn'
    )