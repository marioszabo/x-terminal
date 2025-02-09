#!/usr/bin/env python3

import os
import sys
import tweepy
from dotenv import load_dotenv

def debug_permissions():
    """Debug OAuth settings and permissions."""
    print("\nChecking credentials...")
    
    # Force reload environment variables
    os.environ.clear()
    load_dotenv(override=True)
    
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    
    if not all([api_key, api_secret, access_token, access_token_secret]):
        print("✗ Missing credentials in .env file")
        return False
    return True

def verify_app_permissions(client):
    """Verify that the app has the correct permissions."""
    try:
        # Get user information
        me = client.get_me(user_fields=['username', 'name'])
        print(f"✓ Authenticated as @{me.data.username}")
        return True
        
    except tweepy.errors.Unauthorized as e:
        print("\n✗ Authentication failed.")
        print("Please check your Twitter App settings and credentials.")
        if not debug_permissions():
            print("✗ Some credentials are missing. Please check your .env file.")
        return False
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        return False

def setup_twitter_api():
    """Set up and return Twitter API v2 client."""
    load_dotenv()
    
    # Get credentials from environment variables
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    
    # Verify credentials are loaded
    if not all([api_key, api_secret, access_token, access_token_secret]):
        print("\n✗ Missing credentials in .env file")
        sys.exit(1)
    
    try:
        # Create client with OAuth 1.0a User Context
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True
        )
        
        # Verify app permissions
        if not verify_app_permissions(client):
            sys.exit(1)
            
        return client
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        sys.exit(1)

def post_tweet(message):
    """Post a tweet with the given message using API v2."""
    try:
        client = setup_twitter_api()
        tweet = client.create_tweet(text=message)
        print(f"\nYour post: {message}")
        print(f"View at: https://x.com/i/status/{tweet.data['id']}")
        return True
    except tweepy.errors.Unauthorized:
        print("\n✗ Authentication failed. Please check your credentials.")
        return False
    except Exception as e:
        print(f"\n✗ Error posting tweet: {str(e)}")
        return False

def main():
    # Check if a message was provided
    if len(sys.argv) < 2:
        print("Usage: tweet 'Your message'")
        sys.exit(1)
    
    # Get the tweet message from command line arguments
    message = ' '.join(sys.argv[1:])
    
    # Check tweet length
    if len(message) > 280:
        print("✗ Error: Message exceeds 280 characters")
        sys.exit(1)
    
    # Post the tweet
    post_tweet(message)

if __name__ == "__main__":
    main() 