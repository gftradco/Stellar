from stellar_base.builder import Builder
import csv
from array import *

sender_secret = 'SBIQIV2XQBBVXK7FFNNRDTTKG2YTQI5GI4DNY75SDCP2IBMQ2NFZNQNS'

receiver_address = []
with open('assetHoldersExport(testnet).csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        receiver_address.append(line[1])


# Start Address Count
filename = "assetHoldersExport(testnet).csv"
a = 300
numLines = -1
#numWords = 0
#numChars = 0
#blockReward = 5000

with open(filename, 'r') as file:
    for line in file:
        #create a list for words
        wordsList = line.split( )
        numLines += 1

# End Address Count


for i in range(len(receiver_address)):


    builder = Builder(secret=sender_secret, horizon_uri='https://horizon-testnet.stellar.org', network='TESTNET')
    builder.add_text_memo("Thank you for using TXBNB!").append_payment_op(
        destination=receiver_address[i],
        amount=str(a / int("%i" % (numLines))),
        asset_code='TXBNB',
        asset_issuer='GDHAFLI6STAHO2GPJEG56CEWRC5QNT54QNWIPREHI4NXJHANSKOGDDTI'
    )
    builder.sign()
    response = builder.submit()
    print(response)

