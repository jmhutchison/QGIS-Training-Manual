|LS| Putting it into practice - iSIKHNAS
===============================================================================

In this chapter we are going to use some of what you have learned and apply it to 
data taken from the ISIKHNAS database.

GIS has become an essential tool in the understanding and management of animal 
movements and disease.
It can provide valuable assistance in a range of tasks, including:

1. monitoring animal distribution or movements
2. describing the level and distribution of disease
3. assessing the efficacy of control programs across space
4. developing zones for disease control
5. exploring spatially-linked risk factors
6. management of animal health emergencies.

This exercise is designed to show you how you can use QGIS in a practical way, using 
data that you are familiar with.

**The goal for this lesson:**

Your supervisor has asked you to identify and extract all the cases in the Sulawesi 
Selatan region, where the species is a type of poultry, and the syndrome recorded is 
poultry mortality. S/he would like you to provide a map showing where these cases have 
occurred, and to create a 15 kilometre buffer around the villages in which they have 
occurred.

In order to do this you will have to:

* load vector shapefile layers and create a new QGIS project
* format the styles appropriately
* subset a dataset spatially using *Select by location*
* identify particular records in the attribute table using SQL (structured query language)
* save records to a new shapefile
* save layers with a projection suitable for spatial exercises
* create a buffer zone
* use the clip feature to create a layer including only the data required.


For the purpose of these exercises you will be using the shapefiles provided. It is possible to 
connect directly to the iSIKHNAS database and access the current data however this is beyond the 
scope of this exercise. 

|basic| |FA| Create a new map
--------------------------------------------------------------------------------

Open QGIS. Using the :guilabel:`Add Vector Layer` button, add the following layers 
from the course exercise data, from the folder *ISIKHNAS*:

* :kbd:`Sulawesi`
* :kbd:`Sul_sthn_dist`
* :kbd:`cases_gis`

Your map will now look something like this:


.. image:: ../_static/ISIKHNAS/001.png
   :align: center

The colours will no doubt be different, and probably not suitable. Take the time now 
to change the style to use the *Style* tab in the :guilabel:`Layer Properties` to 
change the colours to those of your choice. As a refresher:

* Right-click on the layer
* Select *Properties*
* Click on the *Style* tab as described above

Here you can change the formatting of the layer in many ways, including colour, fill, symbols, 
lines, and more.

.. image:: ../_static/ISIKHNAS/001a.png
   :align: center

You can save the colours you choose as styles, so you can easily apply them to other projects.

|basic| |TY| Saving styles
--------------------------------------------------------------------------------

You might want to save a particular colour to be used for your background layer, both in this 
project and any future mapping projects. To do this, choose the layer you would like to work 
with, for example :kbd:`Sulawesi`. Open the :guilabel:`Layer Properties`.

Explore your options. As shown in the above image, there are two *Change* buttons.

The first *Change* button, with the little spanner, allows you to format items including:

* the symbol layer type
* the colour
* the fill style
* the border colour
* the border style
* the border width

If you only want to change the colour of the layer, click on the second *Change* button.

Once you are happy with your layer style, click on *Save Style ...*

Save your new style with a name that will make sense to you later, such as :kbd:`BaseCountry`. 
It is a good idea to save all your styles in the one folder so you can easily find them again.

To use a style you have saved, click on the *Load Style ...* button.

We changed our colours of our layers to this:

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
layer containing just the features we are interested in.

|moderate| |FA| Selecting by location
--------------------------------------------------------------------------------

Now that we have our map layers loaded into our project, we would like to work specifically 
with Sulawesi, and in particular, the cases that have been recorded in the Sulawesi Selatan 
districts. Currently our map shows all the cases recorded throughout Indonesia at the time 
the data was downloaded.

Open the :guilabel:`Select by Location`. We want to select the features in the :kbd:`cases_gis` 
file that intersect with the :kbd:`Sul_sthn_dist` file:

.. image:: ../_static/ISIKHNAS/005.png
   :align: center

