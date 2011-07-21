# Generated file, don't edit
# Source: BridgeSupport/CFOpenDirectory.bridgesupport
# Last update: Thu Jul 21 08:51:05 2011

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
    "ODContextRef": objc.createOpaquePointerType('ODContextRef', b'^{_ODContext=}'),
    "ODNodeRef": objc.createOpaquePointerType('ODNodeRef', b'^{_ODNode=}'),
    "ODQueryRef": objc.createOpaquePointerType('ODQueryRef', b'^{_ODQuery=}'),
    "ODRecordRef": objc.createOpaquePointerType('ODRecordRef', b'^{_ODRecord=}'),
    "ODSessionRef": objc.createOpaquePointerType('ODSessionRef', b'^{_ODSessionRef=}'),
}
constants = '''$kODAttributeTypeAccessControlEntry@^{__CFString=}$kODAttributeTypeAddressLine1@^{__CFString=}$kODAttributeTypeAddressLine2@^{__CFString=}$kODAttributeTypeAddressLine3@^{__CFString=}$kODAttributeTypeAdminLimits@^{__CFString=}$kODAttributeTypeAlias@^{__CFString=}$kODAttributeTypeAllAttributes@^{__CFString=}$kODAttributeTypeAllTypes@^{__CFString=}$kODAttributeTypeAreaCode@^{__CFString=}$kODAttributeTypeAttrListRefCount@^{__CFString=}$kODAttributeTypeAttrListRefs@^{__CFString=}$kODAttributeTypeAttrListValueRefCount@^{__CFString=}$kODAttributeTypeAttrListValueRefs@^{__CFString=}$kODAttributeTypeAuthCredential@^{__CFString=}$kODAttributeTypeAuthMethod@^{__CFString=}$kODAttributeTypeAuthenticationAuthority@^{__CFString=}$kODAttributeTypeAuthenticationHint@^{__CFString=}$kODAttributeTypeAuthorityRevocationList@^{__CFString=}$kODAttributeTypeAutomaticSearchPath@^{__CFString=}$kODAttributeTypeAutomountInformation@^{__CFString=}$kODAttributeTypeBirthday@^{__CFString=}$kODAttributeTypeBootParams@^{__CFString=}$kODAttributeTypeBuildVersion@^{__CFString=}$kODAttributeTypeBuilding@^{__CFString=}$kODAttributeTypeCACertificate@^{__CFString=}$kODAttributeTypeCapacity@^{__CFString=}$kODAttributeTypeCertificateRevocationList@^{__CFString=}$kODAttributeTypeCity@^{__CFString=}$kODAttributeTypeComment@^{__CFString=}$kODAttributeTypeCompany@^{__CFString=}$kODAttributeTypeComputers@^{__CFString=}$kODAttributeTypeConfigAvailable@^{__CFString=}$kODAttributeTypeConfigFile@^{__CFString=}$kODAttributeTypeContactGUID@^{__CFString=}$kODAttributeTypeContactPerson@^{__CFString=}$kODAttributeTypeCopyTimestamp@^{__CFString=}$kODAttributeTypeCoreFWVersion@^{__CFString=}$kODAttributeTypeCountry@^{__CFString=}$kODAttributeTypeCreationTimestamp@^{__CFString=}$kODAttributeTypeCrossCertificatePair@^{__CFString=}$kODAttributeTypeCustomSearchPath@^{__CFString=}$kODAttributeTypeDNSDomain@^{__CFString=}$kODAttributeTypeDNSName@^{__CFString=}$kODAttributeTypeDNSNameServer@^{__CFString=}$kODAttributeTypeDataStamp@^{__CFString=}$kODAttributeTypeDateRecordCreated@^{__CFString=}$kODAttributeTypeDepartment@^{__CFString=}$kODAttributeTypeDirRefCount@^{__CFString=}$kODAttributeTypeDirRefs@^{__CFString=}$kODAttributeTypeEMailAddress@^{__CFString=}$kODAttributeTypeEMailContacts@^{__CFString=}$kODAttributeTypeENetAddress@^{__CFString=}$kODAttributeTypeExpire@^{__CFString=}$kODAttributeTypeFWVersion@^{__CFString=}$kODAttributeTypeFaxNumber@^{__CFString=}$kODAttributeTypeFirstName@^{__CFString=}$kODAttributeTypeFullName@^{__CFString=}$kODAttributeTypeFunctionalState@^{__CFString=}$kODAttributeTypeGUID@^{__CFString=}$kODAttributeTypeGroup@^{__CFString=}$kODAttributeTypeGroupMembers@^{__CFString=}$kODAttributeTypeGroupMembership@^{__CFString=}$kODAttributeTypeGroupServices@^{__CFString=}$kODAttributeTypeHTML@^{__CFString=}$kODAttributeTypeHomeDirectory@^{__CFString=}$kODAttributeTypeHomeDirectoryQuota@^{__CFString=}$kODAttributeTypeHomeDirectorySoftQuota@^{__CFString=}$kODAttributeTypeHomeLocOwner@^{__CFString=}$kODAttributeTypeHomePhoneNumber@^{__CFString=}$kODAttributeTypeIMHandle@^{__CFString=}$kODAttributeTypeIPAddress@^{__CFString=}$kODAttributeTypeIPAddressAndENetAddress@^{__CFString=}$kODAttributeTypeIPv6Address@^{__CFString=}$kODAttributeTypeInternetAlias@^{__CFString=}$kODAttributeTypeJPEGPhoto@^{__CFString=}$kODAttributeTypeJobTitle@^{__CFString=}$kODAttributeTypeKDCAuthKey@^{__CFString=}$kODAttributeTypeKDCConfigData@^{__CFString=}$kODAttributeTypeKerberosRealm@^{__CFString=}$kODAttributeTypeKeywords@^{__CFString=}$kODAttributeTypeLDAPReadReplicas@^{__CFString=}$kODAttributeTypeLDAPSearchBaseSuffix@^{__CFString=}$kODAttributeTypeLDAPWriteReplicas@^{__CFString=}$kODAttributeTypeLastName@^{__CFString=}$kODAttributeTypeLocalOnlySearchPath@^{__CFString=}$kODAttributeTypeLocation@^{__CFString=}$kODAttributeTypeMCXFlags@^{__CFString=}$kODAttributeTypeMCXSettings@^{__CFString=}$kODAttributeTypeMIME@^{__CFString=}$kODAttributeTypeMailAttribute@^{__CFString=}$kODAttributeTypeMapCoordinates@^{__CFString=}$kODAttributeTypeMapGUID@^{__CFString=}$kODAttributeTypeMapURI@^{__CFString=}$kODAttributeTypeMetaAutomountMap@^{__CFString=}$kODAttributeTypeMetaNodeLocation@^{__CFString=}$kODAttributeTypeMiddleName@^{__CFString=}$kODAttributeTypeMobileNumber@^{__CFString=}$kODAttributeTypeModificationTimestamp@^{__CFString=}$kODAttributeTypeNFSHomeDirectory@^{__CFString=}$kODAttributeTypeNTDomainComputerAccount@^{__CFString=}$kODAttributeTypeNamePrefix@^{__CFString=}$kODAttributeTypeNameSuffix@^{__CFString=}$kODAttributeTypeNativeOnly@^{__CFString=}$kODAttributeTypeNestedGroups@^{__CFString=}$kODAttributeTypeNetGroupTriplet@^{__CFString=}$kODAttributeTypeNetGroups@^{__CFString=}$kODAttributeTypeNetworkNumber@^{__CFString=}$kODAttributeTypeNickName@^{__CFString=}$kODAttributeTypeNodePath@^{__CFString=}$kODAttributeTypeNodeRefCount@^{__CFString=}$kODAttributeTypeNodeRefs@^{__CFString=}$kODAttributeTypeNote@^{__CFString=}$kODAttributeTypeNumTableList@^{__CFString=}$kODAttributeTypeOrganizationInfo@^{__CFString=}$kODAttributeTypeOrganizationName@^{__CFString=}$kODAttributeTypeOriginalHomeDirectory@^{__CFString=}$kODAttributeTypeOriginalNFSHomeDirectory@^{__CFString=}$kODAttributeTypeOriginalNodeName@^{__CFString=}$kODAttributeTypeOwner@^{__CFString=}$kODAttributeTypeOwnerGUID@^{__CFString=}$kODAttributeTypePGPPublicKey@^{__CFString=}$kODAttributeTypePIDValue@^{__CFString=}$kODAttributeTypePagerNumber@^{__CFString=}$kODAttributeTypePassword@^{__CFString=}$kODAttributeTypePasswordPlus@^{__CFString=}$kODAttributeTypePasswordPolicyOptions@^{__CFString=}$kODAttributeTypePasswordServerList@^{__CFString=}$kODAttributeTypePasswordServerLocation@^{__CFString=}$kODAttributeTypePhoneContacts@^{__CFString=}$kODAttributeTypePhoneNumber@^{__CFString=}$kODAttributeTypePicture@^{__CFString=}$kODAttributeTypePlugInInfo@^{__CFString=}$kODAttributeTypePluginIndex@^{__CFString=}$kODAttributeTypePort@^{__CFString=}$kODAttributeTypePostalAddress@^{__CFString=}$kODAttributeTypePostalAddressContacts@^{__CFString=}$kODAttributeTypePostalCode@^{__CFString=}$kODAttributeTypePresetUserIsAdmin@^{__CFString=}$kODAttributeTypePrimaryComputerGUID@^{__CFString=}$kODAttributeTypePrimaryComputerList@^{__CFString=}$kODAttributeTypePrimaryGroupID@^{__CFString=}$kODAttributeTypePrimaryNTDomain@^{__CFString=}$kODAttributeTypePrintServiceInfoText@^{__CFString=}$kODAttributeTypePrintServiceInfoXML@^{__CFString=}$kODAttributeTypePrintServiceUserData@^{__CFString=}$kODAttributeTypePrinter1284DeviceID@^{__CFString=}$kODAttributeTypePrinterLPRHost@^{__CFString=}$kODAttributeTypePrinterLPRQueue@^{__CFString=}$kODAttributeTypePrinterMakeAndModel@^{__CFString=}$kODAttributeTypePrinterType@^{__CFString=}$kODAttributeTypePrinterURI@^{__CFString=}$kODAttributeTypePrinterXRISupported@^{__CFString=}$kODAttributeTypeProcessName@^{__CFString=}$kODAttributeTypeProtocolNumber@^{__CFString=}$kODAttributeTypeProtocols@^{__CFString=}$kODAttributeTypePwdAgingPolicy@^{__CFString=}$kODAttributeTypeRPCNumber@^{__CFString=}$kODAttributeTypeReadOnlyNode@^{__CFString=}$kODAttributeTypeRealUserID@^{__CFString=}$kODAttributeTypeRecRefCount@^{__CFString=}$kODAttributeTypeRecRefs@^{__CFString=}$kODAttributeTypeRecordName@^{__CFString=}$kODAttributeTypeRecordType@^{__CFString=}$kODAttributeTypeRelationships@^{__CFString=}$kODAttributeTypeRelativeDNPrefix@^{__CFString=}$kODAttributeTypeResourceInfo@^{__CFString=}$kODAttributeTypeResourceType@^{__CFString=}$kODAttributeTypeSMBAcctFlags@^{__CFString=}$kODAttributeTypeSMBGroupRID@^{__CFString=}$kODAttributeTypeSMBHome@^{__CFString=}$kODAttributeTypeSMBHomeDrive@^{__CFString=}$kODAttributeTypeSMBKickoffTime@^{__CFString=}$kODAttributeTypeSMBLogoffTime@^{__CFString=}$kODAttributeTypeSMBLogonTime@^{__CFString=}$kODAttributeTypeSMBPWDLastSet@^{__CFString=}$kODAttributeTypeSMBPrimaryGroupSID@^{__CFString=}$kODAttributeTypeSMBProfilePath@^{__CFString=}$kODAttributeTypeSMBRID@^{__CFString=}$kODAttributeTypeSMBSID@^{__CFString=}$kODAttributeTypeSMBScriptPath@^{__CFString=}$kODAttributeTypeSMBUserWorkstations@^{__CFString=}$kODAttributeTypeSchema@^{__CFString=}$kODAttributeTypeSearchPath@^{__CFString=}$kODAttributeTypeSearchPolicy@^{__CFString=}$kODAttributeTypeServiceType@^{__CFString=}$kODAttributeTypeServicesLocator@^{__CFString=}$kODAttributeTypeSetupAdvertising@^{__CFString=}$kODAttributeTypeSetupAutoRegister@^{__CFString=}$kODAttributeTypeSetupLocation@^{__CFString=}$kODAttributeTypeSetupOccupation@^{__CFString=}$kODAttributeTypeStandardOnly@^{__CFString=}$kODAttributeTypeState@^{__CFString=}$kODAttributeTypeStreet@^{__CFString=}$kODAttributeTypeSubNodes@^{__CFString=}$kODAttributeTypeTimePackage@^{__CFString=}$kODAttributeTypeTimeToLive@^{__CFString=}$kODAttributeTypeTotalRefCount@^{__CFString=}$kODAttributeTypeTotalSize@^{__CFString=}$kODAttributeTypeURL@^{__CFString=}$kODAttributeTypeUniqueID@^{__CFString=}$kODAttributeTypeUserCertificate@^{__CFString=}$kODAttributeTypeUserPKCS12Data@^{__CFString=}$kODAttributeTypeUserSMIMECertificate@^{__CFString=}$kODAttributeTypeUserShell@^{__CFString=}$kODAttributeTypeVFSDumpFreq@^{__CFString=}$kODAttributeTypeVFSLinkDir@^{__CFString=}$kODAttributeTypeVFSOpts@^{__CFString=}$kODAttributeTypeVFSPassNo@^{__CFString=}$kODAttributeTypeVFSType@^{__CFString=}$kODAttributeTypeVersion@^{__CFString=}$kODAttributeTypeWeblogURI@^{__CFString=}$kODAttributeTypeXMLPlist@^{__CFString=}$kODAuthenticationType2WayRandom@^{__CFString=}$kODAuthenticationType2WayRandomChangePasswd@^{__CFString=}$kODAuthenticationTypeAPOP@^{__CFString=}$kODAuthenticationTypeCRAM_MD5@^{__CFString=}$kODAuthenticationTypeChangePasswd@^{__CFString=}$kODAuthenticationTypeClearText@^{__CFString=}$kODAuthenticationTypeCrypt@^{__CFString=}$kODAuthenticationTypeDIGEST_MD5@^{__CFString=}$kODAuthenticationTypeDeleteUser@^{__CFString=}$kODAuthenticationTypeGetEffectivePolicy@^{__CFString=}$kODAuthenticationTypeGetGlobalPolicy@^{__CFString=}$kODAuthenticationTypeGetKerberosPrincipal@^{__CFString=}$kODAuthenticationTypeGetPolicy@^{__CFString=}$kODAuthenticationTypeGetUserData@^{__CFString=}$kODAuthenticationTypeGetUserName@^{__CFString=}$kODAuthenticationTypeKerberosTickets@^{__CFString=}$kODAuthenticationTypeMPPEMasterKeys@^{__CFString=}$kODAuthenticationTypeMSCHAP2@^{__CFString=}$kODAuthenticationTypeNTLMv2@^{__CFString=}$kODAuthenticationTypeNTLMv2WithSessionKey@^{__CFString=}$kODAuthenticationTypeNewUser@^{__CFString=}$kODAuthenticationTypeNewUserWithPolicy@^{__CFString=}$kODAuthenticationTypeNodeNativeClearTextOK@^{__CFString=}$kODAuthenticationTypeNodeNativeNoClearText@^{__CFString=}$kODAuthenticationTypeReadSecureHash@^{__CFString=}$kODAuthenticationTypeSMBNTv2UserSessionKey@^{__CFString=}$kODAuthenticationTypeSMBWorkstationCredentialSessionKey@^{__CFString=}$kODAuthenticationTypeSMB_LM_Key@^{__CFString=}$kODAuthenticationTypeSMB_NT_Key@^{__CFString=}$kODAuthenticationTypeSMB_NT_UserSessionKey@^{__CFString=}$kODAuthenticationTypeSMB_NT_WithUserSessionKey@^{__CFString=}$kODAuthenticationTypeSecureHash@^{__CFString=}$kODAuthenticationTypeSetGlobalPolicy@^{__CFString=}$kODAuthenticationTypeSetLMHash@^{__CFString=}$kODAuthenticationTypeSetNTHash@^{__CFString=}$kODAuthenticationTypeSetPassword@^{__CFString=}$kODAuthenticationTypeSetPasswordAsCurrent@^{__CFString=}$kODAuthenticationTypeSetPolicy@^{__CFString=}$kODAuthenticationTypeSetPolicyAsCurrent@^{__CFString=}$kODAuthenticationTypeSetUserData@^{__CFString=}$kODAuthenticationTypeSetUserName@^{__CFString=}$kODAuthenticationTypeSetWorkstationPassword@^{__CFString=}$kODAuthenticationTypeWithAuthorizationRef@^{__CFString=}$kODAuthenticationTypeWriteSecureHash@^{__CFString=}$kODErrorDomainFramework@^{__CFString=}$kODRecordTypeAFPServer@^{__CFString=}$kODRecordTypeAliases@^{__CFString=}$kODRecordTypeAttributeTypes@^{__CFString=}$kODRecordTypeAugments@^{__CFString=}$kODRecordTypeAutoServerSetup@^{__CFString=}$kODRecordTypeAutomount@^{__CFString=}$kODRecordTypeAutomountMap@^{__CFString=}$kODRecordTypeBootp@^{__CFString=}$kODRecordTypeCertificateAuthorities@^{__CFString=}$kODRecordTypeComputerGroups@^{__CFString=}$kODRecordTypeComputerLists@^{__CFString=}$kODRecordTypeComputers@^{__CFString=}$kODRecordTypeConfiguration@^{__CFString=}$kODRecordTypeEthernets@^{__CFString=}$kODRecordTypeFTPServer@^{__CFString=}$kODRecordTypeFileMakerServers@^{__CFString=}$kODRecordTypeGroups@^{__CFString=}$kODRecordTypeHostServices@^{__CFString=}$kODRecordTypeHosts@^{__CFString=}$kODRecordTypeLDAPServer@^{__CFString=}$kODRecordTypeLocations@^{__CFString=}$kODRecordTypeMounts@^{__CFString=}$kODRecordTypeNFS@^{__CFString=}$kODRecordTypeNetDomains@^{__CFString=}$kODRecordTypeNetGroups@^{__CFString=}$kODRecordTypeNetworks@^{__CFString=}$kODRecordTypePeople@^{__CFString=}$kODRecordTypePresetComputerGroups@^{__CFString=}$kODRecordTypePresetComputerLists@^{__CFString=}$kODRecordTypePresetComputers@^{__CFString=}$kODRecordTypePresetGroups@^{__CFString=}$kODRecordTypePresetUsers@^{__CFString=}$kODRecordTypePrintService@^{__CFString=}$kODRecordTypePrintServiceUser@^{__CFString=}$kODRecordTypePrinters@^{__CFString=}$kODRecordTypeProtocols@^{__CFString=}$kODRecordTypeQTSServer@^{__CFString=}$kODRecordTypeRPC@^{__CFString=}$kODRecordTypeRecordTypes@^{__CFString=}$kODRecordTypeResources@^{__CFString=}$kODRecordTypeSMBServer@^{__CFString=}$kODRecordTypeServer@^{__CFString=}$kODRecordTypeServices@^{__CFString=}$kODRecordTypeSharePoints@^{__CFString=}$kODRecordTypeUsers@^{__CFString=}$kODRecordTypeWebServer@^{__CFString=}$kODSessionDefault@^{_ODSessionRef=}$kODSessionProxyAddress@^{__CFString=}$kODSessionProxyPassword@^{__CFString=}$kODSessionProxyPort@^{__CFString=}$kODSessionProxyUsername@^{__CFString=}$'''
enums = '''$kODErrorCredentialsAccountDisabled@5301$kODErrorCredentialsAccountExpired@5302$kODErrorCredentialsAccountInactive@5303$kODErrorCredentialsAccountNotFound@5300$kODErrorCredentialsContactMaster@5204$kODErrorCredentialsInvalid@5000$kODErrorCredentialsInvalidComputer@5501$kODErrorCredentialsInvalidLogonHours@5500$kODErrorCredentialsMethodNotSupported@5100$kODErrorCredentialsNotAuthorized@5101$kODErrorCredentialsOperationFailed@5103$kODErrorCredentialsParameterError@5102$kODErrorCredentialsPasswordChangeRequired@5401$kODErrorCredentialsPasswordChangeTooSoon@5407$kODErrorCredentialsPasswordExpired@5400$kODErrorCredentialsPasswordNeedsDigit@5406$kODErrorCredentialsPasswordNeedsLetter@5405$kODErrorCredentialsPasswordQualityFailed@5402$kODErrorCredentialsPasswordTooLong@5404$kODErrorCredentialsPasswordTooShort@5403$kODErrorCredentialsPasswordUnrecoverable@5408$kODErrorCredentialsServerCommunicationError@5205$kODErrorCredentialsServerError@5202$kODErrorCredentialsServerNotFound@5201$kODErrorCredentialsServerTimeout@5203$kODErrorCredentialsServerUnreachable@5200$kODErrorDaemonError@10002$kODErrorNodeConnectionFailed@2100$kODErrorNodeUnknownHost@2200$kODErrorNodeUnknownName@2000$kODErrorNodeUnknownType@2001$kODErrorPluginError@10001$kODErrorPluginOperationNotSupported@10000$kODErrorQueryInvalidMatchType@3100$kODErrorQuerySynchronize@3000$kODErrorQueryTimeout@3102$kODErrorQueryUnsupportedMatchType@3101$kODErrorRecordAlreadyExists@4102$kODErrorRecordAttributeNotFound@4201$kODErrorRecordAttributeUnknownType@4200$kODErrorRecordAttributeValueNotFound@4203$kODErrorRecordAttributeValueSchemaError@4202$kODErrorRecordInvalidType@4101$kODErrorRecordParameterError@4100$kODErrorRecordPermissionError@4001$kODErrorRecordReadOnlyNode@4000$kODErrorRecordTypeDisabled@4103$kODErrorSessionDaemonNotRunning@1002$kODErrorSessionDaemonRefused@1003$kODErrorSessionLocalOnlyDaemonInUse@1000$kODErrorSessionNormalDaemonInUse@1001$kODErrorSessionProxyCommunicationError@1100$kODErrorSessionProxyIPUnreachable@1102$kODErrorSessionProxyUnknownHost@1103$kODErrorSessionProxyVersionMismatch@1101$kODMatchAny@1$kODMatchBeginsWith@8194$kODMatchContains@8196$kODMatchEndsWith@8195$kODMatchEqualTo@8193$kODMatchGreaterThan@8198$kODMatchInsensitiveBeginsWith@8450$kODMatchInsensitiveContains@8452$kODMatchInsensitiveEndsWith@8451$kODMatchInsensitiveEqualTo@8449$kODMatchLessThan@8199$kODNodeTypeAuthentication@8705$kODNodeTypeConfigure@8706$kODNodeTypeContacts@8708$kODNodeTypeLocalNodes@8704$kODNodeTypeNetwork@8709$'''
misc.update({})
functions = {'ODNodeCopySubnodeNames': ('^{__CFArray=}^{_ODNode=}^^{__CFError}',), 'ODNodeSetCredentialsExtended': ('Z^{_ODNode=}^{__CFString=}^{__CFString=}^{__CFArray=}^^{__CFArray}^^{_ODContext}^^{__CFError}',), 'ODNodeCreateCopy': ('^{_ODNode=}^{__CFAllocator=}^{_ODNode=}^^{__CFError}',), 'ODNodeGetTypeID': ('Q',), 'ODNodeCustomCall': ('^{__CFData=}^{_ODNode=}q^{__CFData=}^^{__CFError}',), 'ODRecordDelete': ('Z^{_ODRecord=}^^{__CFError}',), 'ODRecordSetNodeCredentials': ('Z^{_ODRecord=}^{__CFString=}^{__CFString=}^^{__CFError}',), 'ODRecordGetRecordName': ('^{__CFString=}^{_ODRecord=}',), 'ODQueryScheduleWithRunLoop': ('v^{_ODQuery=}^{__CFRunLoop=}^{__CFString=}',), 'ODRecordAddMember': ('Z^{_ODRecord=}^{_ODRecord=}^^{__CFError}',), 'ODQuerySetCallback': ('v^{_ODQuery=}^?^v',), 'ODQuerySynchronize': ('v^{_ODQuery=}',), 'ODSessionCopyNodeNames': ('^{__CFArray=}^{__CFAllocator=}^{_ODSessionRef=}^^{__CFError}',), 'ODNodeCopySupportedAttributes': ('^{__CFArray=}^{_ODNode=}^{__CFString=}^^{__CFError}',), 'ODRecordGetRecordType': ('^{__CFString=}^{_ODRecord=}',), 'ODNodeCopyRecord': ('^{_ODRecord=}^{_ODNode=}^{__CFString=}^{__CFString=}^{__CFArray=}^^{__CFError}',), 'ODNodeGetName': ('^{__CFString=}^{_ODNode=}',), 'ODSessionCreate': ('^{_ODSessionRef=}^{__CFAllocator=}^{__CFDictionary=}^^{__CFError}',), 'ODRecordContainsMember': ('Z^{_ODRecord=}^{_ODRecord=}^^{__CFError}',), 'ODRecordSynchronize': ('Z^{_ODRecord=}^^{__CFError}',), 'ODQueryCreateWithNodeType': ('^{_ODQuery=}^{__CFAllocator=}I@^{__CFString=}I@@q^^{__CFError}',), 'ODNodeCopySupportedRecordTypes': ('^{__CFArray=}^{_ODNode=}^^{__CFError}',), 'ODQuerySetDispatchQueue': ('v^{_ODQuery=}^{dispatch_queue_s=}',), 'ODRecordVerifyPassword': ('Z^{_ODRecord=}^{__CFString=}^^{__CFError}',), 'ODNodeCopyDetails': ('^{__CFDictionary=}^{_ODNode=}^{__CFArray=}^^{__CFError}',), 'ODQueryCreateWithNode': ('^{_ODQuery=}^{__CFAllocator=}^{_ODNode=}@^{__CFString=}I@@q^^{__CFError}',), 'ODContextGetTypeID': ('Q',), 'ODRecordCopyPasswordPolicy': ('^{__CFDictionary=}^{__CFAllocator=}^{_ODRecord=}^^{__CFError}',), 'ODNodeSetCredentials': ('Z^{_ODNode=}^{__CFString=}^{__CFString=}^{__CFString=}^^{__CFError}',), 'ODNodeCreateRecord': ('^{_ODRecord=}^{_ODNode=}^{__CFString=}^{__CFString=}^{__CFDictionary=}^^{__CFError}',), 'ODRecordGetTypeID': ('Q',), 'ODRecordCopyValues': ('^{__CFArray=}^{_ODRecord=}^{__CFString=}^^{__CFError}',), 'ODRecordSetValue': ('Z^{_ODRecord=}^{__CFString=}@^^{__CFError}',), 'ODRecordSetNodeCredentialsExtended': ('Z^{_ODRecord=}^{__CFString=}^{__CFString=}^{__CFArray=}^^{__CFArray}^^{_ODContext}^^{__CFError}',), 'ODQueryGetTypeID': ('Q',), 'ODRecordSetNodeCredentialsUsingKerberosCache': ('Z^{_ODRecord=}^{__CFString=}^^{__CFError}',), 'ODNodeCreateWithName': ('^{_ODNode=}^{__CFAllocator=}^{_ODSessionRef=}^{__CFString=}^^{__CFError}',), 'ODRecordRemoveValue': ('Z^{_ODRecord=}^{__CFString=}@^^{__CFError}',), 'ODSessionGetTypeID': ('Q',), 'ODRecordCopyDetails': ('^{__CFDictionary=}^{_ODRecord=}^{__CFArray=}^^{__CFError}',), 'ODNodeSetCredentialsUsingKerberosCache': ('Z^{_ODNode=}^{__CFString=}^^{__CFError}',), 'ODRecordChangePassword': ('Z^{_ODRecord=}^{__CFString=}^{__CFString=}^^{__CFError}',), 'ODQueryCopyResults': ('^{__CFArray=}^{_ODQuery=}Z^^{__CFError}',), 'ODRecordVerifyPasswordExtended': ('Z^{_ODRecord=}^{__CFString=}^{__CFArray=}^^{__CFArray}^^{_ODContext}^^{__CFError}',), 'ODRecordRemoveMember': ('Z^{_ODRecord=}^{_ODRecord=}^^{__CFError}',), 'ODNodeCreateWithNodeType': ('^{_ODNode=}^{__CFAllocator=}^{_ODSessionRef=}I^^{__CFError}',), 'ODNodeCopyUnreachableSubnodeNames': ('^{__CFArray=}^{_ODNode=}^^{__CFError}',), 'ODQueryUnscheduleFromRunLoop': ('v^{_ODQuery=}^{__CFRunLoop=}^{__CFString=}',), 'ODRecordAddValue': ('Z^{_ODRecord=}^{__CFString=}@^^{__CFError}',)}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
finally:
    objc._updatingMetadata(False)
