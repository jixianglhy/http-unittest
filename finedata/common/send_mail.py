from datetime import timedelta
from exchangelib import DELEGATE,IMPERSONATION,Account,Credentials,ServiceAccount
from exchangelib import EWSDateTime,EWSTimeZone,Configuration,NTLM,CalendarItem,Message
from exchangelib import Mailbox,Attendee,Q,ExtendedProperty,FileAttachment,ItemAttachment
from exchangelib import HTMLBody, Build,Version

credentials = Credentials(username='lihaiying@le.com',password='letv.2222')
config = Configuration(server='mail.le.com',credentials=credentials)
account = Account(primary_smtp_address='lihaiying@le.com',config = config,autodiscover=False,access_type=DELEGATE)
'''
for item in account.inbox.all().order_by('-datetime_received')[:5]:
      #print(item.subject, item.body,item.attachments)
      print(item.subject)
'''
subject = 'finedata'
m = Message(account=account, subject='hello1',to_recipients=[Mailbox(email_address='jixianglhy@126.com'),Mailbox(email_address='lihaiying@le.com')])
m.send()
