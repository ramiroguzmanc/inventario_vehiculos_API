# Prueba técnica Gateway IT (API)

Este proyecto hace parte de la prueba técnica de Gateway IT. Específicamente este repositorio corresponde a la API del proyecto.

A continuación se describen los pasos a seguir para la ejecución del proyecto. Tener en cuenta que para un correcto funcionamiento y visualización de este proyecto, debe estarse ejecutando el proyecto perteneciente al FRONTEND. Link del proyecto FRONTEND EN REACT: https://github.com/ramiroguzmanc/inventario_vehiculos_front




## Instalación y ejecución

Inicialice un nuevo entorno virtual (venv) con el comando:

```bash
  py -m venv venv
```
    
Cuando termine la creación del venv, acceda al venv mediante la ejecución:

```bash
  .\venv\Scripts\activate 
```

Instale los requerimientos necesarios del proyecto con:

```bash
  pip install -r requirements.txt
```

Ejecute las migraciones mediante el comando:

```bash
  py manage.py migrate
```

Cree un superusuario mediante el comando. TENGA EN CUENTA QUE ESTE USUARIO LO UTILIZARÁ EN EL FRONTEND PARA ACCEDER:

```bash
  py manage.py createsuperuser
```

Ejecute el proyecto con el comando:

```bash
  py manage.py runserver
```

Una vez ejecutado el proyecto, puede acceder desde el FRONTEND.

Link repo Frontend: https://github.com/ramiroguzmanc/inventario_vehiculos_front
## Autor

- [Ramiro Guzmán C.](mailto:ramiroguzmanc@gmail.com)

