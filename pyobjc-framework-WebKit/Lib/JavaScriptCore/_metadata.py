# This file is generated by objective.metadata
#
# Last update: Thu Mar  8 09:49:40 2012

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
}
constants = '''$kJSClassDefinitionEmpty@{_JSClassDefinition=iI^c^{OpaqueJSClass=}^{_JSStaticValue=^c^?^?I}^{_JSStaticFunction=^c^?I}^?^?^?^?^?^?^?^?^?^?^?}$'''
enums = '''$WEBKIT_VERSION_1_0@256$WEBKIT_VERSION_1_1@272$WEBKIT_VERSION_1_2@288$WEBKIT_VERSION_1_3@304$WEBKIT_VERSION_2_0@512$WEBKIT_VERSION_3_0@768$WEBKIT_VERSION_3_1@784$WEBKIT_VERSION_4_0@1024$WEBKIT_VERSION_LATEST@39321$kJSClassAttributeNoAutomaticPrototype@2$kJSClassAttributeNone@0$kJSPropertyAttributeDontDelete@8$kJSPropertyAttributeDontEnum@4$kJSPropertyAttributeNone@0$kJSPropertyAttributeReadOnly@2$kJSTypeBoolean@2$kJSTypeNull@1$kJSTypeNumber@3$kJSTypeObject@5$kJSTypeString@4$kJSTypeUndefined@0$'''
misc.update({})
functions={'JSStringGetCharactersPtr': (b'^S^{OpaqueJSString=}',), 'JSValueToObject': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSValueGetType': (b'i^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSClassRetain': (b'^{OpaqueJSClass=}^{OpaqueJSClass=}',), 'JSValueCreateJSONString': (b'^{OpaqueJSString=}^{OpaqueJSContext=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectMakeFunctionWithCallback': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}^?', '', {'arguments': {2: {'function': {'args': [{'typestr': [u'^{OpaqueJSContext=}', False]}, {'typestr': [u'^{OpaqueJSValue=}', False]}, {'typestr': [u'^{OpaqueJSValue=}', False]}, {'typestr': [u'l', False]}, {'typestr': [u'^^{OpaqueJSValue=}', False]}, {'typestr': [u'^^{OpaqueJSValue=}', False]}], 'retval': {'typestr': [u'^{OpaqueJSValue=}', False]}}}}}), 'JSValueIsObject': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSPropertyNameArrayRetain': (b'^{OpaqueJSPropertyNameArray=}^{OpaqueJSPropertyNameArray=}',), 'JSValueIsString': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSStringGetUTF8CString': (b'l^{OpaqueJSString=}^cl',), 'JSStringCreateWithCFString': (b'^{OpaqueJSString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'JSValueToBoolean': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSContextGetGlobalObject': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSGlobalContextCreate': (b'^{OpaqueJSContext=}^{OpaqueJSClass=}', '', {'retval': {'already_cfretained': True}}), 'JSStringCopyCFString': (b'^{__CFString=}^{__CFAllocator=}^{OpaqueJSString=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectGetPrivate': (b'^v^{OpaqueJSValue=}',), 'JSObjectSetProperty': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}',), 'JSValueIsEqual': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSObjectIsFunction': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectCopyPropertyNames': (b'^{OpaqueJSPropertyNameArray=}^{OpaqueJSContext=}^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSValueIsBoolean': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsUndefined': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueProtect': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsObjectOfClass': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSClass=}',), 'JSObjectGetPrototype': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueMakeString': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSObjectMakeArray': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}l^^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSStringIsEqualToUTF8CString': (b'B^{OpaqueJSString=}^c',), 'JSPropertyNameArrayGetNameAtIndex': (b'^{OpaqueJSString=}^{OpaqueJSPropertyNameArray=}l',), 'JSValueMakeNull': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSStringGetMaximumUTF8CStringSize': (b'l^{OpaqueJSString=}',), 'JSObjectMakeError': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}l^^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSValueMakeBoolean': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}B',), 'JSGlobalContextRelease': (b'v^{OpaqueJSContext=}',), 'JSObjectMakeRegExp': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}l^^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSObjectSetPropertyAtIndex': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}I^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSContextGetGroup': (b'^{OpaqueJSContextGroup=}^{OpaqueJSContext=}',), 'JSContextGroupCreate': (b'^{OpaqueJSContextGroup=}', '', {'retval': {'already_cfretained': True}}), 'JSValueMakeNumber': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}d',), 'JSValueIsInstanceOfConstructor': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSValueIsNull': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSStringIsEqual': (b'B^{OpaqueJSString=}^{OpaqueJSString=}',), 'JSObjectCallAsConstructor': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}l^^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSStringRetain': (b'^{OpaqueJSString=}^{OpaqueJSString=}',), 'JSObjectDeleteProperty': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^^{OpaqueJSValue=}',), 'JSObjectMakeConstructor': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSClass=}^?', '', {'arguments': {2: {'function': {'args': [{'typestr': [u'^{OpaqueJSContext=}', False]}, {'typestr': [u'^{OpaqueJSValue=}', False]}, {'typestr': [u'l', False]}, {'typestr': [u'^^{OpaqueJSValue=}', False]}, {'typestr': [u'^^{OpaqueJSValue=}', False]}], 'retval': {'typestr': [u'^{OpaqueJSValue=}', False]}}}}}), 'JSObjectSetPrivate': (b'B^{OpaqueJSValue=}^v',), 'JSObjectMakeFunction': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}I^^{OpaqueJSString=}^{OpaqueJSString=}^{OpaqueJSString=}i^^{OpaqueJSValue=}',), 'JSValueToStringCopy': (b'^{OpaqueJSString=}^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSValueMakeFromJSONString': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSValueIsNumber': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSEvaluateScript': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}^{OpaqueJSValue=}^{OpaqueJSString=}i^^{OpaqueJSValue=}',), 'JSObjectGetPropertyAtIndex': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}',), 'JSStringCreateWithCharacters': (b'^{OpaqueJSString=}^Sl', '', {'retval': {'already_cfretained': True}}), 'JSValueToNumber': (b'd^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSObjectGetProperty': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^^{OpaqueJSValue=}',), 'JSPropertyNameAccumulatorAddName': (b'v^{OpaqueJSPropertyNameAccumulator=}^{OpaqueJSString=}',), 'JSObjectSetPrototype': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}',), 'JSContextGroupRelease': (b'v^{OpaqueJSContextGroup=}',), 'JSStringCreateWithUTF8CString': (b'^{OpaqueJSString=}^c', '', {'retval': {'already_cfretained': True}}), 'JSValueIsStrictEqual': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}',), 'JSObjectMake': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSClass=}^v',), 'JSValueMakeUndefined': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSCheckScriptSyntax': (b'B^{OpaqueJSContext=}^{OpaqueJSString=}^{OpaqueJSString=}i^^{OpaqueJSValue=}',), 'JSObjectHasProperty': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}',), 'JSValueUnprotect': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectIsConstructor': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectMakeDate': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}l^^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSPropertyNameArrayRelease': (b'v^{OpaqueJSPropertyNameArray=}',), 'JSClassRelease': (b'v^{OpaqueJSClass=}',), 'JSObjectCallAsFunction': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}l^^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSContextGroupRetain': (b'^{OpaqueJSContextGroup=}^{OpaqueJSContextGroup=}',), 'JSClassCreate': (b'^{OpaqueJSClass=}^{_JSClassDefinition=iI^c^{OpaqueJSClass=}^{_JSStaticValue=^c^?^?I}^{_JSStaticFunction=^c^?I}^?^?^?^?^?^?^?^?^?^?^?}', '', {'retval': {'already_cfretained': True}}), 'JSGlobalContextCreateInGroup': (b'^{OpaqueJSContext=}^{OpaqueJSContextGroup=}^{OpaqueJSClass=}', '', {'retval': {'already_cfretained': True}}), 'JSPropertyNameArrayGetCount': (b'l^{OpaqueJSPropertyNameArray=}',), 'JSGlobalContextRetain': (b'^{OpaqueJSContext=}^{OpaqueJSContext=}',), 'JSGarbageCollect': (b'v^{OpaqueJSContext=}',), 'JSStringRelease': (b'v^{OpaqueJSString=}',), 'JSStringGetLength': (b'l^{OpaqueJSString=}',)}
expressions = {}

# END OF FILE
