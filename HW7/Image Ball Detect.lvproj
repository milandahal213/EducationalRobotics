<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="21008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Bounce.vi" Type="VI" URL="../_SubVis/Bounce.vi"/>
		<Item Name="Finding-g.vi" Type="VI" URL="../Finding-g.vi"/>
		<Item Name="FindXYandT.vi" Type="VI" URL="../_SubVis/FindXYandT.vi"/>
		<Item Name="GFinder.vi" Type="VI" URL="../_SubVis/GFinder.vi"/>
		<Item Name="Ramp.vi" Type="VI" URL="../_SubVis/Ramp.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="user.lib" Type="Folder">
				<Item Name="BiggestComplexBlob.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/BiggestComplexBlob.vi"/>
				<Item Name="BinaryThreshold.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/BinaryThreshold.vi"/>
				<Item Name="BlobCtrl.ctl" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/BlobFind2/BlobCtrl.ctl"/>
				<Item Name="BlobIt.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/BlobFind2/BlobIt.vi"/>
				<Item Name="CheckFor8bitDepth.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/CheckFor8bitDepth.vi"/>
				<Item Name="CheckForBinary.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/CheckForBinary.vi"/>
				<Item Name="CheckSizes.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/CheckSizes.vi"/>
				<Item Name="ComplexBlob.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/ComplexBlob.vi"/>
				<Item Name="ConvertImageToQTFormat.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/WindowsDriver/ConvertImageToQTFormat.vi"/>
				<Item Name="DrawImageLowLevel.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/DrawImageLowLevel.vi"/>
				<Item Name="Err_SizeCheck.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/Err_SizeCheck.vi"/>
				<Item Name="Extract8BitImage.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/Extract8BitImage.vi"/>
				<Item Name="FindBlob_CenterOfMass.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/FindBlob_CenterOfMass.vi"/>
				<Item Name="FindMinMaxRect.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/BlobFind2/FindMinMaxRect.vi"/>
				<Item Name="FlatttenMatrix.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/FlatttenMatrix.vi"/>
				<Item Name="GenerateColorLUT.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/GenerateColorLUT.vi"/>
				<Item Name="GetBlobROI.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/GetBlobROI.vi"/>
				<Item Name="GetGreyscalePlane.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/GetGreyscalePlane.vi"/>
				<Item Name="GetPlane.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/GetPlane.vi"/>
				<Item Name="ID Blob.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/BlobFind2/ID Blob.vi"/>
				<Item Name="IdentifyBlob_Circle_Cluster.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/IdentifyBlob_Circle_Cluster.vi"/>
				<Item Name="IdentifyBlob_Circle_Image.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/IdentifyBlob_Circle_Image.vi"/>
				<Item Name="IdentifyBlob_Square_Cluster.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/IdentifyBlob_Square_Cluster.vi"/>
				<Item Name="IdentifyBlob_Square_Image.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/IdentifyBlob_Square_Image.vi"/>
				<Item Name="IdentifyBlobPoly.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/IdentifyBlobPoly.vi"/>
				<Item Name="LV86_32 bit array to image.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/LV86_32 bit array to image.vi"/>
				<Item Name="LV86_Convert to image.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/LV86_Convert to image.vi"/>
				<Item Name="LV86_GetImageSubset.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/LV86_GetImageSubset.vi"/>
				<Item Name="LV86_Image to 32 bit arrray.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/LV86_Image to 32 bit arrray.vi"/>
				<Item Name="LV86_Subtract.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/LV86_Subtract.vi"/>
				<Item Name="ManyColorTables.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/ManyColorTables.vi"/>
				<Item Name="OpenImageFile.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/OpenImageFile.vi"/>
				<Item Name="QT_File.ctl" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/QTLIB_2595_LV86/QT_File.ctl"/>
				<Item Name="QT_Image.ctl" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/QTLIB_2595_LV86/QT_Image.ctl"/>
				<Item Name="QT_Private.ctl" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/QTLIB_2595_LV86/QT_Private.ctl"/>
				<Item Name="RemoveBlob.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/BlobFind2/RemoveBlob.vi"/>
				<Item Name="ShowImage.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/ShowImage.vi"/>
				<Item Name="StripOutside.vi" Type="VI" URL="/&lt;userlib&gt;/ImageProcessing/BlobFind2/StripOutside.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Bit-array To Byte-array.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pictutil.llb/Bit-array To Byte-array.vi"/>
				<Item Name="Calc Long Word Padded Width.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Calc Long Word Padded Width.vi"/>
				<Item Name="Check Path.vi" Type="VI" URL="/&lt;vilib&gt;/picture/jpeg.llb/Check Path.vi"/>
				<Item Name="Create Mask By Alpha.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Create Mask By Alpha.vi"/>
				<Item Name="Directory of Top Level VI.vi" Type="VI" URL="/&lt;vilib&gt;/picture/jpeg.llb/Directory of Top Level VI.vi"/>
				<Item Name="Draw Arc.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Draw Arc.vi"/>
				<Item Name="Draw Circle by Radius.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pictutil.llb/Draw Circle by Radius.vi"/>
				<Item Name="Draw Flattened Pixmap(6_1).vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Draw Flattened Pixmap(6_1).vi"/>
				<Item Name="Draw Flattened Pixmap.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Draw Flattened Pixmap.vi"/>
				<Item Name="Draw Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Draw Rect.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="FixBadRect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pictutil.llb/FixBadRect.vi"/>
				<Item Name="Flip and Pad for Picture Control.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Flip and Pad for Picture Control.vi"/>
				<Item Name="imagedata.ctl" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/imagedata.ctl"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="QT_ImgOpen.vi" Type="VI" URL="/&lt;vilib&gt;/addons/RoboLab/ImageProcessing/QTLIB_2595_LV86/QT_ImgOpen.vi"/>
				<Item Name="Read BMP File Data.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Read BMP File Data.vi"/>
				<Item Name="Read BMP File.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Read BMP File.vi"/>
				<Item Name="Read BMP Header Info.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Read BMP Header Info.vi"/>
				<Item Name="Read JPEG File.vi" Type="VI" URL="/&lt;vilib&gt;/picture/jpeg.llb/Read JPEG File.vi"/>
				<Item Name="Read PNG File.vi" Type="VI" URL="/&lt;vilib&gt;/picture/png.llb/Read PNG File.vi"/>
				<Item Name="Set Pen State.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Set Pen State.vi"/>
			</Item>
			<Item Name="lvanlys.framework" Type="Document" URL="/&lt;resource&gt;/lvanlys.framework"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
