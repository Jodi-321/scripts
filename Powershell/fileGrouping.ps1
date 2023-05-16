$e = $ErrorActionPreference
$ErrorActionPreference="stop"

$folders = Get-ChildItem $startfolders | Where-Object {$_.PSIsContainer -eq $true} | Sort-Object
$groupSize = 0.00
$groupCount = 0

[System.Collections.ArrayList]$fileArray = @()
[System.Collections.ArrayList]$bigFileArray =@()

try {
	foreach ($i in $folders)
	{
		$subfoldersItems = Get-ChildItem $i.FullName -recurse -ErrorAction SilentlyContinue -ErrorVariable myError | Where-Object {$_.PSIsContainer -eq $false} | Measure-Object -property Length -sum | Select-Object Sum -ErrorAction SilentlyContinue
		$subfolderNum = ($subfoldersItems.sum /1GB) 
		$fileItem = (-join($i.FullName," - ",$subfolderNum))
		$bigFileItem = (-join($i.FullName," - ",$subfolderNum))

		$groupSize += $subfolderNum
		if ($subfolderNum -le 160.00)  #If groupSize exceeds this number, current #group is printed, and new group is started
		{
			if ($groupSize -ge 250.00)
			{
				write-output "`n`n" 
				#echo "groupSize more than 250"

				write-output "Group: "

				echo $fileArray
				echo $groupSize 
				$fileArray = @()

				$groupSize = 0.00

				$fileArray.Add($fileItem) | out-null
				$groupSize += $subfolderNum
			}
			else 
			{
				$fileArray.Add($fileItem) | out-null
				$groupSize += $subfolderNum
			}
		}
		else #Adds folder to current group  
		{
			$bigFileArray.Add($bigFileItem) | out-null
		}
	}
	}
catch 
	{ 
		$ErrorActionPreference=$e
	}
$ErrorActionPreference=$e;

echo $fileArray  #prints final group
echo $groupSize

write-output "`n`n Big Folders"

echo $bigFileArray 