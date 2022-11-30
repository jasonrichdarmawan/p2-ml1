def imp(df, **kwargs):
    df_c = df.copy()
    df_c.loc[((df_c['TotalCharges'].isna()) | (df_c['TotalCharges'] == ' ')) &
             (df_c['tenure'] == 0),'TotalCharges'] = 0
    return df_c

def imp_out(self, input_features):
    return self.kw_args['features']