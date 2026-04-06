from tarea1 import Stack, Queue, HashTable


# ===== STACK =====
print("STACK  - Deshacer acciones ")
undo = Stack()
undo.push("escribir hola")
undo.push("cambiar color")
undo.push("mover caja")
print(f"Deshacer: {undo.pop()}")
print(f"Deshacer: {undo.pop()}")
print()

# ===== QUEUE =====
print("QUEUE  - Atención al cliente")
cola = Queue()
cola.enqueue("Cliente 1")
cola.enqueue("Cliente 2")
cola.enqueue("Cliente 3")
print(f"Siguiente cliente: {cola.dequeue()}")
print(f"Siguiente cliente: {cola.dequeue()}")
print()

# ===== HASHTABLE =====
print("HASHTABLE - Almacenar datos de usuario ")
cache = HashTable()
cache.put("nombre", "Juan")
cache.put("edad", 25)
cache.put("ciudad", "Madrid")
print(f"Nombre: {cache.get('nombre')}")
print(f"Edad: {cache.get('edad')}")
print(f"¿Existe ciudad? {cache.contains('ciudad')}")
cache.delete("edad")
print(f"¿Existe edad? {cache.contains('edad')}")
