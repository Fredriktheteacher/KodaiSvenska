# Skapad av Frippe 2017
# fabelmakaren.se

# Enkelt program som kollar om man är bleking
fras="Den däkan är riktigt duktig på att spela basket."
if fras.find('däkan'):
  print('Du är en äkta bleking.')
else:
  print('Du är förmodligen inte bleking.')

# Förslag till progression:
# Kolla om en eller flera ord ingår i en fras
fras='den däkan jobbar redigt hårt'
ordlista=['däka','färas','redig']
if any(word in fras for word in ordlista):
  print('Du är verkligen en äkta bleking!')
else:
  print('Du verkar inte prata blekingska')
