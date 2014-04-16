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
Once you have loaded this layer, look closely at where the cases lie within the village polygons 
(you may have to zoom in closer on your map).

What do you notice?

.. image:: ../_static/ISIKHNAS/015.png
   :align: center

Every case is positioned in the centre of the village boundaries. This indicates they are not 
the exact coordinates of where the case occurred - all we know is the case occurred somewhere 
in that particular village. The data is recorded at village level so it takes so it is positioned 
using the centroid of the village polygon.


