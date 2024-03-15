import streamlit as st
import datetime
from twilio.rest import Client as TwilioClient

# Twilio credentials (replace these with your own)
TWILIO_SID = 'AC6048c38b57662163c389bcd6f0cd6e2b'
TWILIO_AUTH_TOKEN = '98693e4ec2c79f75c09dfa3ef0698be2'
TWILIO_PHONE_NUMBER = '+13212030357'

# Function to send SMS using Twilio
def send_sms(to, body):
    client = TwilioClient(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )

# Function to calculate meal times based on user input
def calculate_meal_time(breakfast_hour, breakfast_minute, lunch_hour, lunch_minute, dinner_hour, dinner_minute):
    breakfast_time = datetime.time(breakfast_hour, breakfast_minute)
    lunch_time = datetime.time(lunch_hour, lunch_minute)
    dinner_time = datetime.time(dinner_hour, dinner_minute)
    return breakfast_time, lunch_time, dinner_time

# Streamlit app
def main():
    st.title("Meal Time SMS Notifier")
    
    st.write("Enter meal times (24-hour format):")
    breakfast_hour = st.slider("Breakfast Hour", 0, 23, 7)
    breakfast_minute = st.slider("Breakfast Minute", 0, 59, 0)
    lunch_hour = st.slider("Lunch Hour", 0, 23, 12)
    lunch_minute = st.slider("Lunch Minute", 0, 59, 30)
    dinner_hour = st.slider("Dinner Hour", 0, 23, 18)
    dinner_minute = st.slider("Dinner Minute", 0, 59, 0)

    breakfast_time, lunch_time, dinner_time = calculate_meal_time(breakfast_hour, breakfast_minute, lunch_hour, lunch_minute, dinner_hour, dinner_minute)

    st.write(f"Breakfast Time: {breakfast_time}")
    st.write(f"Lunch Time: {lunch_time}")
    st.write(f"Dinner Time: {dinner_time}")

    
    phone_number = st.text_input("Enter your phone number (with country code, e.g., +1234567890):")

    if st.button("Send SMS Notifications"):
        if phone_number:
            send_sms(phone_number, f"It's time for breakfast at {breakfast_time}, lunch at {lunch_time}, and dinner at {dinner_time}")
            st.success("SMS notifications sent successfully!")
        else:
            st.error("Please enter a valid phone number.")

    # # Continuously check the time and send SMS notifications
    # while True:
    #     current_time = datetime.datetime.now().time()
    #     if current_time == breakfast_time:
    #         if phone_number:
    #             send_sms(phone_number, "It's time for breakfast!")
    #     elif current_time == lunch_time:
    #         if phone_number:
    #             send_sms(phone_number, "It's time for lunch!")
    #     elif current_time == dinner_time:
    #         if phone_number:
    #             send_sms(phone_number, "It's time for dinner!")

    #     # Check every minute
    #     time.sleep(60)

if __name__ == "__main__":
    main()
