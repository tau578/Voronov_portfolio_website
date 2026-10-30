$ErrorActionPreference='Stop'
$ffmpeg=(Get-ChildItem .tools/imageio_ffmpeg/binaries -Filter '*.exe').FullName
foreach($gif in Get-ChildItem assets -Filter '*.gif'){
 $source=Join-Path '.media-backup' $gif.Name
 if(!(Test-Path $source)){Copy-Item $gif.FullName $source}
 $stem=$gif.BaseName
 & $ffmpeg -hide_banner -loglevel error -i $source -vf 'fps=12,scale=640:-2:flags=lanczos' -an -c:v libx264 -preset medium -crf 25 -pix_fmt yuv420p -movflags +faststart ('assets/'+$stem+'.mp4') -y
 if($LASTEXITCODE -ne 0){throw "Failed: $stem"}
 & $ffmpeg -hide_banner -loglevel error -ss 1 -i $source -vf 'scale=640:-2' -frames:v 1 -q:v 3 ('assets/'+$stem+'-poster.jpg') -y
 Write-Output $stem
}
