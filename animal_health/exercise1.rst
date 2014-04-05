|LS| Putting it into practice - ISIKHNAS
===============================================================================

In this chapter we are going to use some of what you have learned and apply it to 
data taken from the ISIKHNAS database.

GIS have become an essential tool in the understanding and management of animal 
movements and disease.
They can provide valuable assistance in a range of tasks, including:

1. monitoring animal distribution or movements
2. describing the level and distribution of disease
3. assessing the efficacy of control programs across space
4. developing zones for disease control
5. exploring spatially-linked risk factors
6. management of animal health emergencies.

This exercise is designed to show you how you can use QGIS in a practical way, using 
data that you are familiar with.

**The goal for this lesson:**

Refresh the following skills learnt in previous chapters:

* creating a new QGIS project
* load vector shapefile layers
* format styles
* apply buffers to data points

Learn new skills, including:

* how to subset a dataset spatially - selecting by location
* identify particular records using SQL

|basic| |FA| Create a new map
--------------------------------------------------------------------------------

Open QGIS. Using the :guilabel:`Add Vector Layer` button, add the following layers 
from the course exercise data:

* Sulawesi
* Sul_sthn_dist
* cases_gis

Your map will now look something like this:


.. image:: ../_static/ISIKHNAS/001.png
   :align: center

The colours will no doubt be different, and probably not suitable. Take the time now 
to change the style to use the *Style* tab in the :guilabel:`Layer Properties` to 
change the colours to those of your choice.

We changed our colours to this:

.. image:: ../_static/ISIKHNAS/002.png
   :align: center

There is a very useful website named **Colorbrewer: Color Advice for Maps** found 
here <http://colorbrewer2.org>' developed by Cynthia Brewer of Penn State.
This site contains a lot of useful information about appropriate colour schemes for maps.

Save your work as a new project.

|basic| |FA| Selecting records
--------------------------------------------------------------------------------
There are several ways of selecting records from layers, including:

* Select Single Feature
* Select Features by Rectangle
* Select Features by Polygon
* Select Features by Freehand
* Select Features by Radius

This are found by clicking on the :guilabel:`Select Features by Polygon` button, and 
referring to the drop down menu.

.. image:: ../_static/ISIKHNAS/003.png
   :align: center

This is a useful tool for selecting one or two features, or quickly drawing around an area. 
When we want to be more accurate, we can use the *Select by Location* tool.

To find the :guilabel:`Select by Location` tool, click on the menu *Vector - Research Tools - Select by location*:

.. image:: ../_static/ISIKHNAS/004.png
   :align: center

By selecting features of one layer that intersect with another, we can create a new 
layer containing just the attributes we are interested in.

|moderate| |FA| Selecting by location
--------------------------------------------------------------------------------

Now that we have our map layers loaded into our project, we would like to work specifically 
with Sulawesi, and in particular, the cases that have been recorded in the South Sulawesi districts.
Currently our map shows all the cases recorded throughout Indonesia at the time the data was 
downloaded.

Open the :guilabel:`Select by Location`. We want to select the features in the *cases_gis* 
file that intersect with the *Sul_sthn_dist* file:

.. image:: ../_static/ISIKHNAS/005.png
   :align: center

Click 'OK' and check your map. You should see that the cases that occur in South Sulawesi 
are now highlighted:

.. image:: ../_static/ISIKHNAS/006.png
   :align: center

Save this selection as a new layer by right-clicking on the *cases-gis* layer, and then 
clicking on *Save Selection As...*:

.. image:: ../_static/ISIKHNAS/007.png
   :align: center
   
Save your new layer as *Sul_sthn_cases* and add it to your map. If you feel the need, format 
the colour.

You can now remove the *cases_gis* layer.

|basic| |FA| Inspect the data
--------------------------------------------------------------------------------
Let's say you have been asked to find out how many records for cattle showing signs of diarrhoea 
are in the ISIKHNAS database for the Southern Sulawesi region.
How would you go about doing that?

One answer lies in a layer's :guilabel:`Attribute Table`. Here you are able to see much more 
information about each record in the layer.
The :guilabel:`Attribute Table` has been mentioned earlier, particularly in Chapters 3 and 4. 
Now we are going to use the information contained in the attribute table to select the records 
we require.

When we open the :guilabel:`Attribute Table` for the *Sul_sthn_cases* layer, we see several 
columns showing information about each record:

.. image:: ../_static/ISIKHNAS/008.png
   :align: center

What information do you notice?

In this example we can see there are 1728 records in total in this layer. The attribute table 
has columns containing the following information:

* gid (Geographic identification)
* reportdate
* caseid
* species
* cases
* reporttype
* syndrome2
* reporter
* desa

We can use this screen to find (for example) all the records relating to cattle by typing in *cattle* 
in the *Look for* box, choosing *species* in the drop down box and clicking on *Search*. 
Immediately, all the records with cattle recorded as the species are highlighted in the attribute 
table.

However, we don't want just want cattle, we want cattle that have shown signs of diarrhoea. 
To select these records, we need to use the *Advanced search* features.

|moderate| |FA| Selecting records using SQL (Simple Query Language)
--------------------------------------------------------------------------------
The *Advanced search features* allow us to create more specific queries, selecting records with 
the particular attributes we are interested in.


.. image:: ../_static/ISIKHNAS/009.png
   :align: center

Our query is asking for all the records that contain cattle as the species, **and** a value of 
diarrhoea in the syndrome2 table.

By testing the query, we find that there are 351 records matching our query:

.. image:: ../_static/ISIKHNAS/010.png
   :align: center

Now that we have our records selected, we will use the *Save selection as* option, and save 
this layer to our map.
   
By turning off the *Sul_sthn_cases* layer, we can now see the records in the database of 
cattle showing signs of diarrhoea (in southern Sulawesi).

.. image:: ../_static/ISIKHNAS/011.png
   :align: center

Note we have used the *Advanced Labeling* tool referred to in Section 4.2.1 *Using labels* to 
show the labels of each of the districts.

|moderate| |TY| Selection using SQL
--------------------------------------------------------------------------------

Using the `Advanced search` features in the `Attribute table` for the `Sul_sthn_cases` layer, 
try selecting specific records according to various combinations.

Do not be afraid to experiment. Try selecting records different combinations such as the date, 
village, species, syndrome etc.

|IC|
--------------------------------------------------------------------------------


|WN|
--------------------------------------------------------------------------------



