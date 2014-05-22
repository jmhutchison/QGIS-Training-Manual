|LS| More map styling
===============================================================================
A good map is able to convey information quickly and clearly. For example, we can 
use colour to indicate the number of cases in each village of the particular syndrome 
we are investigating.

**The goal for this lesson:**

To review ways of styling our maps so the information is displayed in the clearest 
possible way.

|basic| |FA| Colouring according to density
--------------------------------------------------------------------------------

Open the PoultrySuddenDeath_32750 attribute table and have a look at the columns. 
What do you notice? What information can you easily display on your map?

Take a look at the 'cases' column. It tells you the number of cases recorded in 
each village. We can use colour coding to display this information on our map.

To do this, open the layer properties for PoultrySuddenDeath_32750 and click on the 
'Style' tab.

Select 'Graduated' from the pull-down rendering menu. This spreads our chosen colours 
from light to dark, or dark to light.

Set the 'Column' to 'cases', and the 'Classes' to 5.

The 'Color ramp' can stay at blue for now, and the 'Mode' can be set to 'Equal Interval'. 
QGIS should immediately provide a set of five blue colours, with five equally spaced 
intervals. (If not, click on 'Classify'.)

Click on 'Apply' to see how this looks on your map.

What do you notice?