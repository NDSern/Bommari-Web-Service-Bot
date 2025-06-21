# Bommari climbing route website

At: [https://bommari.vraminhos.com](https://bommari.vraminhos.com)

This project pull climbing routes made by club member of Tekilla in a Telegram channel and upload it to the website for a better viewing experience.

## Prerequisites

Make sure you have installed the following on your system:
- [Node.js](https://nodejs.org) (20.18.3 or later)
- [Python](https://python.org) (3.13.2 or later)

## Installation

- In *Telegram Bot* folder:
    - [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
    - [dotenv](https://pypi.org/project/dotenv/)
    - [aiohttp](https://pypi.org/project/aiohttp/)
    ```
    pip install pyTelegramBotAPI dotenv aiohttp
    ```

- In *API* folder:
    ```
    npm install
    ```

- In *Web App* folder:
    ```
    cd bommari_webapp
    npm install
    ```

## API Endpoints
- `GET /routes` - Fetch all routes