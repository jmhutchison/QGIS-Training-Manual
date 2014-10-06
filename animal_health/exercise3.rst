|LS| Buffering 
===============================================================================
Now we have have our layers necessary to create our 15 kilometre buffer. Or do we? 

**The goal for this lesson:**

To consider and understand point data versus polygon data, and how what effect each type 
will have when creating a buffer zone.

|basic| |FA| Point data, centroids and polygons
--------------------------------------------------------------------------------

If you look at your map you will notice that the cases of poultry mortality occur mostly 
in the districts of Barru and Sinjai.

For this exercise we are going to add a new vector layer, :kbd:`VillagePolyBarSin_32750`, which shows the 
boundaries of the village polygons in Barru and Sinjai.

Once you have loaded this layer, arrange the layers so the cases are on top of the village boundaries. 
Look closely at where the cases lie within the village polygons (you may have to zoom in closer 
on your map).

What do you notice?

.. image:: ../_static/ISIKHNAS/015.png
   :align: center

Every case is positioned in the centre of the village boundaries. This suggests they are not 
the exact coordinates of where the case occurred - all we know is the case occurred somewhere 
in that particular village. The data is recorded at village level, and it is positioned 
using the centroid of the village polygon.

How will this affect our 15 kilometre buffer zone? Let's find out.

|basic| |FA| Buffering from the village centroid
--------------------------------------------------------------------------------

For this buffering exercise we will use the :kbd:`PoultryMortality_32750` file we created. 
Select this layer, and go to the *Vector* menu. Hover over *Geoprocessing Tools* and select 
*Buffer(s)*.

.. image:: ../_static/ISIKHNAS/016.png
   :align: center

The following window will open:

.. image:: ../_static/ISIKHNAS/017.png
   :align: center

Choose :kbd:`PoultryMortality_32750` as the input vector layer, and use a buffer distance of  
15000 (remember your layer units are metres).

Click on *Dissolve buffer results*.

Click on *Browse* and name your new shapefile :kbd:`PoultryM15kmBuffer_32750.shp`.

Add this layer to your map. The result should look something like this:

.. image:: ../_static/ISIKHNAS/018.png
   :align: center

Do you see that the buffers naturally extend into the sea? We will now use the **Clip** function to 
fix this.

|basic| |FA| **Clipping** datasets
--------------------------------------------------------------------------------

We can use one dataset to cut through another dataset, leaving us with only the 
information we want.

In this case, we are going to clip our new buffer layer with the :kbd:`DistrictsSthnSul_32750` layer 
that you should have created in section 16.2.2 **Try yourself... Project the remaining layers**. 

.. note::  You may have named it differently, such as :kbd:`Sul_sth_dist_32750`.

::

Again, we move to the *Vector* menu, hover over the *Geoprocessing Tools*, and select *Clip*. 

.. image:: ../_static/ISIKHNAS/019.png
   :align: center
 
Our input layer is the layer we want to change, in this case our new buffer layer. The clip layer is 
the layer we will use cut around our buffered layer.

Click on the *Browse* button, and name your new shapefile :kbd:`PoultryM15kmBufferClip_32750.shp`.

Add it to the map. 

Remove the :kbd:`PoultryM15kmBuffer_32750.shp` layer.

Your screen should now look similar to this:

.. image:: ../_static/ISIKHNAS/020.png
   :align: center
 
Our new layer is fitting nicely within the coastlines of South Sulawesi and your supervisor can easily 
see where the 15 kilometre buffers extend to. 

But is this the best buffer zone for the data? 

Remember the data suggests the cases are recorded in the database as being in the centre 
of each village - in reality they are probably taken from anywhere within the village boundary. 

This means our 15 kilometre buffers are not going to be as accurate as they might be. 

In the next section we will create the buffer using the village polygon layer and compare the two results.

|basic| |TY| Buffering using the village polygon
--------------------------------------------------------------------------------

Using the same skills you have learnt above to buffer and clip layers, create a 15 kilometre 
buffer zone around the village polygons containing cases of poultry mortality. Clip your new
layer and add it to your map, naming it :kbd:`PoultryM15kmBufferPolyClip_32750`.

Rearrange the layers, so that the buffer zone created with the village centroids is visible over the 
top of your new buffer zone created with the village polygons. What do you notice?

.. image:: ../_static/ISIKHNAS/021.png
   :align: center
 
 
In this picture, the dark green shows the buffer zone around the village polygons (shown in the light 
colour). The lighter green shows the buffer zones created using the case data points.

Since we don't know exactly where each case occurred, it is a good idea to consider using the 
village polygons when creating a buffer zone, not the village centroids.

|WN|
--------------------------------------------------------------------------------

It would be useful if we could estimate by looking at our map how many cases have been 
recorded in each village. In our next lesson we will review more styling, and how to colour 
areas according to particular attributes we wish to display.

