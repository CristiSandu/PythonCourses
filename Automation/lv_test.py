from twilio.rest import Client 
 
account_sid = 'ACc2b4a9e2424181ebeb111724bfe5646f' 
auth_token = 'd49f3a573125258eef4ff9a8cbff7aff' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment isfdddddddddddddddddds coming up on July 21 at 3PM',      
                              to='whatsapp:+40775592486' 
                          ) 
 
print(message.sid)
