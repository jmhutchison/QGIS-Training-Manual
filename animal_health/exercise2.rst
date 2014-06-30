|LS| Projecting layers 
===============================================================================

We have created a map showing all the cases of sudden death in poultry in the 
Sulawesi Selatan region. Now we need to consider our approach to creating the required 
15 kilometre buffer zone around these cases.

**The goal for this lesson:**

To review map projections 

|basic| |FA| Projecting the layers
--------------------------------------------------------------------------------
Think back to Chapter 7 where you learnt about projections, and now take a look at the layers 
on your map. Is their CRS (Coordinate Reference System) a Geographic Coordinate Reference 
System (GCS) or a Projected Coordinate System (PCS)? How can you tell?

The easiest way is to check the 'Coordinate' box at the bottom of the map canvas. It should 
be showing longitude and latitude values in decimal degrees, separated by a comma e.g. 
120.723,-4.971.

To find even more detail about a layer's CRS, right-click on the layer, and go to *Properties*, 
then click on the *General* tab you will see that the CRS is EPSG:4326 - WGS 84. 
Even greater detail is seen when you click on the *Metadata* tab.

.. image:: ../_static/ISIKHNAS/013.png
   :align: center
   
As a general rule, if you are going to manipulate spatial data using tools from the *Vector* menu, 
your layers will need to be projected to a format where distance is expressed in measurement units 
such as metres.

For this exercise we will use the Universal Transverse Mercator (UTM) zone 50s (EPSG 32750).

* Right-click on the :kbd:`Cases_PoultrySuddenDeath` layer in the :guilabel:`Layers list`.
* Select :guilabel:`Save As...` in the menu that appears. You will be shown the :guilabel:`Save vector layer as...` dialog.
* Click on the :guilabel:`Browse` button next to the :guilabel:`Save as` field.
* Navigate to the folder you have nominated to store your exercise data and specify the name of the new layer as :kbd:`PoultrySuddenDeath_32750.shp`.
* Leave the :guilabel:`Encoding` unchanged.
* Click the :guilabel:`Browse` button beneath the dropdown.
* The :guilabel:`CRS Selector` dialog will now appear.
* In its :guilabel:`Filter` field, search for :kbd:`32750`.
* Choose :guilabel:`WGS 84 / UTM zone 50S` from the list.
* Click :guilabel:`OK`.

|basic| |TY| Project the remaining layers
--------------------------------------------------------------------------------

Repeat these steps for your remaining layers, adding the new, projected layers to your map. You can 
now remove the original, unprojected layers from your map. As we have determined that we are only 
using maps from the areas in Sulawesi Selatan, you no longer need your 'Sulawesi' layer.

The option to project 'On the fly' should be turned off.

Your map should now look something like this:

.. image:: ../_static/ISIKHNAS/014.png
   :align: center

Note the 'Coordinate' box shows the units in metres instead of degrees. 

Save your project.
