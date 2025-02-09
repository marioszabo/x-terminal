# Terminal Tweet Poster

A simple command-line tool to post tweets directly from your terminal using Python and the Twitter API v2.

## Features

- Post tweets from any terminal
- OAuth 1.0a authentication
- Clean and simple interface
- Error handling and validation
- Character limit checking

## Prerequisites

- Python 3.x
- A Twitter Developer Account
- Twitter API Keys and Tokens

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tweet.git
cd tweet
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install tweepy python-dotenv
```

### 4. Set Up Twitter Developer Account

1. Go to [Twitter Developer Portal](https://developer.x.com/portal/dashboard)
2. Create a new Project and App
3. In App Settings > User authentication settings:
   - Enable OAuth 1.0a
   - Set App permissions to "Read and write"
   - Set Type of App to "Native App"
   - Set Website URL to "https://twitter.com"
   - Set Callback URI to "http://127.0.0.1"

### 5. Configure Environment Variables

Create a `.env` file in the project directory:

```env
API_KEY="your_api_key"
API_KEY_SECRET="your_api_key_secret"
ACCESS_TOKEN="your_access_token"
ACCESS_TOKEN_SECRET="your_access_token_secret"
```

Replace the placeholder values with your Twitter API credentials from the Developer Portal.

### 6. Make the Script Accessible System-wide

```bash
# Create bin directory if it doesn't exist
mkdir -p ~/bin

# Create symbolic links
ln -s "/path/to/your/tweet_wrapper.sh" ~/bin/tweet

# Make scripts executable
chmod +x tweet_wrapper.sh
chmod +x tweet.py
```

Add this to your `~/.zshrc` or `~/.bashrc`:
```bash
export PATH="$HOME/bin:$PATH"
```

Then reload your shell:
```bash
source ~/.zshrc  # or source ~/.bashrc
```

## Usage

Post a tweet:
```bash
tweet "Your message here"
```

The script will:
1. Authenticate with your Twitter account
2. Post your message
3. Show the URL to view your tweet

## Error Handling

The script will show clear error messages for:
- Authentication failures
- Missing credentials
- Messages exceeding 280 characters
- API errors

## File Structure

```
.
├── README.md
├── tweet.py              # Main Python script
├── tweet_wrapper.sh      # Shell wrapper script
├── .env                 # Environment variables (not tracked in git)
└── .gitignore           # Git ignore file
```

## Security Notes

- Never commit your `.env` file to version control
- Keep your API keys and tokens secure
- Regenerate tokens if they're ever exposed

## Troubleshooting

1. **Command not found**: Make sure `~/bin` is in your PATH
2. **Authentication failed**: Verify your API credentials in `.env`
3. **Module not found**: Ensure you're in the virtual environment
4. **Permission denied**: Check file permissions for the scripts

## Contributing

Feel free to:
- Report issues
- Submit pull requests
- Suggest improvements

## License

MIT License - feel free to use and modify as you like! # x-terminal
