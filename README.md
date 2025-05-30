# Simple Discord Economy Bot

This is a basic Discord economy bot built using discord.py. It allows users to check their balance, deposit and withdraw money, and send money to other users.

## Features

*   **Balance:** Check your wallet and bank balance.
*   **Deposit:** Deposit money from your wallet into your bank.
*   **Withdraw:** Withdraw money from your bank into your wallet.
*   **Send:** Send money to other users.

## Prerequisites

*   Python 3.6 or higher
*   discord.py library
*   A Discord bot token

## Setup

1.  **Install Dependencies:**

    ```bash
    pip install discord.py
    ```

2.  **Configure the Bot:**

    *   Replace `"YOUR_BOT_TOKEN"` in the `main.py` file with your actual Discord bot token.

3.  **Run the Bot:**

    ```bash
    python main.py
    ```

## Commands

*   `!balance [user]`: Check your own or another user's balance.
*   `!deposit <amount>`: Deposit money into your bank. Use `!deposit all` to deposit all money from your wallet.
*   `!withdraw <amount>`: Withdraw money from your bank. Use `!withdraw all` to withdraw all money from your bank.
*   `!send <user> <amount>`: Send money to another user.

## Important Notes

*   **Data Storage:** The bot uses a `mainbank.json` file to store user data. This file is created automatically if it doesn't exist.
*   **Error Handling:** The bot includes basic error handling, but more robust error handling is recommended for a production bot.
*   **Security:** Be careful when handling user input and ensure that the bot is secure to prevent abuse.

## Contributing

Contributions are welcome! Feel free to submit pull requests with bug fixes, new features, or improvements to the documentation.
