# SNS Simple Notification Service

    Simple Notification Service is used so you publish to one place and setup actions behind it like email or callouts etc
    
## Examples

    ### Publish Example
    
        import boto3

        # Initialize the SNS client
        sns_client = boto3.client("sns")

        # Replace with your SNS Topic ARN
        sns_topic_arn = "arn:aws:sns:your-region:your-account-id:your-topic-name"

        # Define the message
        message = "Test alert message, no action needed"

        # Publish the message
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject="Test Notification"
        )

        # Print response metadata
        print("Message sent! MessageId:", response["MessageId"])
