Start-Job -ScriptBlock {
    Start-Process "\\citydata\public\InfoSys\Deployment_Apps\ArcGIS\10.7\setup.msi" TRANSFORMS="\\citydata\public\InfoSys\Deployment_Apps\ArcGIS\10.7\fixed.mst" -Wait 
    Start-Process "\\gisfile\GIS_software\Software_Authorization\ArcGISDesktopStandard_SingleUse_859018.prvc" -Wait
} | Wait-Job

