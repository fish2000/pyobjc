"""
Instances of WSTConnectionWindowController are the controlling object
for the document windows for the Web Services Tool application.

Implements a standard toolbar.
"""
from AppKit import *
from Foundation import *

from objc import IBOutlet
from objc import selector
from objc import YES, NO

import xmlrpclib
import sys
import types
import string
import traceback

kWSTReloadContentsToolbarItemIdentifier = "WST: Reload Contents Toolbar Identifier"
"""Identifier for 'reload contents' toolbar item."""

kWSTPreferencesToolbarItemIdentifier = "WST: Preferences Toolbar Identifier"
"""Identifier for 'preferences' toolbar item."""

kWSTUrlTextFieldToolbarItemIdentifier = "WST: URL Textfield Toolbar Identifier"
"""Idnetifier for URL text field toolbar item."""

def addToolbarItem(aController, anIdentifier, aLabel, aPaletteLabel,
                   aToolTip, aTarget, anAction, anItemContent, aMenu):
    """
    Adds an freshly created item to the toolber defined by
    aController.  Makes a number of assumptions about the
    implementation of aController.   It should be refactored into a
    generically useful toolbar management untility.
    """
    toolbarItem = NSToolbarItem.alloc().initWithItemIdentifier_(anIdentifier)
    
    toolbarItem.setLabel_(aLabel)
    toolbarItem.setPaletteLabel_(aPaletteLabel)
    toolbarItem.setToolTip_(aToolTip)
    toolbarItem.setTarget_(aTarget)
    if anAction:
        toolbarItem.setAction_(anAction)
    
    if type(anItemContent) == NSImage:
        toolbarItem.setImage_(anItemContent)
    else:
        toolbarItem.setView_(anItemContent)
        bounds = anItemContent.bounds()
        minSize = (100, bounds[1][1])
        maxSize = (1000, bounds[1][1])
        toolbarItem.setMinSize_( minSize )
        toolbarItem.setMaxSize_( maxSize )
        
    if aMenu:
        menuItem = NSMenuItem.alloc().init()
        menuItem.setSubmenu_(aMenu)
        menuItem.setTitle_( aMenu.title() )
        toolbarItem.setMenuFormRepresentation_(menuItem)
    
    aController._toolbarItems.setObject_forKey_(toolbarItem, anIdentifier)

from PyObjCTools import NibClassBuilder

