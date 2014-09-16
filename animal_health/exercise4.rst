|LS| Styling to show density
===============================================================================
A good map is able to convey information quickly and clearly. For example, we can 
use colour to indicate the number of cases in each village of the particular syndrome 
we are investigating.

**The goal for this lesson:**

To review ways of styling our maps so the information is displayed in the clearest 
possible way.

|basic| |FA| Styling to show density
--------------------------------------------------------------------------------

Open the :kbd:`PoultrySuddenDeath_32750` attribute table and have a look at the columns. 
What do you notice? What information can you easily display on your map?

Take a look at the *cases* column. It tells you the number of cases recorded in 
each village. We can use colour coding to display this information on our map.

To do this, open the layer properties for :kbd:`PoultrySuddenDeath_32750` and click on the 
*Style* tab.

Select *Graduated* from the pull-down rendering menu. This spreads our chosen colours 
from light to dark, or dark to light.

Set the *Column* to *cases*, and the *Classes* to 5.

The *Color ramp* can stay at blue for now, and the *Mode* can be set to *Equal Interval*. 
QGIS should immediately provide a set of five blue colours, with five equally spaced 
intervals. (If not, click on *Classify*).

Click on *Apply* to see how this looks on your map.

What do you notice?

.. image:: ../_static/ISIKHNAS/022.png
   :align: center

Our points on the map are very small, and it is difficult to distinguish the colour variation. 
One way to change this is to experiment with the size of the points. 

To do this, open the layer properties for :kbd:`PoultrySuddenDeath_32750` and click on the 
*Style* tab again. This time, click on the change button next to *Symbol*. Experiment with 
the size of the point until you think it is large enough to show the varying shades.

This is what it looks like when the size is set to 5 millimetres:

.. image:: ../_static/ISIKHNAS/023.png
   :align: center

|WN|
--------------------------------------------------------------------------------

This improves our map for showing which villages have recorded the most cases, but it would be 
better if we could show this using the village boundaries. 

In our next lesson, we will learn how to join layers together by their location. This will enable 
us to create a new file that combines attributes such as the case numbers from the 
:kbd:`PoultrySuddenDeath_32750` shapefile and the village boundaries from the :kbd:`VillagePolyBarSin_32750` 
shapefile. 