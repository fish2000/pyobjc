# This file is generated by objective.metadata
#
# Last update: Mon Mar 18 09:12:16 2013

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$SKErrorDomain$'''
enums = '''$SKDownloadStateActive@1$SKDownloadStateCancelled@5$SKDownloadStateFailed@4$SKDownloadStateFinished@3$SKDownloadStatePaused@2$SKDownloadStateWaiting@0$SKErrorClientInvalid@1$SKErrorPaymentCancelled@2$SKErrorPaymentInvalid@3$SKErrorPaymentNotAllowed@4$SKErrorUnknown@0$SKPaymentTransactionStateFailed@2$SKPaymentTransactionStatePurchased@1$SKPaymentTransactionStatePurchasing@0$SKPaymentTransactionStateRestored@3$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'SKPaymentQueue', b'canMakePayments', {'retval': {'type': b'Z'}})
    r(b'SKProduct', b'downloadable', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'paymentQueue:removedTransactions:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'paymentQueue:restoreCompletedTransactionsFailedWithError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'paymentQueue:updatedDownloads:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'paymentQueue:updatedTransactions:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'paymentQueueRestoreCompletedTransactionsFinished:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'productsRequest:didReceiveResponse:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'request:didFailWithError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'requestDidFinish:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
