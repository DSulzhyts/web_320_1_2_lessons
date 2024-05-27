from platform import platform, machine, processor, system, version

print(platform())
print(platform(True))
print(platform(False, True))
print(machine())
print(processor())
print(system())
print(version())