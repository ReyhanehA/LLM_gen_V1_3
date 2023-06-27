#10.# Example 10: CWE-916 - Use of Hard-coded Slack API Token
slack_api_token = "xoxp-1234567890" # vulnerable line
# This code is vulnerable to CWE-916 as it uses a hard-coded Slack API token which can be easily guessed or exploited by attackers.