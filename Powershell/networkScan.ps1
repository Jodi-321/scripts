$e = $ErrorActionPreference
$ErrorActionPreference="stop"

$folders = Get-ChildItem $startfolders | Where-Object {$_.PSIsContainer -eq $true} | Sort-Object
$groupSize = 0.00
$groupCount = 0
[System.Collections.ArrayList]$fileArray = @()

try {
	foreach ($i in $folders)
	{
		$subfolderNum = ($subfoldersItems.sum / 1GB) 		
		#If groupSize exceeds this number, current group is printed, and new group is started
        if ($groupSize -ge 260.00)  		
        {
			write-output "Group: "
			echo $fileArray + " `n "

			$fileArray = @()
			$groupSize = 0.00
			$groupCount += 1
		}
		else #Adds folder to current group  
		{

			$subfoldersItems = Get-ChildItem $i.FullName -Recurse -ErrorAction SilentlyContinue -ErrorVariable myError | Where-Object {$_.PSIsContainer -eq $false} | Measure-Object -property Length -sum | Select-Object Sum -ErrorAction SilentlyContinue
			$fileItem = $i.FullName + ” — ” + “{0:N2}” -f ($subfoldersItems.sum / 1GB) + ” GB”
			$fileArray.Add($fileItem) | out-null
			$groupSize += $subfolderNum
		}
	}
	}
catch 
	{ 
		$ErrorActionPreference=$e
	}

$ErrorActionPreference=$e;
echo $fileArray  #prints final group
