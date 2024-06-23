# CS-340-Project-2
Web Application Dashboard 


# Grazioso Salvare Animal Rescue Dashboard

## Project Overview

This project involves creating an interactive dashboard for Grazioso Salvare, a company specializing in animal rescue operations. The dashboard allows users to filter and view animal data based on different rescue operations: Water Rescue, Mountain/Wilderness Rescue, and Disaster/Individual Tracking.

## Required Functionality

The dashboard provides the following functionalities:

1. **Data Filtering**: Users can filter animal data based on rescue operations using radio buttons.
2. **Interactive Data Table**: Displays filtered data in an interactive table with sorting and filtering capabilities.
3. **Graphs and Maps**: Shows visual representations of the data, including a pie chart and a map with markers for the animals' locations.

### Screenshots

1. **Initial State**:
   
   ![Initial State](Initial_state.png)
   ![Initial State Graph and Map](Initial_state_map.png)

2. **Water Rescue**:
   
   ![Water Rescue](Water.png)
   ![Water Rescue Graph and Map](Water_map.png)

3. **Mountain/Wilderness Rescue**:
   
   ![Mountain/Wilderness Rescue](Wild.png)
   ![Mountain/Wilderness Rescue Graph and Map](Wild_map.png)

4. **Disaster/Individual Tracking**:
   
   ![Disaster/Individual Tracking](Disaster.png)
   ![Disaster/Individual Tracking Graph and Map](Disaster_map.png)

## Tools and Rationale

### MongoDB
MongoDB was chosen as the database for this project due to its flexibility in handling JSON-like documents, which are well-suited for the dynamic schema of animal rescue data. MongoDB's compatibility with Python through the `pymongo` library allows for seamless data operations. Key qualities include:
- **Flexibility**: Handles dynamic schemas effectively.
- **Scalability**: Easily scales to handle large volumes of data.
- **Performance**: Optimized for read and write operations, making it suitable for applications requiring real-time data processing.

### Dash
Dash by Plotly was used to create the web application. It provides a robust framework for building analytical web applications without the need for extensive JavaScript knowledge. Dash combines the ease of using Flask for the backend with React for the front-end, making it ideal for creating interactive and dynamic dashboards.

### Other Tools
- **Pandas**: For data manipulation and conversion between CSV and MongoDB. It provides powerful data structures to perform data analysis efficiently.
- **Plotly Express**: For creating interactive graphs. It simplifies the process of generating complex visualizations.
- **Dash Leaflet**: For integrating maps into the Dash application, allowing for geographic visualization of animal locations.

## Steps Taken

### 1. Data Preparation
Loaded and cleaned the CSV data, then inserted it into the MongoDB database. Here is a snippet of the code used:

```python
import pandas as pd
from pymongo import MongoClient

# Read the CSV file
df = pd.read_csv('/mnt/data/aac_shelter_outcomes (1).csv')

# Initialize MongoDB client and specify database and collection
client = MongoClient('mongodb://aacuser:SNHU1234@nv-desktop-services.apporto.com:31111')
db = client['AAC']
collection = db['animals']

# Convert DataFrame to dictionary and insert into MongoDB
data_dict = df.to_dict("records")
collection.insert_many(data_dict)
print("Data inserted successfully")
```

### 2. CRUD Operations
Implemented CRUD operations for interacting with the MongoDB database. This allowed for seamless data management within the dashboard.

### 3. Dashboard Development
Built the dashboard using Dash, including components for data filtering, tables, graphs, and maps. Here is a snippet for creating the data table and integrating the map:

```python
app.layout = html.Div([
    html.H1('Grazioso Salvare Animal Rescue Dashboard'),
    dcc.RadioItems(
        id='filter-type',
        options=[
            {'label': 'Water Rescue', 'value': 'water_rescue'},
            {'label': 'Mountain/Wilderness Rescue', 'value': 'mountain_wilderness_rescue'},
            {'label': 'Disaster/Individual Tracking', 'value': 'disaster_individual_tracking'},
            {'label': 'Reset', 'value': 'reset'}
        ],
        value='reset',
        labelStyle={'display': 'inline-block'}
    ),
    dash_table.DataTable(
        id='datatable-id',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10
    ),
    dcc.Graph(id='graph-id'),
    dl.Map(id='map-id', center=[30.75, -97.48], zoom=10, children=[
        dl.TileLayer(id="base-layer-id")
    ])
])
```

### 4. Testing
Tested the dashboard by applying different filters and ensuring the correct data display and interactivity. Each filter was applied, and the resulting data was verified through visual inspection of the graphs and maps.

## Challenges and Solutions

### Challenge 1: Data Cleaning
- **Issue**: Ensuring data consistency and handling missing values.
- **Solution**: Implemented rigorous data cleaning procedures during the initial data preparation phase, including handling missing values and ensuring data types were consistent.

### Challenge 2: MongoDB Integration
- **Issue**: Ensuring a stable connection and handling CRUD operations efficiently.
- **Solution**: Used the `pymongo` library to handle database operations with appropriate error handling mechanisms to ensure a stable connection.

### Challenge 3: Dynamic Dashboard Updates
- **Issue**: Updating dashboard components dynamically based on user inputs.
- **Solution**: Utilized Dash's callback functions to ensure real-time updates of the data table, graphs, and maps based on the selected filters.

Here is an example of a callback function used to update the dashboard:

```python
@app.callback(
    [Output('datatable-id', 'data'),
     Output('graph-id', 'figure'),
     Output('map-id', 'children')],
    [Input('filter-type', 'value')]
)
def update_dashboard(filter_type):
    if filter_type == 'reset':
        data = df
    else:
        data = get_filtered_data(filter_type)
    fig = px.pie(data, names='breed', title='Preferred Animals')
    map_markers = [
        dl.Marker(position=[row['location_lat'], row['location_long']],
                  children=[dl.Tooltip(row['breed']), dl.Popup(row['name'])])
        for index, row in data.iterrows()
    ]
    return data.to_dict('records'), fig, map_markers
```

## Resources

- [Dash Documentation](https://dash.plotly.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [My GitHub Repository for Screenshots](https://github.com/EmpressCatbug/CS-340-Project-2)

This documentation provides a comprehensive overview of the project, the tools used, the steps taken, challenges faced, and solutions implemented. It aims to ensure that Grazioso Salvare can understand and maintain the dashboard effectively.
