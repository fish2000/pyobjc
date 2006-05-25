/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 * Copyright (c) 2003 Ronald Oussoren
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: objc_support.h,v
 * Revision: 1.16
 * Date: 1998/08/18 15:35:57
 *
 * Created Tue Sep 10 14:11:38 1996.
 */

#ifndef PyObjC_RUNTIME_APPLE_H
#define PyObjC_RUNTIME_APPLE_H

#import <Foundation/NSObject.h>
#import <Foundation/NSString.h>

#include <objc/objc-runtime.h>
#include <objc/Protocol.h>

static inline int 
PyObjCRT_SameSEL(SEL a, SEL b)
{
	return a == b;
}

static inline const char* 
PyObjCRT_SELName(SEL sel)
{
	return sel_getName(sel);
}

static inline SEL 
PyObjCRT_SELUID(const char* str)
{
	return sel_getUid(str);
}

static inline Class 
PyObjCRT_LookUpClass(const char* name)
{
	return objc_lookUpClass(name);
}

static inline struct objc_method_list *
PyObjCRT_NextMethodList(Class c, void ** p)
{
	return class_nextMethodList(c, p);
}

static inline void 
PyObjCRT_InitMethod(Method m, SEL name, const char* types, IMP imp)
{
	memset(m, 0, sizeof(*m));
	m->method_name = name;
	m->method_types = strdup((char*)types);
	m->method_imp = imp;
}

static inline void
PyObjCRT_ClassAddMethodList(Class cls, struct objc_method_list* lst)
{
	class_addMethods(cls, lst);
}


extern struct objc_method_list* PyObjCRT_AllocMethodList(Py_ssize_t);
extern struct objc_protocol_list* PyObjCRT_AllocProtocolList(Py_ssize_t);

typedef Method PyObjCRT_Method_t;
typedef Ivar PyObjCRT_Ivar_t;

#define GETISA(c)       ((c)->isa)

#define RECEIVER(c)     ((c).receiver)

#define _C_CONST    'r'
#define _C_IN       'n'
#define _C_INOUT    'N'
#define _C_OUT      'o'
#define _C_BYCOPY   'O'
#define _C_ONEWAY   'V'
#define _C_LNGLNG   'q'
#define _C_ULNGLNG  'Q'
#define _C_BOOL	    'B'		/* (Objective-)C++ 'bool' */


/* Return a number that is likely to change when the method list changes,
 * and is cheap to compute.
 */
static inline int
objc_methodlist_magic(Class cls)
{
  int res = 0; 
  int cnt = 0;
    
  /* This is the documented way of enumerating the method list.  It
   * is slower than the obvious way, but does not explode under
   * esoteric situations.
   */ 
  void *iterator = NULL;
  struct objc_method_list *mlist;

  if (cls == NULL) return -1;

  while ( (mlist = class_nextMethodList( cls, &iterator )) != NULL ) {
    res += mlist->method_count;
    cnt++;
  }

  return (cnt << 16) | (res & 0xFFFF);
}

static inline const char *
get_selector_encoding (id self, SEL sel)
{
	struct objc_method* m = class_getInstanceMethod(self->isa, sel);

	if (!m) {
		return NULL;
	} else {
		return m->method_types;
	}
}

#endif /* PyObjC_RUNTIME_APPLE_H */
