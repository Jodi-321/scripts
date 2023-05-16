$ErrorActionPreferance = 'SilentlyContinue'

$netFolders = NET.EXE VIEW "\\file_server_name"
$test = ($netFolders | Where-Object { $_ -match '\sDisk\s' }) -replace '\s\s+', ',' | ForEach-Object{ ($_ -split ',')[0] }
[System.Collections.ArrayList]$myArray =@()

foreach ($_ in $test)		# "foreach" loops through each top level folder($_)
{
	$i = $_
	$filePath = "\\file_server_name\$i"		#adds folder ($i) to file path($filePath)
	Set-Location -Path $filePath -ErrorAction SilentlyContinue 
	if($?)		#if the last command(Set-Location $filePath) succesfully ran -- iteration is true
	{
				#iteration completes and moves on
	}
	else 		#if the last command (Set-Location $filePath) fails, iteration is false
	{ 
		$myArray.Add($filePath) | out-null		#folder that needs permissions added to list	
	}
}
#writes final output to screen
write-output "Command Failed: `n" 
echo $myArray
