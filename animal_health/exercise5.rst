|LS| Joining two layers together
===============================================================================
There are two ways we can join layers together:

* we can use the *Join by location* tool to create a new layer combining the attributes from two different layers, or, 
* we can join using a single matching attribute.


**The goal for this lesson:**

To use create a new shapefile using the *Join by location* tool

To display information from a non-spatial file on a spatial file, by joining the two 
using a common data field.

|moderate| |FA| Join attributes by location
--------------------------------------------------------------------------------
In the last lesson we reviewed how to use colour to show the density of case records 
in each village however the results were not really adequate because our file containing 
the case records shows them on the map as point data. We would really like to colour the 
entire villages as shown in the file containing the village boundaries. We can't do this 
using the file as it is, because it does not contain the cases information. We need to join 
the two files using the *Join attributes by location* tool, located under *Data Management 
Tools* in the *Vector* menu.

.. image:: ../_static/ISIKHNAS/024.png
   :align: center


Use the :kbd:`VillagePolyBarSin_32750` file as the Target vector layer, and the :kbd:`PoultryMortality_32750` 
file as the Join vector layer:

* Click on *Take the summary of the first located feature* under *Attribute Summary*
* Tick the :guilabel:`Sum` box underneath.

Browse to where you are going to save your file, and name it appropriately (we used 
:kbd:`PoultryMJoinLocation_32750`).

Only keep the matching records. Click *OK* and add the new layer to your map.

Close the *Join attributes by location* dialog box.
 
Your results should look similar to this:

.. image:: ../_static/ISIKHNAS/025.png
   :align: center

Now open the *Attribute table* of your new layer. You can see that the new layer has the 
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

Explore the effect of each of these, using *Apply* to see the changes each makes to your map.

|LS| Joining vectors by attribute
===============================================================================

For this exercise, we would like to join a file from the iSIKHNAS database, with 
no associated spatial data, with a shapefile that does have geometric data.  By 
doing this, we can display the data from the iSIKHNAS file on a map of Indonesia.

**The goal for this lesson:**

Your supervisor would like the data in a report from iSIKHNAS displayed on a map 
of Indonesia. 

The problem you face is there isn’t any spatial data associated with the data file.

To display the data for your supervisor, you are going to have to join the data 
file to a file that contains spatial data (such as a shapefile) and can be displayed.

|basic| |FA| Load the required files
--------------------------------------------------------------------------------

Load the particular shapefile you wish to use. This could be:

:kbd:`Provinces`

:kbd:`Districts`

:kbd:`Sub-districts`

In this example we are using the :kbd:`Provinces` shapefile.

There are two ways in which we can load our table from iSIKHNAS. You already know 
the first one – loading layers using the *Add vector layer button*. 

.. image:: ../_static/ISIKHNAS/025a.png
   :align: center

In this scenario, you might download the data file you need as a .csv file from 
the iSIKHNAS website. 

Save the .csv file in a folder where you will find it again.

Upload it to QGIS using the *Add vector layer* option. 

Remember to choose the correct file type (in this case .csv). Otherwise it may default 
to shapefiles, and you will not be able to choose your .csv file.

.. image:: ../_static/ISIKHNAS/025b.png
   :align: center 

Or, you might want to load your own Excel file that you have been working with. From 
QGIS 1.8 onwards, you are able to load an *Excel* file directly into QGIS as well.

.. note::  QGIS 1.8 will import Excel files saved as .xls, NOT in the newer .xlsx format. 
	
If you are using QGIS 2.0 onwards, it should be able to import an .xlsx file.

::

The second way is using the supplied user login details to connect directly with the database.

.. image:: ../_static/ISIKHNAS/025c.png
   :align: center
 
In this example we have used the :kbd:`rph_prov_week_gis_centroid` table, from the iSIKHNAS 
training database. 

We have found this by scrolling through the available tables.

.. image:: ../_static/ISIKHNAS/025d.png
   :align: center

Double-click on the table and it will load in QGIS. 

Our example QGIS project now looks like this. Save this as a new project.

