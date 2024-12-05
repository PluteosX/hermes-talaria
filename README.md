# Welcome to hermes-talaria 👋
![Version](https://img.shields.io/badge/version-1.1.0-blue.svg?cacheSeconds=2592000)

> Hermes Talaria is a project designed to track and notify users about their cryptocurrency investments, specifically when their investment value surpasses a pre-defined threshold. It retrieves investment data from a Google Sheet and integrates with the GeckoTerminal API to provide real-time notifications via Telegram when significant changes occur in the user's portfolio.

## Key Features
1. **Investment Tracking**  
   Tracks the investments made by users and monitors their price movements in real-time.
   
2. **Threshold Notifications**  
   Sends automated notifications via **Telegram** when the value of a user’s investment surpasses a pre-defined threshold, helping users stay up-to-date on their portfolio performance.
   
3. **Real-Time Data**  
   Retrieves the latest data on cryptocurrency prices and market trends using the **GeckoTerminal API**, ensuring that users are always informed with up-to-date information.

4. **Google Sheets Integration**  
   Fetches user investment data directly from a **Google Sheet** using a simple CSV API integration. The data is retrieved dynamically, allowing real-time updates for the user's investments.

## Automated Notifications
The project sends real-time notifications to a **Telegram** group or individual chat using the `requests` library, alerting users when their investment surpasses a set threshold. Notifications are automated, making the process seamless and efficient for users.

## Techniques and Technologies Used
- **GeckoTerminal API**: Integrated with the `requests` library to retrieve real-time market data and investment prices.
- **Google Sheets**: Data is fetched dynamically from a Google Sheet using a CSV API integration. This allows for easy tracking of investments.
- **Telegram Notifications**: Sent via the `requests` library to ensure smooth integration and real-time alerts.
- **Python**: The primary language for the business logic and API interaction.

## Purpose
The project helps users monitor and manage their cryptocurrency investments more efficiently, providing timely alerts when their investments experience significant changes. It empowers users to make informed decisions based on real-time data.

## Inspiration
The name *Hermes-talaria* is inspired by the winged sandals of the Greek god Hermes, symbolizing swift communication and the ability to instantly notify users about crucial changes in their investments.

## Author

👤 **Beatriz Ruiz Casanova**

* Github: [@bruizk](https://github.com/bruizk)
* LinkedIn: [@beatriz-ruiz-casanova](https://www.linkedin.com/in/beatriz-ruiz-casanova/)

