import ssl
import xml.etree.ElementTree as ET
import smtplib
import sys
import logging
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def createEmail(fileName):
      try:
            #Dictionary created for xml namespace values
            ns = {'real_tag': 'http://www.w3.org/2005/02/xpath-functions',
            'evt': 'http://www.portauthoritytech.com/schmea/event/1.0'}

            #reading xml file in memory
            oXMLTree = ET.parse(str(fileName))
            root = oXMLTree.getroot()

            #populate values with xml data
            evtId = root.find('.//evt:eventId',ns)
            evtIncidentId = root.find('.//evt:incidentId',ns)
            evtSource = root.find('.//evt:source',ns)
            evtDate = root.find('.//evt:insert_date',ns)
            evtDest = root.find('.//evt:destinationList',ns)

            evtUserName = root.find('.//evt:username',ns)
            evtFullName = root.find('.//evt:commonName',ns)
            evtUserEmail = "EMAIL_TO"#root.find('.//evt:email',ns)
            senderEmail = "EMAIL_FROM"

            #applying values to email properties
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "EMAIL SUBJECT"
            msg['From'] = senderEmail
            msg['To'] = evtUserEmail

            logging.info('Email Values captured')


      ## the email message that would be sent to the user

            message = "Dear " + evtFullName.text + ", \n\nThis is " + evtIncidentId.text + ","
            message += " from REDACTED."
            message += " We have had some notifications from our REDACTED"
            message += "that there may be sensitive data being transferred or stored on your system.\n\n"
            message += "As part of REDACTED data loss prevention program,"
            message += "an automated scan discovered that on "
            message += evtDate.text + " you attempted "
            message += "and successfully sent files to " + evtDest.text + "."
            message += "This action is not in compliance with REDACTED"
            message += "for handling sensitive data. Please review the following details"
            message += "details and perform any applicable action:"
            message += "\n\n\n"
            message += "Thank you for your prompt attention to this issue."
            message += "\n"
            message += "REDACTED\n\n"

            #sets conversion of text for email
            htmlMsg = MIMEText(message,'plain')

            #adding message body to email object
            msg.attach(htmlMsg)
            logging.info('Email packed')

            #Send email
            #SMTPGATEWAY='IP_ADDRESS'
 	        ## send an email message
            #oSMTP=smtplib.SMTP(SMTPGATEWAY)
            #oSMTP.sendmail(senderEmail,evtUserEmail,msg.as_string())
            print(msg)
            logging.info('Email Sent')
            #oSMTP=None
      except Exception as err:
            logging.error(f"Unexpected {err=},{type(err)=}")

if __name__ == "__main__":

      logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',filename='notify.log', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
      #fileName = sys.argv[1]
      fileName = 'event.xml'
      
      logging.info('Script Initialized')
      email = createEmail(fileName)
      logging.info('Finished')
