import poplib
import argparse
import re

def clearEmail(email,pwd):
  mailSer = re.match(r"[a-zA-Z\.]+@([\w\.]+)",email).group(1)
  mailbox=poplib.POP3(f"mail.{mailSer}",110)
  mailbox.user(email)
  mailbox.pass_(pwd)
  mails=mailbox.stat()[0]
  for i in range(mails):
      mailbox.dele(i+1)
  mailbox.quit()