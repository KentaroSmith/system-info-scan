Start-Job -ScriptBlock {
    Start-Process "\\citydata\public\InfoSys\Deployment_Apps\ArcGIS\10.7\setup.msi" TRANSFORMS="\\citydata\public\InfoSys\Deployment_Apps\ArcGIS\10.7\fixed.mst" -Wait 
    Start-Process "\\gisfile\GIS_software\ArcGIS Pro\ArcGIS Pro 2.8\ArcGISPro\ArcGISPro.msi" -Wait
    Start-Process "\\gisfile\GIS_software\Software_Authorization\ArcGISDesktopAdvanced_SingleUse_859021.prvc" -Wait
} | Wait-Job