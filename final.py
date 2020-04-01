

def annotate():
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.axes2D.visible = 0
    AnnotationAtts.axes2D.autoSetTicks = 1
    AnnotationAtts.axes2D.autoSetScaling = 1
    AnnotationAtts.axes2D.lineWidth = 0
    AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
    AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.title.font.scale = 1
    AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.title.font.bold = 1
    AnnotationAtts.axes2D.xAxis.title.font.italic = 1
    AnnotationAtts.axes2D.xAxis.title.userTitle = 0
    AnnotationAtts.axes2D.xAxis.title.userUnits = 0
    AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
    AnnotationAtts.axes2D.xAxis.title.units = ""
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.label.font.scale = 1
    AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.label.font.bold = 1
    AnnotationAtts.axes2D.xAxis.label.font.italic = 1
    AnnotationAtts.axes2D.xAxis.label.scaling = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.xAxis.grid = 0
    AnnotationAtts.axes2D.yAxis.title.visible = 1
    AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.title.font.scale = 1
    AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.title.font.bold = 1
    AnnotationAtts.axes2D.yAxis.title.font.italic = 1
    AnnotationAtts.axes2D.yAxis.title.userTitle = 0
    AnnotationAtts.axes2D.yAxis.title.userUnits = 0
    AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
    AnnotationAtts.axes2D.yAxis.title.units = ""
    AnnotationAtts.axes2D.yAxis.label.visible = 1
    AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.label.font.scale = 1
    AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.label.font.bold = 1
    AnnotationAtts.axes2D.yAxis.label.font.italic = 1
    AnnotationAtts.axes2D.yAxis.label.scaling = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.yAxis.grid = 0
    AnnotationAtts.axes3D.visible = 0
    AnnotationAtts.axes3D.autoSetTicks = 1
    AnnotationAtts.axes3D.autoSetScaling = 1
    AnnotationAtts.axes3D.lineWidth = 0
    AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
    AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
    AnnotationAtts.axes3D.triadFlag = 0
    AnnotationAtts.axes3D.bboxFlag = 0
    AnnotationAtts.axes3D.xAxis.title.visible = 1
    AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.xAxis.title.font.scale = 1
    AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.xAxis.title.font.bold = 0
    AnnotationAtts.axes3D.xAxis.title.font.italic = 0
    AnnotationAtts.axes3D.xAxis.title.userTitle = 0
    AnnotationAtts.axes3D.xAxis.title.userUnits = 0
    AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
    AnnotationAtts.axes3D.xAxis.title.units = ""
    AnnotationAtts.axes3D.xAxis.label.visible = 1
    AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.xAxis.label.font.scale = 1
    AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.xAxis.label.font.bold = 0
    AnnotationAtts.axes3D.xAxis.label.font.italic = 0
    AnnotationAtts.axes3D.xAxis.label.scaling = 0
    AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.xAxis.grid = 0
    AnnotationAtts.axes3D.yAxis.title.visible = 1
    AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.yAxis.title.font.scale = 1
    AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.yAxis.title.font.bold = 0
    AnnotationAtts.axes3D.yAxis.title.font.italic = 0
    AnnotationAtts.axes3D.yAxis.title.userTitle = 0
    AnnotationAtts.axes3D.yAxis.title.userUnits = 0
    AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
    AnnotationAtts.axes3D.yAxis.title.units = ""
    AnnotationAtts.axes3D.yAxis.label.visible = 1
    AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.yAxis.label.font.scale = 1
    AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.yAxis.label.font.bold = 0
    AnnotationAtts.axes3D.yAxis.label.font.italic = 0
    AnnotationAtts.axes3D.yAxis.label.scaling = 0
    AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.yAxis.grid = 0
    AnnotationAtts.axes3D.zAxis.title.visible = 1
    AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.zAxis.title.font.scale = 1
    AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.zAxis.title.font.bold = 0
    AnnotationAtts.axes3D.zAxis.title.font.italic = 0
    AnnotationAtts.axes3D.zAxis.title.userTitle = 0
    AnnotationAtts.axes3D.zAxis.title.userUnits = 0
    AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
    AnnotationAtts.axes3D.zAxis.title.units = ""
    AnnotationAtts.axes3D.zAxis.label.visible = 1
    AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.zAxis.label.font.scale = 1
    AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.zAxis.label.font.bold = 0
    AnnotationAtts.axes3D.zAxis.label.font.italic = 0
    AnnotationAtts.axes3D.zAxis.label.scaling = 0
    AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.zAxis.grid = 0
    AnnotationAtts.axes3D.setBBoxLocation = 0
    AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
    AnnotationAtts.axes3D.triadColor = (0, 0, 0)
    AnnotationAtts.axes3D.triadLineWidth = 0
    AnnotationAtts.axes3D.triadFont = 0
    AnnotationAtts.axes3D.triadBold = 1
    AnnotationAtts.axes3D.triadItalic = 1
    AnnotationAtts.axes3D.triadSetManually = 0
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.userInfoFont.scale = 1
    AnnotationAtts.userInfoFont.useForegroundColor = 1
    AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.userInfoFont.bold = 0
    AnnotationAtts.userInfoFont.italic = 0
    AnnotationAtts.databaseInfoFlag = 1
    AnnotationAtts.timeInfoFlag = 0
    AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Courier  # Arial, Courier, Times
    AnnotationAtts.databaseInfoFont.scale = 1
    AnnotationAtts.databaseInfoFont.useForegroundColor = 0
    AnnotationAtts.databaseInfoFont.color = (255, 255, 255, 255)
    AnnotationAtts.databaseInfoFont.bold = 1
    AnnotationAtts.databaseInfoFont.italic = 0
    AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
    AnnotationAtts.databaseInfoTimeScale = 1
    AnnotationAtts.databaseInfoTimeOffset = 0
    AnnotationAtts.legendInfoFlag = 1
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
    AnnotationAtts.gradientColor1 = (grad2, 0, grad1, 255)
    AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
    AnnotationAtts.backgroundMode = AnnotationAtts.Gradient  # Solid, Gradient, Image, ImageSphere
    AnnotationAtts.backgroundImage = ""
    AnnotationAtts.imageRepeatX = 1
    AnnotationAtts.imageRepeatY = 1
    AnnotationAtts.axesArray.visible = 1
    AnnotationAtts.axesArray.ticksVisible = 1
    AnnotationAtts.axesArray.autoSetTicks = 1
    AnnotationAtts.axesArray.autoSetScaling = 1
    AnnotationAtts.axesArray.lineWidth = 0
    AnnotationAtts.axesArray.axes.title.visible = 1
    AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axesArray.axes.title.font.scale = 1
    AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
    AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axesArray.axes.title.font.bold = 0
    AnnotationAtts.axesArray.axes.title.font.italic = 0
    AnnotationAtts.axesArray.axes.title.userTitle = 0
    AnnotationAtts.axesArray.axes.title.userUnits = 0
    AnnotationAtts.axesArray.axes.title.title = ""
    AnnotationAtts.axesArray.axes.title.units = ""
    AnnotationAtts.axesArray.axes.label.visible = 1
    AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axesArray.axes.label.font.scale = 1
    AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
    AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axesArray.axes.label.font.bold = 0
    AnnotationAtts.axesArray.axes.label.font.italic = 0
    AnnotationAtts.axesArray.axes.label.scaling = 0
    AnnotationAtts.axesArray.axes.tickMarks.visible = 1
    AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
    AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
    AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axesArray.axes.grid = 0
    SetAnnotationAttributes(AnnotationAtts)

