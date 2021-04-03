# Return full name given first and last
def lambda_handler(event, context):
	return {
		'statusCode': 200,
		'output': event.get('first_name') + ' ' + event.get('last_name')
	}
