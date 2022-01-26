function getIP{
(Get-NetIPAddress).IPAddress | Select-String "192"
}

Write-Host(getIP)

$IP = getIP

Write-Host("This is our machine's IP: $IP")

Write-Host("This machine's Ip is: {0}" -f $IP)