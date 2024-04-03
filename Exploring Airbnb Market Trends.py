import pandas as pd

# Load data from CSV, Excel, and TSV files
airbnb_price = pd.read_csv('dataset/airbnb_price.csv')
airbnb_room_type = pd.read_excel('dataset/airbnb_room_type.xlsx')
airbnb_last_review = pd.read_csv('dataset/airbnb_last_review.tsv', sep='\t')

# Take a quick look at the data
print(airbnb_price.head())
print(airbnb_room_type.head())
print(airbnb_last_review.head())

# Merge DataFrames on 'listing_id'
merged_data = pd.merge(airbnb_price, airbnb_room_type, on='listing_id')
merged_data = pd.merge(merged_data, airbnb_last_review, on='listing_id')

# Take a look at the merged data
print(merged_data.head())

# Convert 'last_review' to datetime format
merged_data['last_review'] = pd.to_datetime(merged_data['last_review'])

# Find the earliest and most recent review dates
first_reviewed = merged_data['last_review'].min()
last_reviewed = merged_data['last_review'].max()

# Clean 'room_type' data
merged_data['room_type'] = merged_data['room_type'].str.lower()

# Count the number of private rooms
nb_private_rooms = merged_data[merged_data['room_type'] == 'private room'].shape[0]

# Remove non-numeric characters and convert 'price' to float
merged_data['price'] = merged_data['price'].str.replace(r'\D', '')
merged_data['price'] = merged_data['price'].astype(float)
avg_price = merged_data['price'].mean()


# Create the DataFrame with the four solution values
review_dates = pd.DataFrame({
    'first_reviewed': [first_reviewed],
    'last_reviewed': [last_reviewed],
    'nb_private_rooms': [nb_private_rooms],
    'avg_price': [round(avg_price, 2)]
})

# Display the DataFrame
print(review_dates)

