function getIP{
(Get-NetIPAddress).IPv4Address | Select "192"

}

$IP = getIP

function getHostname{
(Get-Host).Hos
}

$HOST = getHostname

Send-MailMessage -To "bellerkr@mail.uc.edu" -From "kylebeller2@gmail.com" -Subject "IT3038C Windows SysInfo" -Body "The IP of the machine is $IP , the hostname is $HOST" -SmtpServer smtp.gmail.com -Port 587 -UseSSL -Credential (Get-Credential)