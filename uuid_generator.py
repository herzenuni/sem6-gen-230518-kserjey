import itertools
import uuid

gen_exp = (uuid.uuid4() for _ in itertools.count())

print(next(gen_exp))
print(next(gen_exp))