from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea, Categorias
app = Flask(__name__)


@app.route('/')
def home():
    todas_las_categorias = db.session.query(Categorias).all()
    return render_template("Inicio.html", lista_de_categorias=todas_las_categorias)


@app.route('/crear-categoria', methods=['POST'])
def crearcat():
    Categoria = Categorias(contenido=request.form['contenido_categoria'])
    db.session.add(Categoria)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/acceso/<id_acceso>')
def acceso(id_acceso):
    todas_las_tareas = db.session.query(Tarea).filter(Tarea.categoria_id == id_acceso)
    return render_template("index.html", lista_de_tareas=todas_las_tareas, id_buscada=id_acceso)


@app.route('/crear-tarea/<id>', methods=['POST'])
def crear(id):
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False, boton_modificar=False, categoria_id=int(id),
                  fecha=request.form['contenido_fecha'])
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("acceso", id_acceso=id))


@app.route('/boton-regreso')
def boton_regreso():
    return redirect(url_for("home"))


@app.route('/eliminar-tarea/<id>/<idcategoria>')
def eliminar(id, idcategoria):
    tarea = db.session.query(Tarea).filter_by(id =int(id)).delete()
    db.session.commit()
    return redirect(url_for("acceso", id_acceso=idcategoria))


@app.route('/eliminar-categoria/<id>')
def eliminarcat(id):
    tarea = db.session.query(Categorias).filter_by(id =int(id)).delete()
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/tarea-hecha/<id>/<idcategoria>')
def hecha(id,idcategoria):
    tarea = db.session.query(Tarea).filter_by(id =int(id)).first()
    tarea.hecha=not tarea.hecha
    db.session.commit()
    return redirect(url_for("acceso", id_acceso=idcategoria))


@app.route('/boton-modificar/<id>/<idcategoria>')
def boton_modificar(id,idcategoria):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.boton_modificar = not tarea.boton_modificar
    return redirect(url_for("acceso", id_acceso=idcategoria))



@app.route('/modificar-tarea/<id>/<idcategoria>', methods=['POST'])#AUNnoseqpd
def modificar(id, idcategoria):
    mod = request.form['modificar_tarea']
    db.session.query(Tarea).filter_by(id =int(id)).update({Tarea.contenido: mod})
    db.session.commit()
    return redirect(url_for("acceso", id_acceso=idcategoria))


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True, port=5000, host='0.0.0.0')
