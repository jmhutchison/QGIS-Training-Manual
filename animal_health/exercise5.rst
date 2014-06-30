|LS| Joining two layers together
===============================================================================
We can use the 'Join by location' tool to create a new layer combining the attributes 
from two different layers.

**The goal for this lesson:**

To use create a new shapefile using the 'Join by location' tool

|moderate| |FA| Join attributes by location
--------------------------------------------------------------------------------
In the last lesson we reviewed how to use colour to show the density of case records 
in each village however the results were not really adequate because our file containing 
the case records shows them on the map as point data. We would really like to colour the 
entire villages as shown in the file containing the village boundaries. We can't do this 
using the file as it is, because it does not contain the cases information. We need to join 
the two files using the 'Join attributes by location' tool, located under 'Data Management 
Tools' in the 'Vector' menu.

.. image:: ../_static/ISIKHNAS/024.png
   :align: center


Use the :kbd:`VillagePolyBarSin_32750` file as the Target vector layer, and the :kbd:`PoultrySuddenDeath_32750` 
file as the Join vector layer.

Click on 'Take the attributes of the first located feature' under 'Attribute Summary'.

Browse to where you are going to save your file, and name it appropriately (we used 
:kbd:`PoultrySDJoinLocation_32750`).

Only keep the matching records. Click 'OK' and add the new layer to your map. 
Your results should look similar to this:

.. image:: ../_static/ISIKHNAS/025.png
   :align: center

Now open the 'Attribute table' of your new layer. You can see that the new layer has the 
attributes of each original file, including the number of cases. We can now use this to 
improve our depiction of case density on the map.

|basic| |TY| Style the villages to show the density of recorded cases
--------------------------------------------------------------------------------

Using the skills from the previous lesson, amend the style to show the case density in each 
village. Experiment with the effect of choosing different intervals:

* **Equal Interval:** Divides your data into equally-spaced groups.
* **Quantile:** Uses an equation to divide values into equal-sized subsets.
* **Natural breaks (Jenks):** Tries to minimise differences within classes whilst maximising the difference between classes. Standard deviation: Illustrates how values deviate from the average.
* **Pretty breaks:** Breaks the values into classes that are easily understood by non-statisticians.

Explore the effect of each of these, using 'Apply' to see the changes each makes to your map.

|WN|
--------------------------------------------------------------------------------

In our next, and final, exercise, we will investigate some of the movements data (showing livestock 
moving from one place to another). Here we will work through a simple and practical exercise as 
another example of an actual task that you may be asked to complete. 

