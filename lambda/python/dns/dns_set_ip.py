import boto3, json
def lambda_handler(event, context):
    HOSTED_ZONE_ID = 'Z0483785363LZ0HONVZGW'
    route53 = boto3.client('route53')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("table-ip-cortijo")
    ip =  event["requestContext"]["identity"]["sourceIp"]
    table.put_item(Item={'Place': 'cortijo', 'Ip': ip})
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
