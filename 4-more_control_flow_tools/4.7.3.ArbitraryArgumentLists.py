def concat(*args, sep='/'):
    return sep.join(args);

r0 = concat("earth", "mars", "venus");
print(r0)

r1 = concat("earth", "mars", "venus", sep=".")
print(r1)

print(20 * "=")