NibClassBuilder.extractClasses( "WSTConnection" )
class WSTConnectionWindowController(NibClassBuilder.AutoBaseClass, 
                                    NSTableDataSource, NSToolbarDelegate):
    """
    As per the definition in the NIB file,
    WSTConnectionWindowController is a subclass of
    NSWindowController.  It acts as a NSTableView data source and
    implements a standard toolbar.
    """
    __slots__ = ('_toolbarItems',
        '_toolbarDefaultItemIdentifiers',
        '_toolbarAllowedItemIdentifiers',
        '_methods',
        '_methodSignatures',
        '_methodDescriptions',
        '_server',
        '_methodPrefix' )
    
    def connectionWindowController(self):
        """
        Create and return a default connection window instance.
        """
        return WSTConnectionWindowController.alloc().init()
           
    def init(self):
        """
        Designated initializer.

        Returns self (as per ObjC designated initializer definition,
        unlike Python's __init__() method).
        """
        self = self.initWithWindowNibName_("WSTConnection")

        # assignments imply a -retain!
        self._toolbarItems = NSMutableDictionary.dictionary()
        self._toolbarDefaultItemIdentifiers = NSMutableArray.array()
        self._toolbarAllowedItemIdentifiers = NSMutableArray.array()

        self._methods = []
                
        return self
    
    def awakeFromNib(self):
        """
        Invoked when the NIB file is loaded.  Initializes the various
        UI widgets.
        """
        self.retain() # balanced by autorelease() in windowWillClose_
        
        self.statusTextField.setStringValue_("No host specified.")
        self.progressIndicator.setStyle_(NSProgressIndicatorSpinningStyle)
        self.progressIndicator.setUsesThreadedAnimation_(YES)
        self.progressIndicator.setDisplayedWhenStopped_(NO)
        
        self.createToolbar()
        
    def windowWillClose_(self, aNotification):
        """
        Clean up when the document window is closed.
        """
        self.autorelease()

    def createToolbar(self):
        """
        Creates and configures the toolbar to be used by the window.
        """
        toolbar = NSToolbar.alloc().initWithIdentifier_("WST Connection Window")
        toolbar.setDelegate_(self)
        toolbar.setAllowsUserCustomization_(YES)
        toolbar.setAutosavesConfiguration_(YES)
        
        self.createToolbarItems()
        
        self.window().setToolbar_(toolbar)

        lastURL = NSUserDefaults.standardUserDefaults().stringForKey_("LastURL")
        if lastURL and len(lastURL):
            self.urlTextField.setStringValue_(lastURL)
        
    def createToolbarItems(self):
        """
        Creates all of the toolbar items that can be made available in
        the toolbar.  The actual set of available toolbar items is
        determined by other mechanisms (user defaults, for example).
        """
        addToolbarItem(self, kWSTReloadContentsToolbarItemIdentifier, "Reload", "Reload", "Reload Contents", None, "reloadVisibleData:", NSImage.imageNamed_("Reload"), None)
        addToolbarItem(self, kWSTPreferencesToolbarItemIdentifier, "Preferences", "Preferences", "Show Preferences", None, "orderFrontPreferences:", NSImage.imageNamed_("Preferences"), None)
        addToolbarItem(self, kWSTUrlTextFieldToolbarItemIdentifier, "URL", "URL", "Server URL", None, None, self.urlTextField, None)
        
        self._toolbarDefaultItemIdentifiers.addObject_(kWSTReloadContentsToolbarItemIdentifier)
        self._toolbarDefaultItemIdentifiers.addObject_(kWSTUrlTextFieldToolbarItemIdentifier)
        self._toolbarDefaultItemIdentifiers.addObject_(NSToolbarSeparatorItemIdentifier)
        self._toolbarDefaultItemIdentifiers.addObject_(NSToolbarCustomizeToolbarItemIdentifier)
        
        self._toolbarAllowedItemIdentifiers.addObject_(kWSTReloadContentsToolbarItemIdentifier)
        self._toolbarAllowedItemIdentifiers.addObject_(kWSTUrlTextFieldToolbarItemIdentifier)
        self._toolbarAllowedItemIdentifiers.addObject_(NSToolbarSeparatorItemIdentifier)
        self._toolbarAllowedItemIdentifiers.addObject_(NSToolbarSpaceItemIdentifier)
        self._toolbarAllowedItemIdentifiers.addObject_(NSToolbarFlexibleSpaceItemIdentifier)
        self._toolbarAllowedItemIdentifiers.addObject_(NSToolbarPrintItemIdentifier)
        self._toolbarAllowedItemIdentifiers.addObject_(kWSTPreferencesToolbarItemIdentifier)
        self._toolbarAllowedItemIdentifiers.addObject_(NSToolbarCustomizeToolbarItemIdentifier)
        
    def toolbarDefaultItemIdentifiers_(self, anIdentifier):
        """
        Return an array of toolbar item identifiers that identify the
        set, in order, of items that should be displayed on the
        default toolbar.
        """
        return self._toolbarDefaultItemIdentifiers

    def toolbarAllowedItemIdentifiers_(self, anIdentifier):
        """
        Return an array of toolbar items that may be used in the toolbar.
        """
        return self._toolbarAllowedItemIdentifiers
        
    def toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_(self,
                                                                 toolbar,
                                                                 itemIdentifier, flag):
        """
        Delegate method fired when the toolbar is about to insert an
        item into the toolbar.  Item is identified by itemIdentifier.

        Effectively makes a copy of the cached reference instance of
        the toolbar item identified by itemIdentifier.
        """
        newItem = NSToolbarItem.alloc().initWithItemIdentifier_(itemIdentifier)
        item = self._toolbarItems.objectForKey_(itemIdentifier)
        
        newItem.setLabel_( item.label() )
        newItem.setPaletteLabel_( item.paletteLabel() )
        if item.view():
            newItem.setView_( item.view() )
        else:
            newItem.setImage_( item.image() )
            
        newItem.setToolTip_( item.toolTip() )
        newItem.setTarget_( item.target() )
        newItem.setAction_( item.action() )
        newItem.setMenuFormRepresentation_( item.menuFormRepresentation() )
        
        if newItem.view():
            newItem.setMinSize_( item.minSize() )
            newItem.setMaxSize_( item.maxSize() )
        
        return newItem  
        
    def setStatusTextFieldMessage_(self, aMessage):
        """
        Sets the contents of the statusTextField to aMessage and
        forces the fileld's contents to be redisplayed.
        """
        if not aMessage:
            aMessage = "Displaying information about %d methods." % len(self._methods)
        self.statusTextField.setStringValue_(aMessage)
        self.statusTextField.display()

    def reloadVisibleData_(self, sender):
        """
        Reloads the list of methods and their signatures from the
        XML-RPC server specified in the urlTextField.  Displays
        appropriate error messages, if necessary.
        """
        url = self.urlTextField.stringValue()
        self._methods = []
        self._methodSignatures = {}
        self._methodDescriptions = {}
        
        if url and len(url):
            self._server = xmlrpclib.ServerProxy(url)
            self.progressIndicator.startAnimation_(sender)
            self.setStatusTextFieldMessage_("Retrieving method list...")
            try:
                self._methods = self._server.listMethods()
                self._methodPrefix = ""
            except:
                try:
                    self._methods = self._server.system.listMethods()
                    self._methodPrefix = "system."
                except:
                    self.setStatusTextFieldMessage_("Server failed to respond to listMethods query.  See below for more information.")
                    self.progressIndicator.stopAnimation_(sender)
                    self._server = None
                    self._methodPrefix = None
                    
                    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                    self.methodDescriptionTextView.setString_("Exception information\n\nType: %s\n\nValue: %s\n\nTraceback:\n\n %s\n" % (exceptionType, exceptionValue, string.join(traceback.format_tb( exceptionTraceback ), '\n' )))
                    
                    return
                    
            self._methods.sort(lambda x, y: cmp(x, y))
            self.methodsTable.reloadData()
            self.methodsTable.display()
            self.setStatusTextFieldMessage_("Retrieving information about %d methods." % len(self._methods))
            self.window().setTitle_(url)
            NSUserDefaults.standardUserDefaults().setObject_forKey_(url, "LastURL")
            
            index = 0
            for aMethod in self._methods:
                index = index + 1
                if not (index % 5):
                    self.methodsTable.reloadData()
                    self.methodsTable.display()
                self.setStatusTextFieldMessage_("Retrieving signature for method %s (%d of %d)." % (aMethod , index, len(self._methods)))
                methodSignature = getattr(self._server, self._methodPrefix + "methodSignature")(aMethod)
                signatures = None
                if not len(methodSignature):
                    continue
                for aSignature in methodSignature:
                    if (type(aSignature) == types.ListType) and (len(aSignature) > 0):
                        signature = "%s %s(%s)" % (aSignature[0], aMethod, string.join(aSignature[1:], ", "))
                    else:
                        signature = aSignature
                if signatures:
                    signatures = signatures + ", " + signature
                else:
                    signatures = signature
                self._methodSignatures[aMethod] = signatures
            self.setStatusTextFieldMessage_(None)
            self.progressIndicator.stopAnimation_(sender)
            self.methodsTable.reloadData()
        else:
            self.window().setTitle_("Untitled.")
            self.setStatusTextFieldMessage_("No URL specified.")
    
    def selectMethodAction_(self, sender):
        """
        When the user selects a remote method, this method displays
        the documentation for that method as returned by the XML-RPC
        server.  If the method's documentation has been previously
        queried, the documentation will be retrieved from a cache.
        """
        selectedRow = self.methodsTable.selectedRow()
        selectedMethod = self._methods[selectedRow]
        
        if  not self._methodDescriptions.has_key(selectedMethod):
            self.progressIndicator.startAnimation_(sender)
            self.setStatusTextFieldMessage_("Retrieving signature for method %s..." % selectedMethod)
            methodDescription = getattr(self._server, self._methodPrefix + "methodHelp")(selectedMethod)
            if not methodDescription:
                methodDescription = "No description available."
            self._methodDescriptions[selectedMethod] = methodDescription
            self.progressIndicator.stopAnimation_(sender)
        else:
            methodDescription = self._methodDescriptions[selectedMethod]
       
        self.setStatusTextFieldMessage_(None)
        self.methodDescriptionTextView.setString_(methodDescription)

    def numberOfRowsInTableView_(self, aTableView):
        """
        Returns the number of methods found on the server.
        """
        return len(self._methods)

    def tableView_objectValueForTableColumn_row_(self, aTableView, aTableColumn, rowIndex):
        """
        Returns either the raw method name or the method signature,
        depending on if a signature had been found on the server.
        """
        aMethod = self._methods[rowIndex]
        if self._methodSignatures.has_key(aMethod):
            return self._methodSignatures[aMethod]
        else:
            return aMethod

    ### adjust method decls to be in line with ObjC requirements
    connectionWindowController = selector(connectionWindowController, isClassMethod=1)
    """
    Declares that the method connectionWindowController is actually a
    class method.  This is the one piece of non-automatic glue
    required to make this class work.   If we used a more pythonic
    module level function to create instances of this class, this
    could easily be eliminated.
    """
