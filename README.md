# XurTracker.com

[![XurTracker.com](https://img.shields.io/website-up-down-green-red/https/www.xurtracker.com.svg)](https://www.xurtracker.com)

XurTracker.com is a comprehensive service that provides Destiny 2 players with real-time information on Xur's location and inventory. This repository contains the source code for the [XurTracker](https://www.xurtracker.com) website, Twitter bot, and API.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)


## Overview

This project powers the XurTracker.com website, a Twitter bot that tweets Xur's current location and inventory every weekend, and a public API that allows developers to access Xur's data programmatically.

## Features

- **Website**: A user-friendly interface for viewing Xur's current location, inventory, and historical data.
- **Twitter Bot**: Automatically tweets updates about Xur's location and inventory as soon as the information becomes available.
- **API**: Provides developers with programmatic access to Xur's data, enabling integration with other applications or tools.
- **Data Collection**: Aggregates data from various sources to provide the most accurate and up-to-date information.

## API Documentation

The XurTracker API allows developers to fetch real-time and historical data about Xur's location and inventory.

### API URL

```
https://api.xurtracker.com/api
```

### Endpoints
- **GET `/get-legendary-weapons`**: Retrieve legendary weapons for sale.
- **GET `/get-armor?class=<class_str>`**: Retrieve armor for sale for the specified class.
- **GET `/get-dates`**: Retrieve Xur's arrival and departure dates.
- **GET `/get-location`**: Retrieve Xur's current location.

### Example Request

```bash
curl https://api.xurtracker.com/api/get-location
```

### Example Response

```json
{
  "LandingZone": "Bazaar, The Tower",
  "Location": "The Last City",
  "Planet": "Earth"
}
```



## Contributing

We welcome contributions from the community! If you have suggestions, bug reports, or improvements, feel free to open an issue or submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Your commit message'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
