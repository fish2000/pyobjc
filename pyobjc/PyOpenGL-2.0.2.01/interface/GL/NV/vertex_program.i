/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module vertex_program

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.NV.vertex_program Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_NV_vertex_program)
DECLARE_EXT(glAreProgramsResidentNV, GLboolean, 0, (GLsizei n, const GLuint *programs, GLboolean *residences), (n, programs, residences))
DECLARE_VOID_EXT(glBindProgramNV, (GLenum target, GLuint id), (target, id))
DECLARE_VOID_EXT(glDeleteProgramsNV, (GLsizei n, const GLuint *programs), (n, programs))
DECLARE_VOID_EXT(glExecuteProgramNV, (GLenum target, GLuint id, const GLfloat *params), (target, id, params))
DECLARE_VOID_EXT(glGenProgramsNV, (GLsizei n, GLuint *programs), (n, programs))
DECLARE_VOID_EXT(glGetProgramParameterdvNV, (GLenum target, GLuint index, GLenum pname, GLdouble *params), (target, index, pname, params))
DECLARE_VOID_EXT(glGetProgramParameterfvNV, (GLenum target, GLuint index, GLenum pname, GLfloat *params), (target, index, pname, params))
DECLARE_VOID_EXT(glGetProgramivNV, (GLuint id, GLenum pname, GLint *params), (id, pname, params))
DECLARE_VOID_EXT(glGetProgramStringNV, (GLuint id, GLenum pname, GLubyte *program), (id, pname, program))
DECLARE_VOID_EXT(glGetTrackMatrixivNV, (GLenum target, GLuint address, GLenum pname, GLint *params), (target, address, pname, params))
DECLARE_VOID_EXT(glGetVertexAttribdvNV, (GLuint index, GLenum pname, GLdouble *params), (index, pname, params))
DECLARE_VOID_EXT(glGetVertexAttribfvNV, (GLuint index, GLenum pname, GLfloat *params), (index, pname, params))
DECLARE_VOID_EXT(glGetVertexAttribivNV, (GLuint index, GLenum pname, GLint *params), (index, pname, params))
DECLARE_VOID_EXT(glGetVertexAttribPointervNV, (GLuint index, GLenum pname, GLvoid* *pointer), (index, pname, pointer))
DECLARE_EXT(glIsProgramNV, GLboolean, 0, (GLuint id), (id))
DECLARE_VOID_EXT(glLoadProgramNV, (GLenum target, GLuint id, GLsizei len, const GLubyte *program), (target, id, len, program))
DECLARE_VOID_EXT(glProgramParameter4dNV, (GLenum target, GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w), (target, index, x, y, z, w))
DECLARE_VOID_EXT(glProgramParameter4dvNV, (GLenum target, GLuint index, const GLdouble *v), (target, index, v))
DECLARE_VOID_EXT(glProgramParameter4fNV, (GLenum target, GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w), (target, index, x, y, z, w))
DECLARE_VOID_EXT(glProgramParameter4fvNV, (GLenum target, GLuint index, const GLfloat *v), (target, index, v))
DECLARE_VOID_EXT(glProgramParameters4dvNV, (GLenum target, GLuint index, GLuint count, const GLdouble *v), (target, index, count, v))
DECLARE_VOID_EXT(glProgramParameters4fvNV, (GLenum target, GLuint index, GLuint count, const GLfloat *v), (target, index, count, v))
DECLARE_VOID_EXT(glRequestResidentProgramsNV, (GLsizei n, const GLuint *programs), (n, programs))
DECLARE_VOID_EXT(glTrackMatrixNV, (GLenum target, GLuint address, GLenum matrix, GLenum transform), (target, address, matrix, transform))
DECLARE_VOID_EXT(glVertexAttribPointerNV, (GLuint index, GLint fsize, GLenum type, GLsizei stride, const GLvoid *pointer), (index, fsize, type, stride, pointer))
DECLARE_VOID_EXT(glVertexAttrib1dNV, (GLuint index, GLdouble x), (index, x))
DECLARE_VOID_EXT(glVertexAttrib1dvNV, (GLuint index, const GLdouble *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib1fNV, (GLuint index, GLfloat x), (index, x))
DECLARE_VOID_EXT(glVertexAttrib1fvNV, (GLuint index, const GLfloat *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib1sNV, (GLuint index, GLshort x), (index, x))
DECLARE_VOID_EXT(glVertexAttrib1svNV, (GLuint index, const GLshort *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib2dNV, (GLuint index, GLdouble x, GLdouble y), (index, x, y))
DECLARE_VOID_EXT(glVertexAttrib2dvNV, (GLuint index, const GLdouble *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib2fNV, (GLuint index, GLfloat x, GLfloat y), (index, x, y))
DECLARE_VOID_EXT(glVertexAttrib2fvNV, (GLuint index, const GLfloat *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib2sNV, (GLuint index, GLshort x, GLshort y), (index, x, y))
DECLARE_VOID_EXT(glVertexAttrib2svNV, (GLuint index, const GLshort *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib3dNV, (GLuint index, GLdouble x, GLdouble y, GLdouble z), (index, x, y, z))
DECLARE_VOID_EXT(glVertexAttrib3dvNV, (GLuint index, const GLdouble *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib3fNV, (GLuint index, GLfloat x, GLfloat y, GLfloat z), (index, x, y, z))
DECLARE_VOID_EXT(glVertexAttrib3fvNV, (GLuint index, const GLfloat *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib3sNV, (GLuint index, GLshort x, GLshort y, GLshort z), (index, x, y, z))
DECLARE_VOID_EXT(glVertexAttrib3svNV, (GLuint index, const GLshort *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib4dNV, (GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w), (index, x, y, z, w))
DECLARE_VOID_EXT(glVertexAttrib4dvNV, (GLuint index, const GLdouble *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib4fNV, (GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w), (index, x, y, z, w))
DECLARE_VOID_EXT(glVertexAttrib4fvNV, (GLuint index, const GLfloat *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib4sNV, (GLuint index, GLshort x, GLshort y, GLshort z, GLshort w), (index, x, y, z, w))
DECLARE_VOID_EXT(glVertexAttrib4svNV, (GLuint index, const GLshort *v), (index, v))
DECLARE_VOID_EXT(glVertexAttrib4ubNV, (GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w), (index, x, y, z, w))
DECLARE_VOID_EXT(glVertexAttrib4ubvNV, (GLuint index, const GLubyte *v), (index, v))
DECLARE_VOID_EXT(glVertexAttribs1dvNV, (GLuint index, GLsizei count, const GLdouble *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs1fvNV, (GLuint index, GLsizei count, const GLfloat *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs1svNV, (GLuint index, GLsizei count, const GLshort *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs2dvNV, (GLuint index, GLsizei count, const GLdouble *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs2fvNV, (GLuint index, GLsizei count, const GLfloat *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs2svNV, (GLuint index, GLsizei count, const GLshort *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs3dvNV, (GLuint index, GLsizei count, const GLdouble *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs3fvNV, (GLuint index, GLsizei count, const GLfloat *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs3svNV, (GLuint index, GLsizei count, const GLshort *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs4dvNV, (GLuint index, GLsizei count, const GLdouble *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs4fvNV, (GLuint index, GLsizei count, const GLfloat *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs4svNV, (GLuint index, GLsizei count, const GLshort *v), (index, count, v))
DECLARE_VOID_EXT(glVertexAttribs4ubvNV, (GLuint index, GLsizei count, const GLubyte *v), (index, count, v))
#endif
%}

/* FUNCTION DECLARATIONS */
GLboolean glAreProgramsResidentNV(GLsizei n, const GLuint *programs, GLboolean *residences);
DOC(glAreProgramsResidentNV, "glAreProgramsResidentNV(n, programs, residences)")
void glBindProgramNV(GLenum target, GLuint id);
DOC(glBindProgramNV, "glBindProgramNV(target, id)")
void glDeleteProgramsNV(GLsizei n, const GLuint *programs);
DOC(glDeleteProgramsNV, "glDeleteProgramsNV(n, programs)")
void glExecuteProgramNV(GLenum target, GLuint id, const GLfloat *params);
DOC(glExecuteProgramNV, "glExecuteProgramNV(target, id, params)")
void glGenProgramsNV(GLsizei n, GLuint *programs);
DOC(glGenProgramsNV, "glGenProgramsNV(n, programs)")
void glGetProgramParameterdvNV(GLenum target, GLuint index, GLenum pname, GLdouble *params);
DOC(glGetProgramParameterdvNV, "glGetProgramParameterdvNV(target, index, pname, params)")
void glGetProgramParameterfvNV(GLenum target, GLuint index, GLenum pname, GLfloat *params);
DOC(glGetProgramParameterfvNV, "glGetProgramParameterfvNV(target, index, pname, params)")
void glGetProgramivNV(GLuint id, GLenum pname, GLint *params);
DOC(glGetProgramivNV, "glGetProgramivNV(id, pname, params)")
void glGetProgramStringNV(GLuint id, GLenum pname, GLubyte *program);
DOC(glGetProgramStringNV, "glGetProgramStringNV(id, pname, program)")
void glGetTrackMatrixivNV(GLenum target, GLuint address, GLenum pname, GLint *params);
DOC(glGetTrackMatrixivNV, "glGetTrackMatrixivNV(target, address, pname, params)")
void glGetVertexAttribdvNV(GLuint index, GLenum pname, GLdouble *params);
DOC(glGetVertexAttribdvNV, "glGetVertexAttribdvNV(index, pname, params)")
void glGetVertexAttribfvNV(GLuint index, GLenum pname, GLfloat *params);
DOC(glGetVertexAttribfvNV, "glGetVertexAttribfvNV(index, pname, params)")
void glGetVertexAttribivNV(GLuint index, GLenum pname, GLint *params);
DOC(glGetVertexAttribivNV, "glGetVertexAttribivNV(index, pname, params)")
void glGetVertexAttribPointervNV(GLuint index, GLenum pname, GLvoid* *pointer);
DOC(glGetVertexAttribPointervNV, "glGetVertexAttribPointervNV(index, pname, pointer)")
GLboolean glIsProgramNV(GLuint id);
DOC(glIsProgramNV, "glIsProgramNV(id)")
void glLoadProgramNV(GLenum target, GLuint id, GLsizei len, const GLubyte *program);
DOC(glLoadProgramNV, "glLoadProgramNV(target, id, len, program)")
void glProgramParameter4dNV(GLenum target, GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w);
DOC(glProgramParameter4dNV, "glProgramParameter4dNV(target, index, x, y, z, w)")
void glProgramParameter4dvNV(GLenum target, GLuint index, const GLdouble *v);
DOC(glProgramParameter4dvNV, "glProgramParameter4dvNV(target, index, v)")
void glProgramParameter4fNV(GLenum target, GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w);
DOC(glProgramParameter4fNV, "glProgramParameter4fNV(target, index, x, y, z, w)")
void glProgramParameter4fvNV(GLenum target, GLuint index, const GLfloat *v);
DOC(glProgramParameter4fvNV, "glProgramParameter4fvNV(target, index, v)")
void glProgramParameters4dvNV(GLenum target, GLuint index, GLuint count, const GLdouble *v);
DOC(glProgramParameters4dvNV, "glProgramParameters4dvNV(target, index, count, v)")
void glProgramParameters4fvNV(GLenum target, GLuint index, GLuint count, const GLfloat *v);
DOC(glProgramParameters4fvNV, "glProgramParameters4fvNV(target, index, count, v)")
void glRequestResidentProgramsNV(GLsizei n, const GLuint *programs);
DOC(glRequestResidentProgramsNV, "glRequestResidentProgramsNV(n, programs)")
void glTrackMatrixNV(GLenum target, GLuint address, GLenum matrix, GLenum transform);
DOC(glTrackMatrixNV, "glTrackMatrixNV(target, address, matrix, transform)")
void glVertexAttribPointerNV(GLuint index, GLint fsize, GLenum type, GLsizei stride, const GLvoid *pointer);
DOC(glVertexAttribPointerNV, "glVertexAttribPointerNV(index, fsize, type, stride, pointer)")
void glVertexAttrib1dNV(GLuint index, GLdouble x);
DOC(glVertexAttrib1dNV, "glVertexAttrib1dNV(index, x)")
void glVertexAttrib1dvNV(GLuint index, const GLdouble *v);
DOC(glVertexAttrib1dvNV, "glVertexAttrib1dvNV(index, v)")
void glVertexAttrib1fNV(GLuint index, GLfloat x);
DOC(glVertexAttrib1fNV, "glVertexAttrib1fNV(index, x)")
void glVertexAttrib1fvNV(GLuint index, const GLfloat *v);
DOC(glVertexAttrib1fvNV, "glVertexAttrib1fvNV(index, v)")
void glVertexAttrib1sNV(GLuint index, GLshort x);
DOC(glVertexAttrib1sNV, "glVertexAttrib1sNV(index, x)")
void glVertexAttrib1svNV(GLuint index, const GLshort *v);
DOC(glVertexAttrib1svNV, "glVertexAttrib1svNV(index, v)")
void glVertexAttrib2dNV(GLuint index, GLdouble x, GLdouble y);
DOC(glVertexAttrib2dNV, "glVertexAttrib2dNV(index, x, y)")
void glVertexAttrib2dvNV(GLuint index, const GLdouble *v);
DOC(glVertexAttrib2dvNV, "glVertexAttrib2dvNV(index, v)")
void glVertexAttrib2fNV(GLuint index, GLfloat x, GLfloat y);
DOC(glVertexAttrib2fNV, "glVertexAttrib2fNV(index, x, y)")
void glVertexAttrib2fvNV(GLuint index, const GLfloat *v);
DOC(glVertexAttrib2fvNV, "glVertexAttrib2fvNV(index, v)")
void glVertexAttrib2sNV(GLuint index, GLshort x, GLshort y);
DOC(glVertexAttrib2sNV, "glVertexAttrib2sNV(index, x, y)")
void glVertexAttrib2svNV(GLuint index, const GLshort *v);
DOC(glVertexAttrib2svNV, "glVertexAttrib2svNV(index, v)")
void glVertexAttrib3dNV(GLuint index, GLdouble x, GLdouble y, GLdouble z);
DOC(glVertexAttrib3dNV, "glVertexAttrib3dNV(index, x, y, z)")
void glVertexAttrib3dvNV(GLuint index, const GLdouble *v);
DOC(glVertexAttrib3dvNV, "glVertexAttrib3dvNV(index, v)")
void glVertexAttrib3fNV(GLuint index, GLfloat x, GLfloat y, GLfloat z);
DOC(glVertexAttrib3fNV, "glVertexAttrib3fNV(index, x, y, z)")
void glVertexAttrib3fvNV(GLuint index, const GLfloat *v);
DOC(glVertexAttrib3fvNV, "glVertexAttrib3fvNV(index, v)")
void glVertexAttrib3sNV(GLuint index, GLshort x, GLshort y, GLshort z);
DOC(glVertexAttrib3sNV, "glVertexAttrib3sNV(index, x, y, z)")
void glVertexAttrib3svNV(GLuint index, const GLshort *v);
DOC(glVertexAttrib3svNV, "glVertexAttrib3svNV(index, v)")
void glVertexAttrib4dNV(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w);
DOC(glVertexAttrib4dNV, "glVertexAttrib4dNV(index, x, y, z, w)")
void glVertexAttrib4dvNV(GLuint index, const GLdouble *v);
DOC(glVertexAttrib4dvNV, "glVertexAttrib4dvNV(index, v)")
void glVertexAttrib4fNV(GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w);
DOC(glVertexAttrib4fNV, "glVertexAttrib4fNV(index, x, y, z, w)")
void glVertexAttrib4fvNV(GLuint index, const GLfloat *v);
DOC(glVertexAttrib4fvNV, "glVertexAttrib4fvNV(index, v)")
void glVertexAttrib4sNV(GLuint index, GLshort x, GLshort y, GLshort z, GLshort w);
DOC(glVertexAttrib4sNV, "glVertexAttrib4sNV(index, x, y, z, w)")
void glVertexAttrib4svNV(GLuint index, const GLshort *v);
DOC(glVertexAttrib4svNV, "glVertexAttrib4svNV(index, v)")
void glVertexAttrib4ubNV(GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w);
DOC(glVertexAttrib4ubNV, "glVertexAttrib4ubNV(index, x, y, z, w)")
void glVertexAttrib4ubvNV(GLuint index, const GLubyte *v);
DOC(glVertexAttrib4ubvNV, "glVertexAttrib4ubvNV(index, v)")
void glVertexAttribs1dvNV(GLuint index, GLsizei count, const GLdouble *v);
DOC(glVertexAttribs1dvNV, "glVertexAttribs1dvNV(index, count, v)")
void glVertexAttribs1fvNV(GLuint index, GLsizei count, const GLfloat *v);
DOC(glVertexAttribs1fvNV, "glVertexAttribs1fvNV(index, count, v)")
void glVertexAttribs1svNV(GLuint index, GLsizei count, const GLshort *v);
DOC(glVertexAttribs1svNV, "glVertexAttribs1svNV(index, count, v)")
void glVertexAttribs2dvNV(GLuint index, GLsizei count, const GLdouble *v);
DOC(glVertexAttribs2dvNV, "glVertexAttribs2dvNV(index, count, v)")
void glVertexAttribs2fvNV(GLuint index, GLsizei count, const GLfloat *v);
DOC(glVertexAttribs2fvNV, "glVertexAttribs2fvNV(index, count, v)")
void glVertexAttribs2svNV(GLuint index, GLsizei count, const GLshort *v);
DOC(glVertexAttribs2svNV, "glVertexAttribs2svNV(index, count, v)")
void glVertexAttribs3dvNV(GLuint index, GLsizei count, const GLdouble *v);
DOC(glVertexAttribs3dvNV, "glVertexAttribs3dvNV(index, count, v)")
void glVertexAttribs3fvNV(GLuint index, GLsizei count, const GLfloat *v);
DOC(glVertexAttribs3fvNV, "glVertexAttribs3fvNV(index, count, v)")
void glVertexAttribs3svNV(GLuint index, GLsizei count, const GLshort *v);
DOC(glVertexAttribs3svNV, "glVertexAttribs3svNV(index, count, v)")
void glVertexAttribs4dvNV(GLuint index, GLsizei count, const GLdouble *v);
DOC(glVertexAttribs4dvNV, "glVertexAttribs4dvNV(index, count, v)")
void glVertexAttribs4fvNV(GLuint index, GLsizei count, const GLfloat *v);
DOC(glVertexAttribs4fvNV, "glVertexAttribs4fvNV(index, count, v)")
void glVertexAttribs4svNV(GLuint index, GLsizei count, const GLshort *v);
DOC(glVertexAttribs4svNV, "glVertexAttribs4svNV(index, count, v)")
void glVertexAttribs4ubvNV(GLuint index, GLsizei count, const GLubyte *v);
DOC(glVertexAttribs4ubvNV, "glVertexAttribs4ubvNV(index, count, v)")

/* CONSTANT DECLARATIONS */
#define           GL_VERTEX_PROGRAM_NV 0x8620
#define     GL_VERTEX_STATE_PROGRAM_NV 0x8621
#define        GL_ATTRIB_ARRAY_SIZE_NV 0x8623
#define      GL_ATTRIB_ARRAY_STRIDE_NV 0x8624
#define        GL_ATTRIB_ARRAY_TYPE_NV 0x8625
#define           GL_CURRENT_ATTRIB_NV 0x8626
#define           GL_PROGRAM_LENGTH_NV 0x8627
#define           GL_PROGRAM_STRING_NV 0x8628
#define     GL_MODELVIEW_PROJECTION_NV 0x8629
#define                 GL_IDENTITY_NV 0x862A
#define                  GL_INVERSE_NV 0x862B
#define                GL_TRANSPOSE_NV 0x862C
#define        GL_INVERSE_TRANSPOSE_NV 0x862D
#define GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV 0x862E
#define       GL_MAX_TRACK_MATRICES_NV 0x862F
#define                  GL_MATRIX0_NV 0x8630
#define                  GL_MATRIX1_NV 0x8631
#define                  GL_MATRIX2_NV 0x8632
#define                  GL_MATRIX3_NV 0x8633
#define                  GL_MATRIX4_NV 0x8634
#define                  GL_MATRIX5_NV 0x8635
#define                  GL_MATRIX6_NV 0x8636
#define                  GL_MATRIX7_NV 0x8637
#define GL_CURRENT_MATRIX_STACK_DEPTH_NV 0x8640
#define           GL_CURRENT_MATRIX_NV 0x8641
#define GL_VERTEX_PROGRAM_POINT_SIZE_NV 0x8642
#define  GL_VERTEX_PROGRAM_TWO_SIDE_NV 0x8643
#define        GL_PROGRAM_PARAMETER_NV 0x8644
#define     GL_ATTRIB_ARRAY_POINTER_NV 0x8645
#define           GL_PROGRAM_TARGET_NV 0x8646
#define         GL_PROGRAM_RESIDENT_NV 0x8647
#define             GL_TRACK_MATRIX_NV 0x8648
#define   GL_TRACK_MATRIX_TRANSFORM_NV 0x8649
#define   GL_VERTEX_PROGRAM_BINDING_NV 0x864A
#define   GL_PROGRAM_ERROR_POSITION_NV 0x864B
#define     GL_VERTEX_ATTRIB_ARRAY0_NV 0x8650
#define     GL_VERTEX_ATTRIB_ARRAY1_NV 0x8651
#define     GL_VERTEX_ATTRIB_ARRAY2_NV 0x8652
#define     GL_VERTEX_ATTRIB_ARRAY3_NV 0x8653
#define     GL_VERTEX_ATTRIB_ARRAY4_NV 0x8654
#define     GL_VERTEX_ATTRIB_ARRAY5_NV 0x8655
#define     GL_VERTEX_ATTRIB_ARRAY6_NV 0x8656
#define     GL_VERTEX_ATTRIB_ARRAY7_NV 0x8657
#define     GL_VERTEX_ATTRIB_ARRAY8_NV 0x8658
#define     GL_VERTEX_ATTRIB_ARRAY9_NV 0x8659
#define    GL_VERTEX_ATTRIB_ARRAY10_NV 0x865A
#define    GL_VERTEX_ATTRIB_ARRAY11_NV 0x865B
#define    GL_VERTEX_ATTRIB_ARRAY12_NV 0x865C
#define    GL_VERTEX_ATTRIB_ARRAY13_NV 0x865D
#define    GL_VERTEX_ATTRIB_ARRAY14_NV 0x865E
#define    GL_VERTEX_ATTRIB_ARRAY15_NV 0x865F
#define    GL_MAP1_VERTEX_ATTRIB0_4_NV 0x8660
#define    GL_MAP1_VERTEX_ATTRIB1_4_NV 0x8661
#define    GL_MAP1_VERTEX_ATTRIB2_4_NV 0x8662
#define    GL_MAP1_VERTEX_ATTRIB3_4_NV 0x8663
#define    GL_MAP1_VERTEX_ATTRIB4_4_NV 0x8664
#define    GL_MAP1_VERTEX_ATTRIB5_4_NV 0x8665
#define    GL_MAP1_VERTEX_ATTRIB6_4_NV 0x8666
#define    GL_MAP1_VERTEX_ATTRIB7_4_NV 0x8667
#define    GL_MAP1_VERTEX_ATTRIB8_4_NV 0x8668
#define    GL_MAP1_VERTEX_ATTRIB9_4_NV 0x8669
#define   GL_MAP1_VERTEX_ATTRIB10_4_NV 0x866A
#define   GL_MAP1_VERTEX_ATTRIB11_4_NV 0x866B
#define   GL_MAP1_VERTEX_ATTRIB12_4_NV 0x866C
#define   GL_MAP1_VERTEX_ATTRIB13_4_NV 0x866D
#define   GL_MAP1_VERTEX_ATTRIB14_4_NV 0x866E
#define   GL_MAP1_VERTEX_ATTRIB15_4_NV 0x866F
#define    GL_MAP2_VERTEX_ATTRIB0_4_NV 0x8670
#define    GL_MAP2_VERTEX_ATTRIB1_4_NV 0x8671
#define    GL_MAP2_VERTEX_ATTRIB2_4_NV 0x8672
#define    GL_MAP2_VERTEX_ATTRIB3_4_NV 0x8673
#define    GL_MAP2_VERTEX_ATTRIB4_4_NV 0x8674
#define    GL_MAP2_VERTEX_ATTRIB5_4_NV 0x8675
#define    GL_MAP2_VERTEX_ATTRIB6_4_NV 0x8676
#define    GL_MAP2_VERTEX_ATTRIB7_4_NV 0x8677
#define    GL_MAP2_VERTEX_ATTRIB8_4_NV 0x8678
#define    GL_MAP2_VERTEX_ATTRIB9_4_NV 0x8679
#define   GL_MAP2_VERTEX_ATTRIB10_4_NV 0x867A
#define   GL_MAP2_VERTEX_ATTRIB11_4_NV 0x867B
#define   GL_MAP2_VERTEX_ATTRIB12_4_NV 0x867C
#define   GL_MAP2_VERTEX_ATTRIB13_4_NV 0x867D
#define   GL_MAP2_VERTEX_ATTRIB14_4_NV 0x867E
#define   GL_MAP2_VERTEX_ATTRIB15_4_NV 0x867F


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_NV_vertex_program)
"glAreProgramsResidentNV",
"glBindProgramNV",
"glDeleteProgramsNV",
"glExecuteProgramNV",
"glGenProgramsNV",
"glGetProgramParameterdvNV",
"glGetProgramParameterfvNV",
"glGetProgramivNV",
"glGetProgramStringNV",
"glGetTrackMatrixivNV",
"glGetVertexAttribdvNV",
"glGetVertexAttribfvNV",
"glGetVertexAttribivNV",
"glGetVertexAttribPointervNV",
"glIsProgramNV",
"glLoadProgramNV",
"glProgramParameter4dNV",
"glProgramParameter4dvNV",
"glProgramParameter4fNV",
"glProgramParameter4fvNV",
"glProgramParameters4dvNV",
"glProgramParameters4fvNV",
"glRequestResidentProgramsNV",
"glTrackMatrixNV",
"glVertexAttribPointerNV",
"glVertexAttrib1dNV",
"glVertexAttrib1dvNV",
"glVertexAttrib1fNV",
"glVertexAttrib1fvNV",
"glVertexAttrib1sNV",
"glVertexAttrib1svNV",
"glVertexAttrib2dNV",
"glVertexAttrib2dvNV",
"glVertexAttrib2fNV",
"glVertexAttrib2fvNV",
"glVertexAttrib2sNV",
"glVertexAttrib2svNV",
"glVertexAttrib3dNV",
"glVertexAttrib3dvNV",
"glVertexAttrib3fNV",
"glVertexAttrib3fvNV",
"glVertexAttrib3sNV",
"glVertexAttrib3svNV",
"glVertexAttrib4dNV",
"glVertexAttrib4dvNV",
"glVertexAttrib4fNV",
"glVertexAttrib4fvNV",
"glVertexAttrib4sNV",
"glVertexAttrib4svNV",
"glVertexAttrib4ubNV",
"glVertexAttrib4ubvNV",
"glVertexAttribs1dvNV",
"glVertexAttribs1fvNV",
"glVertexAttribs1svNV",
"glVertexAttribs2dvNV",
"glVertexAttribs2fvNV",
"glVertexAttribs2svNV",
"glVertexAttribs3dvNV",
"glVertexAttribs3fvNV",
"glVertexAttribs3svNV",
"glVertexAttribs4dvNV",
"glVertexAttribs4fvNV",
"glVertexAttribs4svNV",
"glVertexAttribs4ubvNV",
#endif
	NULL
};

#define glInitVertexProgramNV() InitExtension("GL_NV_vertex_program", proc_names)
%}

int glInitVertexProgramNV();
DOC(glInitVertexProgramNV, "glInitVertexProgramNV() -> bool")

%{
PyObject *__info()
{
	if (glInitVertexProgramNV())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

