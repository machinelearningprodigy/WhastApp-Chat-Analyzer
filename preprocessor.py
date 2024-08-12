import pandas as pd
import re

def preprocess(data):
    # Define the regex pattern for dates and times
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?[ap]m?\s?[-]?\s?'

    # Split the messages using the regex pattern
    messages = re.split(pattern, data)
    
    # Find all the dates in the data
    dates = re.findall(pattern, data)

    # Remove leading empty message if it exists
    if messages[0] == "":
        messages = messages[1:]


    # Parse dates directly inside the preprocess function
    parsed_dates = []
    for date_str in dates:
        try:
            parsed_date = pd.to_datetime(date_str, format='%d/%m/%y, %I:%M %p - ')
        except ValueError:
            try:
                parsed_date = pd.to_datetime(date_str, format='%d/%m/%y, %H:%M - ')
            except ValueError:
                parsed_date = pd.NaT  # Assign Not a Time for unparseable dates
        parsed_dates.append(parsed_date)

    # Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'date': parsed_dates})

    # Extract users and messages
    users = []
    msgs = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if len(entry) > 2:  # Check if there are user name and message
            users.append(entry[1])
            msgs.append(entry[2])
        else:  # It's a group notification
            users.append('group_notification')
            msgs.append(entry[0])

    df['user'] = users
    df['message'] = msgs

    # Drop the 'user_message' column as it's no longer needed
    df.drop(columns=['user_message'], inplace=True)

    # # Filter out messages with "Media omitted"
    # df = df[~df['message'].str.contains('Media omitted')]

    # Extract additional datetime features
    df['only_date'] = df['date'].dt.date #Daily Timeline
    df['year'] = df['date'].dt.year.astype(str)  # Convert year to string to prevent formatting issues
    df['month_num'] = df['date'].dt.month #Timeline(monthly)
    df['month'] = df['date'].dt.month_name()
    df['day_name'] = df['date'].dt.day_name() #activity on days
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute


    # For Heatmap
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    
    df['period'] = period
    
    return df
