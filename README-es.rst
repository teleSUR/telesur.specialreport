=====================
telesur.specialreport
=====================

Es un producto para Plone que permite crear micrositios con especiales en formato flash dentro de los mismos. Los micrositios pueden tener un theme independiente al de Plone.

Instalación
===========

Para instalar `telesur.specialreport` simplemente agregar ``telesur.specialreport``
a la lista de eggs de su buildout, correr buildout y reiniciar Plone.
Después instalar `telesur.specialreport` usando el panel de control de complementos.


Configuración
=============

Para poder aplicar temas propios a cada 'especial' primero debemos instalar dichos temas Diazo.
Para hacerlo se puede cargar el zip del tema al panel de control de Diazo siguiendo los siguientes pasos:

Buscar en http://pypi.python.org/pypi/ los temas disponibles para Plone.

.. figure:: https://raw.github.com/teleSUR/telesur.specialreport/master/docs/config1.png
    :align: center
    :height: 405px
    :width: 706px

Elejir uno para el cual exista un archivo zip que pueda ser descargado.

.. figure:: https://raw.github.com/teleSUR/telesur.specialreport/master/docs/config2.png
    :align: center
    :height: 405px
    :width: 706px

Descargar el archivo y cargarlo en el panel de control de Diazo, "Configuración del Sitio" -> "Diazo theme" -> "Import theme", la opciones "Immediately enable new theme" y "Replace existing theme" deben estar desactivadas.

.. figure:: https://raw.github.com/teleSUR/telesur.specialreport/master/docs/config3.png
    :align: center
    :height: 405px
    :width: 706px

Una vez que tenemos instalado un nuevo tema podemos crear un especial, el primer paso es crear un contenedor para los especiales:

.. figure:: https://raw.github.com/teleSUR/telesur.specialreport/master/docs/config4.png
    :align: center
    :height: 405px
    :width: 706px

Y dentro de nuestra carpeta podemos crear el especial seleccionando el tema que fue cargado anteriormente, la imagen se exibirá como vista previa en la carpeta de especiales y el archivo flash es el que se muestra dentro del especial:

.. figure:: https://raw.github.com/teleSUR/telesur.specialreport/master/docs/config5.png
    :align: center
    :height: 405px
    :width: 706px


Referencias
===========

* `Source code @ GitHub <git@github.com:teleSUR/telesur.specialreport.git>`_