def psuedo():
    AddPlot("Pseudocolor", "sst", 1, 1)
    SetActivePlots(0)
    SetActivePlots(0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
    PseudocolorAtts.skewFactor = 1
    PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
    PseudocolorAtts.minFlag = 0
    PseudocolorAtts.min = 0
    PseudocolorAtts.useBelowMinColor = 0
    PseudocolorAtts.belowMinColor = (0, 0, 0, 255)
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.max = 35
    PseudocolorAtts.useAboveMaxColor = 0
    PseudocolorAtts.aboveMaxColor = (0, 0, 0, 255)
    PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
    PseudocolorAtts.colorTableName = "Spectral"
    PseudocolorAtts.invertColorTable = 1
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    PseudocolorAtts.opacityVariable = ""
    PseudocolorAtts.opacity = 1
    PseudocolorAtts.opacityVarMin = 0
    PseudocolorAtts.opacityVarMax = 1
    PseudocolorAtts.opacityVarMinFlag = 0
    PseudocolorAtts.opacityVarMaxFlag = 0
    PseudocolorAtts.pointSize = 0.05
    PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    PseudocolorAtts.pointSizeVarEnabled = 0
    PseudocolorAtts.pointSizeVar = "default"
    PseudocolorAtts.pointSizePixels = 2
    PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
    PseudocolorAtts.lineWidth = 0
    PseudocolorAtts.tubeResolution = 10
    PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
    PseudocolorAtts.tubeRadiusAbsolute = 0.125
    PseudocolorAtts.tubeRadiusBBox = 0.005
    PseudocolorAtts.tubeRadiusVarEnabled = 0
    PseudocolorAtts.tubeRadiusVar = ""
    PseudocolorAtts.tubeRadiusVarRatio = 10
    PseudocolorAtts.tailStyle = PseudocolorAtts.None  # None, Spheres, Cones
    PseudocolorAtts.headStyle = PseudocolorAtts.None  # None, Spheres, Cones
    PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
    PseudocolorAtts.endPointRadiusAbsolute = 0.125
    PseudocolorAtts.endPointRadiusBBox = 0.05
    PseudocolorAtts.endPointResolution = 10
    PseudocolorAtts.endPointRatio = 5
    PseudocolorAtts.endPointRadiusVarEnabled = 0
    PseudocolorAtts.endPointRadiusVar = ""
    PseudocolorAtts.endPointRadiusVarRatio = 10
    PseudocolorAtts.renderSurfaces = 1
    PseudocolorAtts.renderWireframe = 0
    PseudocolorAtts.renderPoints = 0
    PseudocolorAtts.smoothingLevel = 0
    PseudocolorAtts.legendFlag = 1
    PseudocolorAtts.lightingFlag = 1
    PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
    PseudocolorAtts.pointColor = (0, 0, 0, 0)
    SetPlotOptions(PseudocolorAtts)

def saveWin(day):
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = "./410FinalProject/window_saves/sesh3"
    SaveWindowAtts.fileName = str(year)+"_"+str(month)+"_"+str(day)
    SaveWindowAtts.family = 1
    SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
    SaveWindowAtts.width = 1024
    SaveWindowAtts.height = 1024
    SaveWindowAtts.screenCapture = 0
    SaveWindowAtts.saveTiled = 0
    SaveWindowAtts.quality = 80
    SaveWindowAtts.progressive = 0
    SaveWindowAtts.binary = 0
    SaveWindowAtts.stereo = 0
    SaveWindowAtts.compression = SaveWindowAtts.None  # None, PackBits, Jpeg, Deflate, LZW
    SaveWindowAtts.forceMerge = 0
    SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
    SaveWindowAtts.pixelData = 1
    SaveWindowAtts.advancedMultiWindowSave = 0
    SaveWindowAtts.subWindowAtts.win1.position = (0, 0)
    SaveWindowAtts.subWindowAtts.win1.size = (128, 128)
    SaveWindowAtts.subWindowAtts.win1.layer = 0
    SaveWindowAtts.subWindowAtts.win1.transparency = 0
    SaveWindowAtts.subWindowAtts.win1.omitWindow = 0
    SaveWindowAtts.opts.types = ()
    SaveWindowAtts.opts.help = ""
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

def extrude():
    AddOperator("Extrude", 1)
    ExtrudeAtts = ExtrudeAttributes()
    ExtrudeAtts.axis = (0, 0, 1)
    ExtrudeAtts.byVariable = 1
    ExtrudeAtts.variable = "sst"
    ExtrudeAtts.length = 1
    ExtrudeAtts.steps = 1
    ExtrudeAtts.preserveOriginalCellNumbers = 1
    SetOperatorOptions(ExtrudeAtts, 0, 1)

v1 = GetView3D() #original window (top-down)
v1.viewNormal = (0, 0, 1)
v1.focus = (180, 0, 0)
v1.viewUp = (0, 1, 0)
v1.viewAngle = 30
v1.parallelScale = 201.078
v1.nearPlane = -402.157
v1.farPlane = 402.157
v1.imagePan = (0, 0)
v1.imageZoom = 1
v1.perspective = 1
v1.eyeAngle = 2
v1.centerOfRotationSet = 0
v1.centerOfRotation = (180, 0, 0)
v1.axis3DScaleFlag = 0
v1.axis3DScales = (1, 1, 1)
v1.shear = (0, 0, 1)
v1.windowValid = 1

v2 = GetView3D() #north
v2.viewNormal = (-0.0451351, -0.443815, 0.894981)
v2.focus = (180, 0, 0)
v2.viewUp = (0.00114275, 0.895871, 0.444313)
v2.viewAngle = 30
v2.parallelScale = 201.078
v2.nearPlane = -402.157
v2.farPlane = 402.157
v2.imagePan = (0, 0)
v2.imageZoom = 1
v2.perspective = 1
v2.eyeAngle = 2
v2.centerOfRotationSet = 0
v2.centerOfRotation = (180, 0, 0)
v2.axis3DScaleFlag = 0
v2.axis3DScales = (1, 1, 1)
v2.shear = (0, 0, 1)
v2.windowValid = 1

v3 = GetView3D() #north-west
v3.viewNormal = (0.467174, -0.319398, 0.82446)
v3.focus = (180, 0, 0)
v3.viewUp = (-0.16205, 0.885745, 0.434965)
v3.viewAngle = 30
v3.parallelScale = 201.078
v3.nearPlane = -402.157
v3.farPlane = 402.157
v3.imagePan = (0, 0)
v3.imageZoom = 1
v3.perspective = 1
v3.eyeAngle = 2
v3.centerOfRotationSet = 0
v3.centerOfRotation = (180, 0, 0)
v3.axis3DScaleFlag = 0
v3.axis3DScales = (1, 1, 1)
v3.shear = (0, 0, 1)
v3.windowValid = 1

v4 = GetView3D() #south-west
v4.viewNormal = (0.409846, 0.294663, 0.86325)
v4.focus = (180, 0, 0)
v4.viewUp = (-0.0520368, 0.952397, -0.300387)
v4.viewAngle = 30
v4.parallelScale = 201.078
v4.nearPlane = -402.157
v4.farPlane = 402.157
v4.imagePan = (0, 0)
v4.imageZoom = 1
v4.perspective = 1
v4.eyeAngle = 2
v4.centerOfRotationSet = 0
v4.centerOfRotation = (180, 0, 0)
v4.axis3DScaleFlag = 0
v4.axis3DScales = (1, 1, 1)
v4.shear = (0, 0, 1)
v4.windowValid = 1

v5 = GetView3D() #south
v5.viewNormal = (0.0630336, 0.492354, 0.868109)
v5.focus = (180, 0, 0)
v5.viewUp = (-0.00956062, 0.870097, -0.492788)
v5.viewAngle = 30
v5.parallelScale = 201.078
v5.nearPlane = -402.157
v5.farPlane = 402.157
v5.imagePan = (0, 0)
v5.imageZoom = 1
v5.perspective = 1
v5.eyeAngle = 2
v5.centerOfRotationSet = 0
v5.centerOfRotation = (180, 0, 0)
v5.axis3DScaleFlag = 0
v5.axis3DScales = (1, 1, 1)
v5.shear = (0, 0, 1)
v5.windowValid = 1

v6 = GetView3D() #south-east
v6.viewNormal = (-0.364899, 0.483454, 0.795689)
v6.focus = (180, 0, 0)
v6.viewUp = (0.117255, 0.871675, -0.47585)
v6.viewAngle = 30
v6.parallelScale = 201.078
v6.nearPlane = -402.157
v6.farPlane = 402.157
v6.imagePan = (0, 0)
v6.imageZoom = 1
v6.perspective = 1
v6.eyeAngle = 2
v6.centerOfRotationSet = 0
v6.centerOfRotation = (180, 0, 0)
v6.axis3DScaleFlag = 0
v6.axis3DScales = (1, 1, 1)
v6.shear = (0, 0, 1)
v6.windowValid = 1

v7 = GetView3D() #north-east
v7.viewNormal = (-0.48451, -0.255703, 0.83658)
v7.focus = (180, 0, 0)
v7.viewUp = (0.0054671, 0.955422, 0.295193)
v7.viewAngle = 30
v7.parallelScale = 201.078
v7.nearPlane = -402.157
v7.farPlane = 402.157
v7.imagePan = (0, 0)
v7.imageZoom = 1
v7.perspective = 1
v7.eyeAngle = 2
v7.centerOfRotationSet = 0
v7.centerOfRotation = (180, 0, 0)
v7.axis3DScaleFlag = 0
v7.axis3DScales = (1, 1, 1)
v7.shear = (0, 0, 1)
v7.windowValid = 1

import os

#year = 1980 TODO: start @ 1980
year = 1980

month = 0

grad1 = 255
grad2 = 0
gradinc = 6.5

#animate camera
numSteps = 3650
curStep = 0
vpts=(v1,v2, v3, v4, v5, v6, v7)
x=[0, 0.16, 0.33, 0.5, 0.66, 0.83, 1]

for i in range(40):
    month = 0
    year += 1
    grad1-=gradinc
    grad2+=gradinc
    for j in range(12):
        month += 1
        DeleteActivePlots()
        if(month < 10):
            if (os.path.isfile("/Users/sean/410FinalProject/python-scripts/data/"+str(year)+"_"+"0"+str(month)+"_01.nc")):
                OpenDatabase("localhost:/Users/sean/410FinalProject/python-scripts/data/"+str(year)+"_"+"0"+str(month)+"_*.nc database", 0)
                ActivateDatabase("localhost:/Users/sean/410FinalProject/python-scripts/data/"+str(year)+"_"+"0"+str(month)+"_*.nc database")
            else:
                print(str(year)+"/"+str(month)+" not a db")
                continue

        else:
            if (os.path.isfile("/Users/sean/410FinalProject/python-scripts/data/"+str(year)+"_"+str(month)+"_01.nc")):
                OpenDatabase("localhost:/Users/sean/410FinalProject/python-scripts/data/"+str(year)+"_"+str(month)+"_*.nc database", 0)
                ActivateDatabase("localhost:/Users/sean/410FinalProject/python-scripts/data/"+str(year)+"_"+str(month)+"_*.nc database")
            else:
                print(str(year)+"/"+str(month)+" not a db")
                continue

        psuedo()
        extrude()
        annotate()
        InvertBackgroundColor()
        DrawPlots()
        for i in range(1, 32):
            if(curStep == numSteps):
                curStep = 0
            else:
                curStep += 1
            t = float(curStep) / float(numSteps - 1)
            c = EvalCubicSpline(t, x, vpts)
            SetView3D(c)


            SaveWindowAtts = SaveWindowAttributes()
            SaveWindowAtts.outputToCurrentDirectory = 1
            SaveWindowAtts.outputDirectory = "./410FinalProject/window_saves/sesh3"
            SaveWindowAtts.fileName = str(year)+"_"+str(month)+"_"+str(i)
            SaveWindowAtts.family = 1
            SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
            SaveWindowAtts.width = 1024
            SaveWindowAtts.height = 1024
            SaveWindowAtts.screenCapture = 0
            SaveWindowAtts.saveTiled = 0
            SaveWindowAtts.quality = 80
            SaveWindowAtts.progressive = 0
            SaveWindowAtts.binary = 0
            SaveWindowAtts.stereo = 0
            SaveWindowAtts.compression = SaveWindowAtts.None  # None, PackBits, Jpeg, Deflate, LZW
            SaveWindowAtts.forceMerge = 0
            SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
            SaveWindowAtts.pixelData = 1
            SaveWindowAtts.advancedMultiWindowSave = 0
            SaveWindowAtts.subWindowAtts.win1.position = (0, 0)
            SaveWindowAtts.subWindowAtts.win1.size = (128, 128)
            SaveWindowAtts.subWindowAtts.win1.layer = 0
            SaveWindowAtts.subWindowAtts.win1.transparency = 0
            SaveWindowAtts.subWindowAtts.win1.omitWindow = 0
            SaveWindowAtts.opts.types = ()
            SaveWindowAtts.opts.help = ""
            SetSaveWindowAttributes(SaveWindowAtts)
            SaveWindow()

            #saveWin(i)


            TimeSliderNextState()