Click 'OK' and check your map. You should see that the cases that occur in Sulawesi Selatan
are now highlighted:

.. image:: ../_static/ISIKHNAS/006.png
   :align: center

Save this selection as a new layer by right-clicking on the :kbd:`cases_gis` layer, and then 
clicking on *Save Selection As...*:

.. image:: ../_static/ISIKHNAS/007.png
   :align: center
   
Save your new layer as :kbd:`Sul_sthn_cases` and add it to your map. If you feel the need, format 
the colour.

You can now remove the :kbd:`cases_gis` layer.

|basic| |FA| Inspect the data
--------------------------------------------------------------------------------
As mentioned above, you need to extract all the cases of poultry mortality in poultry in the 
Sulawesi Selatan region. How would you go about doing that?

One answer lies in a layer's :guilabel:`Attribute Table`. Here you are able to see much more 
information about each record in the layer.
The :guilabel:`Attribute Table` has been mentioned earlier, particularly in Chapters 3 and 4. 
Now we are going to use the information contained in the attribute table to select the records 
we require.

When we open the :guilabel:`Attribute Table` for the :kbd:`Sul_sthn_cases` layer, we see several 
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

We can use this screen to find (for example) all the records relating to chickens by typing 
in *chicken* in the *Look for* box, choosing *species* in the drop down box and clicking on 
*Search*. 
Immediately, all the records with chicken recorded as the species are highlighted in the 
attribute table.

.. note::  Notice the *Case sensitive* option. It is best to leave this box unticked. 

	That way your search will return results for *Chicken* and *chicken,* and any other variations of sentence case.

::

However, we don't want just chickens, we want all poultry that are recorded with *poultry mortality* 
as the syndrome. 
To select these records, we need to use the *Advanced search* features.

|moderate| |FA| Selecting records using SQL (Simple Query Language)
--------------------------------------------------------------------------------
The *Advanced search features* allow us to create more specific queries, selecting records with 
the particular attributes we are interested in.


.. image:: ../_static/ISIKHNAS/009.png
   :align: center

Our query is asking for all the records that contain chicken or duck or local chicken as the 
species, **and** a value of 'poultry mortality' in the syndrome2 table.

By testing the query, we find that we have 11 matching records:

.. image:: ../_static/ISIKHNAS/010.png
   :align: center

Click *OK* in the window saying *Found 11 matching feature(s),* and click *OK* in the 'Search query 
builder' window. Note that at the top of the attribute table you will now see the heading 
*Attribute table - Sul_cases_sthn (11 matching features)*. Click *Close* on the attribute table.

Now that we have our records selected, we will use the *Save selection as* option that we used before, 
and save this layer to our map. Right-click on the :kbd:`Sul_sthn_cases` layer, and click on *Save selection 
as.* 

.. image:: ../_static/ISIKHNAS/011.png
   :align: center

Name this new layer :kbd:`Cases_PoultryMortality` and add it to your map.
   
By turning off the :kbd:`Sul_sthn_cases` layer, we can now see the records in the database of poultry  
mortality recorded in poultry in Sulawesi Selatan.

.. image:: ../_static/ISIKHNAS/012.png
   :align: center

.. note::  We have used the *Advanced Labeling* tool referred to in Section 4.2.1 *Using labels* to 
	show the labels of each of the districts.

::
	
Save your project.

|moderate| |TY| Selection using SQL
--------------------------------------------------------------------------------

Using the *Advanced search* features in the *Attribute table* for the :kbd:`Sul_sthn_cases` layer, 
try selecting specific records according to various combinations.

Do not be afraid to experiment. Try selecting records different combinations such as the date, 
village, species, syndrome etc.

|IC|
--------------------------------------------------------------------------------

There are several ways available for selecting data. Which method you choose will depend upon 
your needs. 

Using SQL queries enables you to select records according to the particular attributes that are 
of interest to you.
  

|WN|
--------------------------------------------------------------------------------

Now you have your basic map showing where the cases of interest are located. In our next lesson 
we will review why we are going to need to project our layers in order to develop suitable 
buffers.

