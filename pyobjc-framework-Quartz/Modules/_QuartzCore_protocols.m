/*
 * This file is generated by objective.metadata
 *
 * Last update: Fri May 15 15:22:17 2015
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1012
    p = PyObjC_IdToPython(@protocol(CAAnimationDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CALayerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CALayoutManager)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIImageProcessorInput)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIImageProcessorOutput)); Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1012 */
}
