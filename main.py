
def validarNumeroReal(valor):
  input = str(valor)
  estado = 1
  posicion = 0
  for char in input: # ciclo
    posicion+=1
    if estado == 1: # Estado 1
      if char.isnumeric():
        estado = 2
      else:
        error = "Error en la posicion ", posicion, ". Se encontró: '", char , "'"
        return False, error
      continue

    if estado == 2: # Estado 2
      if char.isnumeric():
        estado = 2
      elif char == "E":
        estado = 5
      elif char == ".":
        estado = 3
      else:
        error = "Error en la posicion ", posicion, ". Se encontró: '", char , "'"
        return False, error
      continue

    if estado == 3: # Estado 3
      if char.isnumeric():
        estado = 4
      else:
        error = "Error en la posicion ", posicion, ". Se encontró: '", char , "'"
        return False, error
      continue

    if estado == 4: # Estado 4
      if char.isnumeric():
        estado = 4
      elif char == "E":
        estado = 5
      else:
        error = "Error en la posicion ", posicion, ". Se encontró: '", char , "'"
        return False, error
      continue

    if estado == 5: # Estado 5
      if char == "+" or char == "-":
        estado = 6
      if char.isnumeric():
        estado = 7
      else:
        error = "Error en la posicion ", posicion, ". Se encontró: '", char , "'"
        return False, error
      continue

    if estado == 6:
      if char.isnumeric():
        estado = 7
      else:
        error = "Error en la posicion ", posicion, ". Se encontró: '", char , "'"
        return False, error
      continue

    if estado == 7:
      if char.isnumeric():
        estado = 7
      else:
        error = "Error en la posicion ", posicion, ". Se encontró: '", char , "'"
        return False, error
      continue

  if estado != 4 and estado != 7:
    return False, "Valor de ingreso no es un numero real."
  
  return True, None # Todo bien, es numero real


esNumeroReal, error = validarNumeroReal(25.4)
print(esNumeroReal, error)


