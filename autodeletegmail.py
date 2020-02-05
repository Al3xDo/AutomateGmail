import imapclient,os,imaplib
print('THE SOFT WILL USE THE FILE IN THE DIRECTORY '+ os.getcwd())
print('ONLY USE WITH GMAIL')
imaplib._MAXLINE = 10000000/2
imapObj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
# xử lý tài khoản
print('Your name account:')
name=input()
print('password:')
mypass=input()
imapObj.login(name,mypass)
print('if u see imaplib.error: got more than 10000 bytes then restart the soft')
print('Add the name of the labels (remember to cappitalized)')
print("""
ex: 
INBOX
DARFT
SENT
TRASH
""")
label=input()
label=label.capitalize()
imapObj.select_folder(label,readonly=False)
while True:
    print("""1. Deleting gmail by the date""")
    print('2. Deleting gmail by the email senders:')
    print('3. Deleting gmail by the key word:')
    print('Enter to quit')
    x=input()
    if x=='1':
        print('Add the date you want to delete mess ( The date must be formatted like 05-Jul-2015):')
        date=input()
        date='ON '+date
        UIDs=imapObj.search(date)
        imapObj.delete_messages(UIDs)
        print('Done')
    elif x=='2':
        print("""
        2. Deleting gmail by the email senders 
        Choose keyword:
        + FROM
        + NOT FROM
        + TO
        """)
        kword=input()
        print('Type the email sender you want to delete')
        email=list(map(str,input().strip().split()))
        for i in range(0,len(email)+1):
            emailde='kword '+email[i]
            UID=imapObj.search(email[i])
            imapObj.delete_messages(UID)
        print('Done')
    elif x=='3':
        print("""
        4. Deleting gmail by the key word:
        + ANSWERED
        + UNANSWERED
        + SEEN
        + UNSEEN
        + FLAGGED
        + UNFLAGGED
        """)
        kword=input()
        UIDs=imapObj.search(kword)
        imapObj.delete_messages(UIDs)
        print('Done')
    elif x=='':
        break
imapObj.logout()
print('Exited')
