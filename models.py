import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Categorias(db.Base):
    __tablename__ = "Categorias"
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)

    def __init__(self, contenido):
        self.contenido = contenido

    def __repr__(self):
        return "Categoria {}: {}".format(self.id, self.contenido)

    def __str__(self):
        return "Categoria {}: {} ({})".format(self.id, self.contenido, self.hecha)

class Tarea(db.Base):
    __tablename__ = "Tarea"
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    fecha = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    boton_modificar = Column(Boolean)
    categoria_id =Column(Integer, ForeignKey('Categorias.id'))
    categoria = relationship("Categorias")

    def __init__(self, contenido, hecha, fecha, categoria_id, boton_modificar):
        self.contenido = contenido
        self.hecha = hecha
        self.boton_modificar = boton_modificar
        self.categoria_id=categoria_id
        self.fecha=fecha

    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.fecha, self.hecha)

    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.fecha, self.hecha)