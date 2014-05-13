|LS| Buffering 
===============================================================================
Now we have have our layers necessary to create our 15 kilometre buffer. Or do we? 

**The goal for this lesson:**

To consider and understand point data versus polygon data, and how what effect each type 
will have when creating a buffer zone.

|basic| |FA| Point data, centroids and polygons
--------------------------------------------------------------------------------

If you look at your map you will notice that the cases of sudden death in poultry occur mostly 
in the districts of Barru and Sinjai. 
For this exercise we are going to add a new vector layer, *VillagePolyBarSin_32750*, which shows the 
boundaries of the village polygons.
Once you have loaded this layer, arrange the layers so the cases are on top of the village boundaries. 
Look closely at where the cases lie within the village polygons (you may have to zoom in closer 
on your map).

What do you notice?

.. image:: ../_static/ISIKHNAS/015.png
   :align: center

Every case is positioned in the centre of the village boundaries. This indicates they are not 
the exact coordinates of where the case occurred - all we know is the case occurred somewhere 
in that particular village. The data is recorded at village level, and it is positioned 
using the centroid of the village polygon.

How will this affect our 15 kilometre buffer zone? Let's find out.

|basic| |FA| Buffering from the village centroid
--------------------------------------------------------------------------------

For this buffering exercise we will use the *PoultrySuddenDeath_32750*. Select this layer, and go to 
the *Vector* menu. Hover over *Geoprocessing Tools* and select *Buffer(s)*.

.. image:: ../_static/ISIKHNAS/016.png
   :align: center

The following window will open:

.. image:: ../_static/ISIKHNAS/017.png
   :align: center

Choose :kbd:`PoultrySuddenDeath_32750` as the input vector layer, and use a buffer distance of  
15000 (remember your layer units are metres).

Click on 'Dissolve buffer results' and name your new shapefile :kbd:`PoultrySD15kmBuffer_32750.shp`.

Add this layer to your map. The result should look something like this:

.. image:: ../_static/ISIKHNAS/018.png
   :align: center

Notice the buffers naturally extend into the sea? We will now use the **Clip** function to amend this.

|basic| |FA| **Clipping** datasets
--------------------------------------------------------------------------------

We can use one dataset to cut through another dataset, leaving us with only the 
information we want.
In this case, we are going to clip our new buffer layer with the *DistrictsSthnSul_32750* layer.

Again, we move to the *Vector* menu, hover over the *Geoprocessing Tools*, and select *Clip*.

.. image:: ../_static/ISIKHNAS/019.png
   :align: center
 
Our input layer is the layer we want to change, in this case our new buffer layer. The clip layer is 
the layer we will use cut around our buffered layer.

Name your new shapefile :kbd:`PoultrySD15kmBufferClip_32750.shp` and add it to the map. Your screen should 
now look similar to this:

.. image:: ../_static/ISIKHNAS/020.png
   :align: center
 
Our new layer is fitting nicely within the coastlines of South Sulawesi and your supervisor can easily 
see where the 15 kilometre buffers extend to. But is this the best depiction of a buffer zone for 
the data? Remember we realised the data points were recorded in the database as being in the centre 
of each village - in reality they are probably taken from somewhere else in the village. This means 
our 15 kilometre buffers are not going to be as accurate as they might be. In the next section we will 
create the buffer using the village polygon layer and compare the two results.

|basic| |TY| Buffering using the village polygon
--------------------------------------------------------------------------------

Using the same skills you have learnt above to buffer and clip layers, create a 15 kilometre 
buffer zone around the village polygons containing cases of sudden death in poultry. Clip your new
layer and add it to your map.

Rearrange the layers, so that the buffer zone created with the village centroids is visible over the 
top of your new buffer zone created with the village polygons. What do you notice?