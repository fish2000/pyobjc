#! /usr/bin/python

import unittest
import objc

import Foundation
import CoreData

class Test (unittest.TestCase):
    def setUp(self):
	self.entity = CoreData.NSEntityDescription.new()
	self.entity.setName_('TestEntity')

	self.attribute = CoreData.NSAttributeDescription.new()
	self.attribute.setName_('testAttribute')
	self.attribute.setAttributeType_(CoreData.NSStringAttributeType)

	self.entity.setProperties_([self.attribute])

	self.managedObjectModel = CoreData.NSManagedObjectModel.new()
	self.managedObjectModel.setEntities_([self.entity])

	self.persistentStoreCoordinator = CoreData.NSPersistentStoreCoordinator.alloc().initWithManagedObjectModel_(self.managedObjectModel)
	self.persistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_(CoreData.NSInMemoryStoreType, None, None, None)

	self.managedObjectContext = CoreData.NSManagedObjectContext.new()
	self.managedObjectContext.setPersistentStoreCoordinator_(self.persistentStoreCoordinator)

    def testModeledAttribute(self):
	managedObject = CoreData.NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(self.entity, self.managedObjectContext)

	testValue = u'FooBarBaz'

	managedObject.setValue_forKey_(testValue, u'testAttribute')

	self.assertEquals(testValue, managedObject.valueForKey_(u'testAttribute'))
	self.assertEquals(testValue, managedObject.testAttribute)

	testValue = u'BobFred'
	managedObject.setValue_forKey_(testValue, u'testAttribute')

	self.assertEquals(testValue, managedObject.valueForKey_(u'testAttribute'))
	self.assertEquals(testValue, managedObject.testAttribute)

	testValue = u'Zebras have long legs.'
	managedObject.testAttribute = testValue

	self.assertEquals(testValue, managedObject.valueForKey_(u'testAttribute'))
	self.assertEquals(testValue, managedObject.testAttribute)

    def testPythonicAttribute(self):
	managedObject = CoreData.NSManagedObject.alloc().initWithEntity_insertIntoManagedObjectContext_(self.entity, self.managedObjectContext)

	testValue = u'Ducks have webbed feet'
        self.assertRaises(AttributeError, setattr, managedObject, 'attributeWithoutModel', testValue)
        return

        # XXX: this test is invalid, you cannot add arbitrary attributes
        # to an object that is fully implemented in ObjC.
	managedObject.attributeWithoutModel = testValue

	self.assertEquals(testValue, managedObject.attributeWithoutModel)
	
	self.assertRaises(Foundation.NSUnknownKeyException, managedObject.valueForKey_(u'attributeWithoutModel'))
	

if __name__ == "__main__":
    unittest.main()
