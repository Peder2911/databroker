

import pandas as pd 

from databroker.resolvers.abc import Resolver

class FileResolver(Resolver):
    def get(self,variable):
        return pd.read_parquet(self.uri.path,columns=[variable]).values
