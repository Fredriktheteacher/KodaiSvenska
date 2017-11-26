# Skapad av Frippe 2017
# fabelmakaren.se
# Se avsnittet på YouTube: https://youtu.be/pgVbCzYPPBU

# Enkelt program som kollar om man är bleking
fras="Den däkan är riktigt duktig på att spela basket."
if "däkan" in fras:
  print('Du är bleking.')
else:
  print('Du är förmodligen inte bleking.')

  
# Samma program fast med inmatning från tangentbordet

fras = input('Skriv in fras som ska kollas: ')
if 'däka' in fras:
  print('Frasen innehåller blekingska')
else:
  print('Frasen innehåller INTE blekingska')


# Förslag till progression:
# Kolla om en eller flera ord ingår i en fras mha en ordlista
fras='den däkan pular med sin motorcykel'
ordlista=['däka','färas','pula']
if any(word in fras for word in ordlista):
  print('Du är verkligen en äkta bleking!')
else:
  print('Du verkar inte prata blekingska')
