Get-Content .env | ForEach-Object { Invoke-Expression $_ }
