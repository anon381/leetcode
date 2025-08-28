
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    duplicate_rows = person.loc[person.duplicated('email') == True]
    
    result = duplicate_rows[['email']].drop_duplicates(keep='first')
    
    return result
