|LS| Loading point data
===============================================================================
We have worked with data in the form of shapefiles, raster files, and directly from databases. 
Sometimes your data will be in an Excel spreadsheet, with longitude and latitude. 
It is important that you know how to load data when it is in this format.

**The goal for this lesson:**

To load and plot data from a spreadsheet.


|basic| |FA| Loading a Delimited Text File
--------------------------------------------------------------------------------
For this exercise, you will begin a new project.

We have worked with data in the form of shapefiles, raster files, and directly from databases. 
Often you might receive data in the form of a spreadsheet, so it is important to know how to 
load this data into QGIS.

Data is supplied in this way is often in a CSV file, which is a delimited text file. To load 
these types of files, we will use the "Add Delimited Text Layer" plugin:

.. image:: ../_static/ISIKHNAS/033.png
   :align: center
   
 Click on this button, and the following dialog will open:
 
 .. image:: ../_static/ISIKHNAS/034.png
   :align: center
   
 Browse to the course exercise data, and load :kbd:`PointData.csv` from the folder *ISIKHNAS*. This is 
 just randomly generated point data to use for this exercise.
 
 The plugin does a very good job of reviewing the information contained in the file, but you will 
 need to give it some guidance. In this file, the delimiter is a comma, so we need to select "Comma" as 
 the delimiter.
 
 Your dialog box now looks like this:
 
 .. image:: ../_static/ISIKHNAS/035.png
   :align: center
   
Click on the :kbd:`OK` button. You will now be asked to specify the CRS. This should make you think 
about what format the data was collected in. For now we will select WGS 84 EPSG:4326. Click :kbd:`OK`.

You should have a layer similar to the following image:

.. image:: ../_static/ISIKHNAS/036.png
   :align: center

This shape should look familiar - load the shapefile :kbd:`Sul_sthn_dist`, and rearrange the layers so 
the point data is the top layer.

You should now see something like this:

.. image:: ../_static/ISIKHNAS/037.png
   :align: center
   

|IC| 
--------------------------------------------------------------------------------

This chapter has been designed to show you how to use QGIS in a practical and useful way, using real data 
obtained from the iSIKHNAS database. The exercises have been developed to show examples of actual tasks you 
may be asked to carry out by your supervisor.

It is only a small example of what you can do using the QGIS software. If you are interested, do not be 
afraid to explore the software. Use the internet to search for new ways to create particular maps, or 
investigate different ways of doing things.

 