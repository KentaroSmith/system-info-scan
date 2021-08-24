Start-Job -ScriptBlock {
    Start-Process "\\citydata\public\InfoSys\CIS Infinity\Infinity install files\V4CISInstall\.NET install\.Net4.8\ndp48-x86-x64-allos-enu.exe" -Wait
    Start-Process "\\citydata\public\InfoSys\CIS Infinity\Infinity install files\V4CISInstall\Crystal report runtime\CRRuntime_64bit_13_0_24.msi" -Wait
    Start-Process "\\citydata\public\InfoSys\CIS Infinity\Infinity install files\V4CISInstall\SQLite ODBC\sqliteodbc_w64.exe" -Wait
    Copy-Item "\\citydata\public\InfoSys\CIS Infinity\Infinity install files\CISInfinity4 - Production.lnk" -Destination "C:\Users\Public\Desktop"
}