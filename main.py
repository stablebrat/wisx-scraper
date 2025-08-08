from scrape_wis import get_dispatch_data
from update_sheet import update_google_sheet
import pandas as pd



excel_path = get_dispatch_data()
df = pd.read_excel(excel_path)
if df is not None and not df.empty:
    update_google_sheet(df)
else:
    print("❌ No data to export.")