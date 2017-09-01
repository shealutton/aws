This lambda function monitors an S3 bucket for Put events. It then fires, opens the new object from S3, parses it for root account login events, and if found, sends an email to SNS. 

Shea Lutton, Matt Harvey, Andres from P&G.