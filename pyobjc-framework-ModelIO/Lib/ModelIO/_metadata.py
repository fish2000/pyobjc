# This file is generated by objective.metadata
#
# Last update: Wed Nov  2 10:22:10 2016

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
constants = '''$MDLVertexAttributeAnisotropy$MDLVertexAttributeBinormal$MDLVertexAttributeBitangent$MDLVertexAttributeColor$MDLVertexAttributeEdgeCrease$MDLVertexAttributeJointIndices$MDLVertexAttributeJointWeights$MDLVertexAttributeNormal$MDLVertexAttributeOcclusionValue$MDLVertexAttributePosition$MDLVertexAttributeShadingBasisU$MDLVertexAttributeShadingBasisV$MDLVertexAttributeSubdivisionStencil$MDLVertexAttributeTangent$MDLVertexAttributeTextureCoordinate$kUTType3dObject$kUTTypeAlembic$kUTTypePolygon$kUTTypeStereolithography$kUTTypeUniversalSceneDescription$'''
enums = '''$MDLCameraProjectionOrthographic@1$MDLCameraProjectionPerspective@0$MDLGeometryTypeLines@1$MDLGeometryTypePoints@0$MDLGeometryTypeQuads@4$MDLGeometryTypeTriangleStrips@3$MDLGeometryTypeTriangles@2$MDLGeometryTypeVariableTopology@5$MDLIndexBitDepthInvalid@0$MDLIndexBitDepthUInt16@16$MDLIndexBitDepthUInt32@32$MDLIndexBitDepthUInt8@8$MDLIndexBitDepthUint16@16$MDLIndexBitDepthUint32@32$MDLIndexBitDepthUint8@8$MDLLightTypeAmbient@1$MDLLightTypeDirectional@2$MDLLightTypeDiscArea@6$MDLLightTypeEnvironment@11$MDLLightTypeLinear@5$MDLLightTypePhotometric@9$MDLLightTypePoint@4$MDLLightTypeProbe@10$MDLLightTypeRectangularArea@7$MDLLightTypeSpot@3$MDLLightTypeSuperElliptical@8$MDLLightTypeUnknown@0$MDLMaterialFaceBack@1$MDLMaterialFaceDoubleSided@2$MDLMaterialFaceFront@0$MDLMaterialMipMapFilterModeLinear@1$MDLMaterialMipMapFilterModeNearest@0$MDLMaterialPropertyTypeColor@4$MDLMaterialPropertyTypeFloat@5$MDLMaterialPropertyTypeFloat2@6$MDLMaterialPropertyTypeFloat3@7$MDLMaterialPropertyTypeFloat4@8$MDLMaterialPropertyTypeMatrix44@9$MDLMaterialPropertyTypeNone@0$MDLMaterialPropertyTypeString@1$MDLMaterialPropertyTypeTexture@3$MDLMaterialPropertyTypeURL@2$MDLMaterialSemanticAmbientOcclusion@22$MDLMaterialSemanticAmbientOcclusionScale@23$MDLMaterialSemanticAnisotropic@7$MDLMaterialSemanticAnisotropicRotation@8$MDLMaterialSemanticBaseColor@0$MDLMaterialSemanticBump@14$MDLMaterialSemanticClearcoat@11$MDLMaterialSemanticClearcoatGloss@12$MDLMaterialSemanticDisplacement@20$MDLMaterialSemanticDisplacementScale@21$MDLMaterialSemanticEmission@13$MDLMaterialSemanticInterfaceIndexOfRefraction@16$MDLMaterialSemanticMaterialIndexOfRefraction@17$MDLMaterialSemanticMetallic@2$MDLMaterialSemanticNone@32768$MDLMaterialSemanticObjectSpaceNormal@18$MDLMaterialSemanticOpacity@15$MDLMaterialSemanticRoughness@6$MDLMaterialSemanticSheen@9$MDLMaterialSemanticSheenTint@10$MDLMaterialSemanticSpecular@3$MDLMaterialSemanticSpecularExponent@4$MDLMaterialSemanticSpecularTint@5$MDLMaterialSemanticSubsurface@1$MDLMaterialSemanticTangentSpaceNormal@19$MDLMaterialSemanticUserDefined@32769$MDLMaterialTextureFilterModeLinear@1$MDLMaterialTextureFilterModeNearest@0$MDLMaterialTextureWrapModeClamp@0$MDLMaterialTextureWrapModeMirror@2$MDLMaterialTextureWrapModeRepeat@1$MDLMeshBufferTypeIndex@2$MDLMeshBufferTypeVertex@1$MDLProbePlacementIrradianceDistribution@1$MDLProbePlacementUniformGrid@0$MDLTextureChannelEncodingFloat16@258$MDLTextureChannelEncodingFloat32@260$MDLTextureChannelEncodingUInt16@2$MDLTextureChannelEncodingUInt24@3$MDLTextureChannelEncodingUInt32@4$MDLTextureChannelEncodingUInt8@1$MDLTextureChannelEncodingUint16@2$MDLTextureChannelEncodingUint24@3$MDLTextureChannelEncodingUint32@4$MDLTextureChannelEncodingUint8@1$MDLVertexFormatChar@131073$MDLVertexFormatChar2@131074$MDLVertexFormatChar2Normalized@262146$MDLVertexFormatChar3@131075$MDLVertexFormatChar3Normalized@262147$MDLVertexFormatChar4@131076$MDLVertexFormatChar4Normalized@262148$MDLVertexFormatCharBits@131072$MDLVertexFormatCharNormalized@262145$MDLVertexFormatCharNormalizedBits@262144$MDLVertexFormatFloat@786433$MDLVertexFormatFloat2@786434$MDLVertexFormatFloat3@786435$MDLVertexFormatFloat4@786436$MDLVertexFormatFloatBits@786432$MDLVertexFormatHalf@720897$MDLVertexFormatHalf2@720898$MDLVertexFormatHalf3@720899$MDLVertexFormatHalf4@720900$MDLVertexFormatHalfBits@720896$MDLVertexFormatInt@655361$MDLVertexFormatInt1010102Normalized@659460$MDLVertexFormatInt2@655362$MDLVertexFormatInt3@655363$MDLVertexFormatInt4@655364$MDLVertexFormatIntBits@655360$MDLVertexFormatInvalid@0$MDLVertexFormatPackedBit@4096$MDLVertexFormatShort@393217$MDLVertexFormatShort2@393218$MDLVertexFormatShort2Normalized@524290$MDLVertexFormatShort3@393219$MDLVertexFormatShort3Normalized@524291$MDLVertexFormatShort4@393220$MDLVertexFormatShort4Normalized@524292$MDLVertexFormatShortBits@393216$MDLVertexFormatShortNormalized@524289$MDLVertexFormatShortNormalizedBits@524288$MDLVertexFormatUChar@65537$MDLVertexFormatUChar2@65538$MDLVertexFormatUChar2Normalized@196610$MDLVertexFormatUChar3@65539$MDLVertexFormatUChar3Normalized@196611$MDLVertexFormatUChar4@65540$MDLVertexFormatUChar4Normalized@196612$MDLVertexFormatUCharBits@65536$MDLVertexFormatUCharNormalized@196609$MDLVertexFormatUCharNormalizedBits@196608$MDLVertexFormatUInt@589825$MDLVertexFormatUInt1010102Normalized@593924$MDLVertexFormatUInt2@589826$MDLVertexFormatUInt3@589827$MDLVertexFormatUInt4@589828$MDLVertexFormatUIntBits@589824$MDLVertexFormatUShort@327681$MDLVertexFormatUShort2@327682$MDLVertexFormatUShort2Normalized@458754$MDLVertexFormatUShort3@327683$MDLVertexFormatUShort3Normalized@458755$MDLVertexFormatUShort4@327684$MDLVertexFormatUShort4Normalized@458756$MDLVertexFormatUShortBits@327680$MDLVertexFormatUShortNormalized@458753$MDLVertexFormatUShortNormalizedBits@458752$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'MDLAsset', b'canExportFileExtension:', {'retval': {'type': 'Z'}})
    r(b'MDLAsset', b'canImportFileExtension:', {'retval': {'type': 'Z'}})
    r(b'MDLAsset', b'exportAssetToURL:', {'retval': {'type': 'Z'}})
    r(b'MDLAsset', b'exportAssetToURL:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'MDLAsset', b'initWithURL:vertexDescriptor:bufferAllocator:preserveTopology:error:', {'arguments': {5: {'type': 'Z'}, 6: {'type_modifier': b'o'}}})
    r(b'MDLCamera', b'frameBoundingBox:setNearAndFar:', {'arguments': {3: {'type': 'Z'}}})
    r(b'MDLMaterialPropertyNode', b'evaluationFunction', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'MDLMaterialPropertyNode', b'initWithInputs:outputs:evaluationFunction:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'MDLMaterialPropertyNode', b'setEvaluationFunction:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'MDLMesh', b'generateAmbientOcclusionTextureWithQuality:attenuationFactor:objectsToConsider:vertexAttributeNamed:materialPropertyNamed:', {'retval': {'type': 'Z'}})
    r(b'MDLMesh', b'generateAmbientOcclusionTextureWithSize:raysPerSample:attenuationFactor:objectsToConsider:vertexAttributeNamed:materialPropertyNamed:', {'retval': {'type': 'Z'}})
    r(b'MDLMesh', b'generateAmbientOcclusionVertexColorsWithQuality:attenuationFactor:objectsToConsider:vertexAttributeNamed:', {'retval': {'type': 'Z'}})
    r(b'MDLMesh', b'generateAmbientOcclusionVertexColorsWithRaysPerSample:attenuationFactor:objectsToConsider:vertexAttributeNamed:', {'retval': {'type': 'Z'}})
    r(b'MDLMesh', b'generateLightMapTextureWithQuality:lightsToCondider:objectsToConsider:vertexAttributeNamed:materialPropertyNamed:', {'retval': {'type': 'Z'}})
    r(b'MDLMesh', b'generateLightMapTextureWithTextureSize:lightsToCondider:objectsToConsider:vertexAttributeNamed:materialPropertyNamed:', {'retval': {'type': 'Z'}})
    r(b'MDLMesh', b'generateLightMapVertexColorsWithLightsToConsider:objectsToConsider:vertexAttributeNamed:', {'retval': {'type': 'Z'}})
    r(b'MDLMesh', b'initBoxWithExtent:segments:inwardNormals:geometryType:allocator:', {'arguments': {4: {'type': 'Z'}}})
    r(b'MDLMesh', b'initCapsuleWithExtent:cylinderSegments:hemisphereSegments:inwardNormals:geometryType:allocator:', {'arguments': {5: {'type': 'Z'}}})
    r(b'MDLMesh', b'initConeWithExtent:segments:inwardNormals:cap:geometryType:allocator:', {'arguments': {4: {'type': 'Z'}, 5: {'type': 'Z'}}})
    r(b'MDLMesh', b'initCylinderWithExtent:segments:inwardNormals:topCap:bottomCap:cap:geometryType:allocator:', {'arguments': {4: {'type': 'Z'}, 5: {'type': 'Z'}, 6: {'type': 'Z'}}})
    r(b'MDLMesh', b'initHemisphereWithExtent:segments:inwardNormals:cap:geometryType:allocator:', {'arguments': {4: {'type': 'Z'}, 5: {'type': 'Z'}}})
    r(b'MDLMesh', b'initIcosahedronWithExtent:inwardNormals:segments:geometryType:allocator:', {'arguments': {3: {'type': 'Z'}}})
    r(b'MDLMesh', b'initSphereWithExtent:segments:inwardNormals:geometryType:allocator:', {'arguments': {4: {'type': 'Z'}}})
    r(b'MDLMesh', b'newBoxWithDimensions:segments:geometryType:inwardNormals:allocator:', {'arguments': {5: {'type': 'Z'}}})
    r(b'MDLMesh', b'newCylinderWithHeight:radii:radialSegments:verticalSegments:geometryType:inwardNormals:allocator:', {'arguments': {7: {'type': 'Z'}}})
    r(b'MDLMesh', b'newEllipsoidWithRadii:radialSegments:verticalSegments:geometryType:inwardNormals:hemisphere:allocator:', {'arguments': {6: {'type': 'Z'}, 7: {'type': 'Z'}}})
    r(b'MDLMesh', b'newEllipticalConeWithHeight:radii:radialSegments:verticalSegments:geometryType:inwardNormals:allocator:', {'arguments': {7: {'type': 'Z'}}})
    r(b'MDLMesh', b'newIcosahedronWithRadius:inwardNormals:allocator:', {'arguments': {3: {'type': 'Z'}}})
    r(b'MDLMeshBufferMap', b'bytes', {'retval': {'c_array_of_variable_length': True}})
    r(b'MDLMeshBufferMap', b'initWithBytes:deallocator:', {'arguments': {2: {'type_modifier': b'n', 'c_array_of_variable_length': True}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'MDLNoiseTexture', b'initScalarNoiseWithSmoothness:name:textureDimensions:channelCount:channelEncoding:grayScale:', {'arguments': {7: {'type': 'Z'}}})
    r(b'MDLObject', b'hidden', {'retval': {'type': 'Z'}})
    r(b'MDLObject', b'setHidden:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MDLTexture', b'hasAlphaValues', {'retval': {'type': 'Z'}})
    r(b'MDLTexture', b'initWithData:topLeftOrigin:name:dimensions:rowStride:channelCount:channelEncoding:isCube:', {'arguments': {3: {'type': 'Z'}, 9: {'type': 'Z'}}})
    r(b'MDLTexture', b'isCube', {'retval': {'type': 'Z'}})
    r(b'MDLTexture', b'setHasAlphaValues:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MDLTexture', b'setIsCube:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MDLTexture', b'texelDataWithBottomLeftOriginAtMipLevel:create:', {'arguments': {3: {'type': 'Z'}}})
    r(b'MDLTexture', b'texelDataWithTopLeftOriginAtMipLevel:create:', {'arguments': {3: {'type': 'Z'}}})
    r(b'MDLTexture', b'writeToURL:', {'retval': {'type': 'Z'}})
    r(b'MDLTexture', b'writeToURL:type:', {'retval': {'type': 'Z'}})
    r(b'MDLTransform', b'initWithMatrix:resetsTransform:', {'arguments': {3: {'type': 'Z'}}})
    r(b'MDLTransform', b'initWithTransformComponent:resetsTransform:', {'arguments': {3: {'type': 'Z'}}})
    r(b'MDLVertexAttributeData', b'dataStart', {'retval': {'c_array_of_variable_length': True}})
    r(b'MDLVertexAttributeData', b'setDataStart:', {'arguments': {2: {'c_array_of_variable_length': True}}})
    r(b'MDLVoxelArray', b'isValidSignedShellField', {'retval': {'type': 'Z'}})
    r(b'MDLVoxelArray', b'setIsValidSignedShellField:', {'arguments': {2: {'type': 'Z'}}})
    r(b'MDLVoxelArray', b'voxelExistsAtIndex:allowAnyX:allowAnyY:allowAnyZ:allowAnyShell:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': 'Z'}, 4: {'type': 'Z'}, 5: {'type': 'Z'}, 6: {'type': 'Z'}}})
    r(b'NSObject', b'capacity', {'retval': {'type': sel32or64(b'I', b'Q')}})
    r(b'NSObject', b'fillData:offset:', {'arguments': {3: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'globalTransformWithObject:atTime', {'arguments': {3: {'type': 'd'}}})
    r(b'NSObject', b'length', {'retval': {'type': sel32or64(b'I', b'Q')}})
    r(b'NSObject', b'localTransformAtTime:', {'arguments': {2: {'type': 'd'}}})
    r(b'NSObject', b'maximumTime', {'retval': {'type': 'd'}})
    r(b'NSObject', b'minimumTime', {'retval': {'type': 'd'}})
    r(b'NSObject', b'newBuffer:type:', {'arguments': {2: {'type': sel32or64(b'I', b'Q')}, 3: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'newBufferFromZone:data:type:', {'arguments': {4: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'newBufferFromZone:length:type:', {'arguments': {3: {'type': sel32or64(b'I', b'Q')}, 4: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'newBufferWithData:type:', {'arguments': {3: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'newZone:', {'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'resetsTransform', {'retval': {'type': 'Z'}})
    r(b'NSObject', b'setLocalTransform:forTime:', {'arguments': {3: {'type': 'd'}}})
    r(b'NSObject', b'setMaximumTime:', {'arguments': {2: {'type': 'd'}}})
    r(b'NSObject', b'setMinimumTime:', {'arguments': {2: {'type': 'd'}}})
    r(b'NSObject', b'setResetsTransform:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NSObject', b'setSphericalHarmonicsLevel:', {'arguments': {2: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'sphericalHarmonicsLevel', {'retval': {'type': sel32or64(b'I', b'Q')}})
    r(b'NSObject', b'type', {'retval': {'type': sel32or64(b'I', b'Q')}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
