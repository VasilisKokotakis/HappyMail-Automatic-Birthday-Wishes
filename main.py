import pandas as pd
import datetime as dt
import random
import smtplib

# Get today's month and day
now = dt.datetime.now()
today = (now.month, now.day)

# Read birthdays data
data = pd.read_csv("birthdays.csv")

# Create a dictionary with (month, day) as keys for quick lookup
birthdays_dict = {(row["month"], row["day"]): row for _, row in data.iterrows()}

# Check if today matches any birthday
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]

    # Select a random letter template
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Email credentials
    my_email = "YOUR_EMAIL"
    password = "YOUR_PASSWORD" 

    # Send email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
