from database import DAO
from model.model import Model

model = Model()
model.add_edges()

print(model.getNumNodes())
print(model.getNumEdges())

model.getConnessa(1234)