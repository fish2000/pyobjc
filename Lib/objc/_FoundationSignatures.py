
#
# This file is generated by 'create_byref_module.py'. Do not edit.
#
# Generated from 'Lib/Foundation/Foundation.byref'.
#
#
from objc import set_signature_for_selector

set_signature_for_selector("NSScanner", "scanCharactersFromSet:intoString:", "c@:@o^@")
set_signature_for_selector("NSScanner", "scanDouble:", "c@:o^d")
set_signature_for_selector("NSScanner", "scanFloat:", "c@:o^f")
set_signature_for_selector("NSScanner", "scanHexInt:", "c@:o^I")
set_signature_for_selector("NSScanner", "scanInt:", "c@:o^i")
set_signature_for_selector("NSScanner", "scanLongLong:", "c@:o^q")
set_signature_for_selector("NSScanner", "scanString:intoString:", "c@:@o^@")
set_signature_for_selector("NSScanner", "scanUpToCharactersFromSet:intoString:", "c@:@o^@")
set_signature_for_selector("NSScanner", "scanUpToString:intoString:", "c@:@o^@")
set_signature_for_selector("NSString", "completePathIntoString:caseSensitive:matchesIntoArray:filterTypes:", "Io^@co^@@")
set_signature_for_selector("NSString", "getLineStart:end:contentsEnd:forRange:", "v@:o^Io^Io^I{_NSRange=II}")
set_signature_for_selector("NSMutableAttributedString", "readFromURL:options:documentAttributes:", "c@:@@o^@")
set_signature_for_selector("NSAttributedString", "attribute:atIndex:effectiveRange:", "@0@4:8@12I16o^{_NSRange=II}20")
set_signature_for_selector("NSAttributedString", "attribute:atIndex:longestEffectiveRange:inRange:", "@0@4:8@12I16o^{_NSRange=II}20{_NSRange=II}24")
set_signature_for_selector("NSAttributedString", "attributesAtIndex:effectiveRange:", "@0@4:8I12o^{_NSRange=II}16")
set_signature_for_selector("NSAttributedString", "attributesAtIndex:longestEffectiveRange:inRange:", "@0@4:8I12o^{_NSRange=II}16{_NSRange=II}20")
set_signature_for_selector("NSAttributedString", "initWithHTML:baseURL:documentAttributes:", "@0@4:8@12@16o^@20")
set_signature_for_selector("NSAttributedString", "initWithHTML:documentAttributes:", "@@:@o^@")
set_signature_for_selector("NSAttributedString", "initWithPath:documentAttributes:", "@@:@o^@")
set_signature_for_selector("NSAttributedString", "initWithRTFDFileWrapper:documentAttributes:", "@@:@o^@")
set_signature_for_selector("NSAttributedString", "initWithRTFD:documentAttributes:", "@0@4:8@12o^@16")
set_signature_for_selector("NSAttributedString", "initWithRTF:documentAttributes:", "@0@4:8@12o^@16")
set_signature_for_selector("NSAttributedString", "initWithURL:documentAttributes:", "@0@4:8@12o^@16")
set_signature_for_selector("NSFileManager", "fileExistsAtPath:isDirectory:", "c0@4:8@12o^c16")
set_signature_for_selector("NSArray", "getObject:atIndex:", "c@:o^@I")
set_signature_for_selector("NSCalendarDate", "years:months:days:hours:minutes:seconds:sinceDate:", "v@:o^io^io^io^io^io^i@")
set_signature_for_selector("NSPropertyListSerialization", "dataFromPropertyList:format:errorDescription:", "@@:@io^@")
set_signature_for_selector("NSPropertyListSerialization", "propertyListFromData:mutabilityOption:format:errorDescription:", "@@:@iN^io^@")
set_signature_for_selector("NSAppleScript", "_initWithContentsOfFile:error:", "@@:@o^@")
set_signature_for_selector("NSAppleScript", "_initWithData:error:", "@@:@o^@")
set_signature_for_selector("NSAppleScript", "compileAndReturnError:", "c@:o^@")
set_signature_for_selector("NSAppleScript", "executeAndReturnError:", "@@:o^@")
set_signature_for_selector("NSAppleScript", "executeAppleEvent:error:", "@@:@o^@")
set_signature_for_selector("NSAppleScript", "initWithContentsOfURL:error:", "@@:@o^@")
set_signature_for_selector("NSFaultHandler", "extraData", "i@:")
set_signature_for_selector("NSFaultHandler", "setTargetClass:extraData:", "v@:#i")
set_signature_for_selector("NSFormatter", "getObjectValue:forString:errorDescription:", "c@:o^@@o^@")
set_signature_for_selector("NSFormatter", "isPartialStringValid:newEditingString:errorDescription:", "c@:@o^@o^@")
set_signature_for_selector("NSFormatter", "isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:", "c0@4:8o^@12o^{_NSRange=II}16@20{_NSRange=II}24o^@32")
