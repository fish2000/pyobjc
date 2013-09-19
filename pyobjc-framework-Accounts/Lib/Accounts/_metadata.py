# This file is generated by objective.metadata
#
# Last update: Thu May 23 15:51:55 2013

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
constants = '''$ACAccountStoreDidChangeNotification$ACAccountTypeIdentifierFacebook$ACAccountTypeIdentifierSinaWeibo$ACAccountTypeIdentifierTwitter$ACErrorDomain$ACFacebookAppIdKey$ACFacebookAppVersionKey$ACFacebookPermissionGroupKey$ACFacebookPermissionGroupRead$ACFacebookPermissionGroupReadWrite$ACFacebookPermissionGroupWrite$ACFacebookPermissionsKey$'''
enums = '''$ACAccountCredentialRenewResultFailed@2$ACAccountCredentialRenewResultRejected@1$ACAccountCredentialRenewResultRenewed@0$ACErrorAccessInfoInvalid@8$ACErrorAccountAlreadyExists@5$ACErrorAccountAuthenticationFailed@3$ACErrorAccountMissingRequiredProperty@2$ACErrorAccountNotFound@6$ACErrorAccountTypeInvalid@4$ACErrorPermissionDenied@7$ACErrorUnknown@1$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'ACAccountStore', b'removeAccount:withCompletionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}}}})
    r(b'ACAccountStore', b'renewCredentialsForAccount:completion:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': sel32or64(b'i', b'q')}, 2: {'type': b'@'}}}}}})
    r(b'ACAccountStore', b'requestAccessToAccountsWithType:options:completion:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}}}})
    r(b'ACAccountStore', b'requestAccessToAccountsWithType:withCompletionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}}}})
    r(b'ACAccountStore', b'saveAccount:withCompletionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}}}})
    r(b'ACAccountType', b'accessGranted', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
