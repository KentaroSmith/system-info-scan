Start-Job -ScriptBlock{
    Invoke-Item "\\utilities\Water_Quality\Shared\Technology\Software\Bluebeam\Bluebeam License Info.docx"
    Start-Process "\\citydata\public\InfoSys\Deployment_Apps\VC2015\vc_redist.x64.exe" /passive -Wait
    Start-Process "\\utilities\Water_Quality\Shared\Technology\Software\Bluebeam\BbRevu2019.exe"
} 
