import pandas as pd
import json

# The data string (your input)
data_string = """{
     "-NpHFNn1nVOFFERi9VVy": {
       "Accuracy": "Somewhat accurate",
       "Age": 26,
       "Artist": "Sia",
       "Country": "Ghana",
       "Date": "2024-01-28",
       "Diversity": true,
       "Education Level": "Bachelor's degree",
       "Email": "mambisigermain@gmail.com",
       "Gender": "Male",
       "Interface Design": "Good",
       "Introduction to new artist_genre": true,
       "Is the platform recommendable to other": "Very likely",
       "Platform Usage": "11-15",
       "Profession": "Nurse",
       "Relevance": "Very relevant",
       "Specify platforms": [
         "Apple Music",
         "Youtube"
       ],
       "Time": "22:47:20",
       "Transparency": false,
       "Usage of Music Streaming Platforms": true,
       "Usage of Platforms": "More than once a day"
     },
     "-NpHFNn2nVOFFERi9VVy": {
       "Accuracy": "Somewhat accurate",
       "Age": 26,
       "Artist": "Sia",
       "Country": "Ghana",
       "Date": "2024-01-28",
       "Diversity": true,
       "Education Level": "Bachelor's degree",
       "Email": "mambisigermain@gmail.com",
       "Gender": "Male",
       "Interface Design": "Good",
       "Introduction to new artist_genre": true,
       "Is the platform recommendable to other": "Very likely",
       "Platform Usage": "11-15",
       "Profession": "Nurse",
       "Relevance": "Very relevant",
       "Specify platforms": [
         "Apple Music",
         "Youtube"
       ],
       "Time": "22:47:20",
       "Transparency": false,
       "Usage of Music Streaming Platforms": true,
       "Usage of Platforms": "More than once a day"
     }
}"""

# Parse the JSON string
data = json.loads(data_string)

# Process each entry
processed_data = []
for key, value in data.items():
    # Convert the "Specify platforms" list to a string
    value["Specify platforms"] = ", ".join(value["Specify platforms"])
    processed_data.append(value)

# Create a DataFrame
df = pd.DataFrame(processed_data)

# Export to Excel
excel_file = "output.xlsx"
df.to_excel(excel_file, index=False)

print(f"Data has been exported to {excel_file}")
