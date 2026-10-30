$assets = @{
'paintbucket.png'='O1qjf5lZOhy0IIsOIQsuT0cjic.png'; 'effacement.gif'='nmRHJwtaQz0pqpkVj0pBaMTw98.gif'; 'bdd.gif'='Uo2RyveKpKJ3xWXdfMNcic1r32U.gif'; 'dialekt.gif'='QxE8jy4zOUzUo8T45Y9QfhBDmo.gif'; 'breath.gif'='uDg63TgcwflegmSF2DMRtlVuZ8.gif'; 'cheese.gif'='739lQ8FgfoQ5YrtpAZwvP87Toxs.gif'; 'room.gif'='GRAVyOq7QZOFEYrllgU8kyO9t0.gif'; 'punk.gif'='ChRCZEzG23J9ewtrIQ7FqJWUZA.gif'; 'wasteland.gif'='Ugvu7W17l7P0MR6SFZmkSTLPs9k.gif'; 'critique.gif'='Du6RYMMvCmSRXsidghl6ICFz8.gif'; 'duel.gif'='3ZhIfBFVUazdIv97YPFFkSqDU.gif'; 'panzer.gif'='1oIC0lCtJBadSDEF3jFQWOgWZ5M.gif'
}
foreach ($asset in $assets.GetEnumerator()) { Invoke-WebRequest -Uri ('https://framerusercontent.com/images/' + $asset.Value) -OutFile ('assets/' + $asset.Key) }
Get-ChildItem assets | Select-Object Name,Length

