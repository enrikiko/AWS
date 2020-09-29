import boto3, json
HOSTED_ZONE_ID = 'HOSTED_ZONE_ID'
def lambda_handler(event, context):
    route53 = boto3.client('route53')
    ip =  event["ip"]
    dns_changes = {
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "app.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "jenkins.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "public.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "back.app.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "camera1.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "camera2.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "camera.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "socket.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "file.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "vpn.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "dockerhub.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "couchbase.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "router.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "www.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "gitlab.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "octopi.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "ws.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "haproxy.cortijodemazas.com.",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            }
        ]
    }

    response = route53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch=dns_changes
    )

    return {
            'statusCode': 201,
            'body': ip
        }
