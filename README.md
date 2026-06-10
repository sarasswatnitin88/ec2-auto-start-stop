# ec2-auto-start-stop
Automated EC2 management using Lambda + EventBridge
# EC2 Auto Start/Stop — AWS Lambda Automation

## Overview
Tag-based EC2 instance automation using AWS Lambda, 
EventBridge, and Boto3 (Python).

## Architecture
EventBridge Cron → Lambda → EC2 (Tag Filter)

## AWS Services Used
- AWS Lambda (Python 3.x)
- Amazon EventBridge (Cron Scheduler)
- Amazon EC2
- AWS IAM (Role-based Access)

## How It Works
### Auto Stop
- Scans all running EC2 instances
- Skips instances with tag: shutdown = false
- Stops all remaining instances

### Auto Start
- Finds stopped EC2 instances by tag: Name = se45rver
- Starts them automatically on schedule

## IAM Permissions Required
- ec2:DescribeInstances
- ec2:StartInstances
- ec2:StopInstances

## Author
Nitin Saraswat (Denny)  
AWS Certified Solutions Architect – Associate  
nitinsaraswat.com
