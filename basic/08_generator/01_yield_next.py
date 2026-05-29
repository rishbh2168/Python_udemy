def serve_chai():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = serve_chai()
for cup in chai:
    print(cup)  # ------ here next call automatically


def tea():
    yield "tea 1"
    yield "tea 2"
tea_serve = tea()
print(next(tea_serve))

# print(tea)   ----- we need to call next() here manually 