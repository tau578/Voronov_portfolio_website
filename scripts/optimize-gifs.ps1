$ErrorActionPreference = 'Stop'
$ffmpeg = (Get-ChildItem .tools/imageio_ffmpeg/binaries -Filter '*.exe').FullName
$report = @()
foreach ($asset in (Get-ChildItem assets -Filter '*.gif' | Where-Object Name -ne 'operator.gif')) {
 $backup = Join-Path '.media-backup' $asset.Name
 if (!(Test-Path -LiteralPath $backup)) { Copy-Item -LiteralPath $asset.FullName -Destination $backup }
 $output = Join-Path '.media-optimized' $asset.Name
 & $ffmpeg -hide_banner -loglevel error -i $backup -filter_complex 'fps=8,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=none' -loop 0 $output -y
 if ($LASTEXITCODE -ne 0) { throw "Conversion failed: $($asset.Name)" }
 $size=(Get-Item -LiteralPath $output).Length
 $report += [PSCustomObject]@{file=$asset.Name;before=$asset.Length;after=$size;savedPercent=[Math]::Round((1-$size/$asset.Length)*100,1)}
 Write-Output "$($asset.Name): $($asset.Length) -> $size"
}
$report | ConvertTo-Json | Set-Content docs/gif-optimization.json

