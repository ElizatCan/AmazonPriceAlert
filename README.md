# AmazonPriceAlert
This code sends an email notification when the price of a product on Amazon falls below amount that you decide . It uses web scraping techniques to retrieve the price and product name from the Amazon website and the smtplib library to send the email.

This code is a Python script that sends an email notification if the price of a product on Amazon drops below a certain threshold. To use it, the user would need to replace the URL in the url variable with the Amazon product URL they are interested in tracking. They would also need to replace the email-related variables (smtp_username, smtp_password, sender_email, and recipient_email) with their own email account information. Finally, they would need to adjust the price_as_float comparison value in the if statement to the desired price threshold. Once the script is set up with the user's information, they can run it to receive email alerts whenever the price of their desired product drops below the specified threshold.



