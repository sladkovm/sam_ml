class RemoveOutliers():
    ''' Removes outliers from the dataframe using the outer fence (+/- 3*IQR) criteria

    RemoveOutliers class follows the same API as any scikit-learn classes
    and exposes typical fit, transoform and fit_transform public methods
    '''


    def __init__(self):
        pass


    def fit(self, df):
        '''calculates filter'''
        self.df = df
        self.df_stats = self._statistics(self.df)
        self.filter = self._filter()
        return self


    def transform(self, df):
        '''returns a filter copy of the DataFrame'''
        return df[self.filter].copy()


    def fit_transform(self, df):
        '''calculates filter and returns a filtered copy of the DataFrame'''
        ro = self.fit(df)
        return ro.transform(df)


    def _statistics(self, df):
        '''returns DataFrame containing a descriptive statistics of the dataset'''
        df_stats = df.describe()
        df_stats.loc['IQR', :] = df_stats.loc['75%', :] - df_stats.loc['25%', :]
        df_stats.loc['OUF', :] = df_stats.loc['75%', :] + 3.0 * df_stats.loc['IQR', :]
        df_stats.loc['OLF', :] = df_stats.loc['25%', :] - 3.0 * df_stats.loc['IQR', :]
        return df_stats


    def _filter(self):
        '''returns a logica filter based on OuterFences outliers removal'''
        rv = self.df.index.to_series()
        rv[:] = True
        for col in list(self.df.columns):
            f_lower = (self.df[col] > self.df_stats.loc['OLF', col])
            f_upper = (self.df[col] < self.df_stats.loc['OUF', col])
            rv = rv & f_lower & f_upper
        return rv