.. image:: ../_static/ISIKHNAS/025e.png
   :align: center


 
|basic| |FA| Compare the loaded files
--------------------------------------------------------------------------------

Look closely at the Layers window, and the two files shown there. 

What do you notice?

.. image:: ../_static/ISIKHNAS/025f.png
   :align: center
 
The layer for the provinces can be displayed in QGIS, and therefore must contain 
spatial data. We know this from the little polygon icon next to the file name, and 
the little tick box beside it.

The layer for the slaughter statistics does not contain spatial data. It is a table 
only and cannot be displayed. We know this from the little table icon next to the 
file name, and there is no tick box.

Now compare the attribute tables for :kbd:`rph_prov_week_gis_centroid` and :kbd:`Provinces`. 

What do you notice?

.. image:: ../_static/ISIKHNAS/025g.png
   :align: center

.. image:: ../_static/ISIKHNAS/025h.png
   :align: center

Both files contain an identical field – *code* (this is the unique code for 
each location).

The *code* field is the field we can use to join these two layers together. By creating 
a join, we can display the attributes from the :kbd:`rph_prov_week_gis_centroid` file with 
the images from the :kbd:`Provinces` shapefile.

|Moderate| |FA| Joining files
--------------------------------------------------------------------------------

Right-click on the :kbd:`Provinces` shapefile and open the layer *Properties*. Click on the 
*Join* tab as shown below:

.. image:: ../_static/ISIKHNAS/025i.png
   :align: center 

Click on the green plus sign, to open this window:

.. image:: ../_static/ISIKHNAS/025j.png
   :align: center

The *join layer* is the :kbd:`rph_prov_week_gis_centroid` file. 

The *join field* is the field in the :kbd:`rph_prov_week_gis_centroid` file that we are 
going to use to join the two files. In this case, we are going to use the field 
*code*. This is selected from the drop down list.

The *target field* is *code* again – this is the field in the :kbd:`Provinces` file that 
has matching data to the *code* field in the :kbd:`rph_prov_week_gis_centroid` file.

.. image:: ../_static/ISIKHNAS/025k.png
   :align: center

The names of these fields do not necessarily have to match, but the information 
contained in each field must refer to the same attribute. 

For example, one file might use the name *code* and the other file might use the 
name *location_code*. We can still join the two files as long as the data itself 
is identical.

In this case we are referring to the code given to each location.

Click OK.

Now open the attribute table for the :kbd:`Provinces shapefile` again.

What can you see?

.. image:: ../_static/ISIKHNAS/025l.png
   :align: center

The attributes from the :kbd:`rph_prov_week_gis_centroid:kbd:` file (*gid*, *name*, and *sum*) are 
now in the attribute table for the :kbd:`Provinces` file. The 

We can now use this to map the data from the :kbd:`rph_prov_week_gis_centroid` file on the 
:kbd:`Provinces` image.

|basic| |TY| Format your new map using the styling tab
--------------------------------------------------------------------------------

Using the skills you learnt earlier about style formatting, look for ways that will 
display your data in a way that is helpful.

For example, we can now format our map to show density, because we have the sum of 
the number of animals slaughtered in our new attribute table.

.. image:: ../_static/ISIKHNAS/025m.png
   :align: center

Our :kbd:`rph_prov_week_gis_centroid` file contained summary slaughter statistics for each 
province. 

By joining this file with the :kbd:`Provinces` file, we are able to format the style to 
indicate the numbers of animals slaughtered in each province. 

|IC| 
--------------------------------------------------------------------------------
It is possible to display the information in a data file that does not contain 
spatial data by joining it to a file that does contain spatial data.

Both files must contain an identical data field in order to join the two files.

The headings of the two fields do not have to be the same – just the data contained 
in those fields. 


|WN|
--------------------------------------------------------------------------------

In our next, and final, exercise, we will investigate some of the movements data (showing livestock 
moving from one place to another). Here we will work through a simple and practical exercise as 
another example of an actual task that you may be asked to complete. 
