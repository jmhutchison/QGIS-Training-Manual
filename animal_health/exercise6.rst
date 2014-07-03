|LS| Working with movements data
===============================================================================
iSIKHNAS contains many types of data. One of these is movements data, showing the 
movement of livestock from one place to another.

**The goal for this lesson:**

To create a map that clearly shows livestock movements.

Your supervisor would like you to extract a dataset of poultry movements between 
certain dates. S/he would then like you to create a map that shows:

* Poultry movements between 1 December 2013 and 31 December 2013
* Format the style to clearly show density

|moderate| |FA| Selecting data using SQL
--------------------------------------------------------------------------------

For this exercise, start a new project. Load the following shapefiles supplied in your 
data folder:

* :kbd:`Indonesia_32750`
* :kbd:`Sulawesi_dist_32750`
* :kbd:`Movements_32750`

Use the *Layer Properties* to style the layers as necessary like you have done in the 
exercises.

Your new map should look similar to this:

.. image:: ../_static/ISIKHNAS/026.png
   :align: center

Open the *Attribute table* for the :kbd:`Movements_32750` layer. You can do this by 
either right-clicking on the :kbd:`Movements_32750` layer, and selecting *Open Attribute 
Table*, or you can click on the icon in the menu bar as shown below:

.. image:: ../_static/ISIKHNAS/027.png
   :align: center

Here we will select the records we want using SQL. Open the *Advanced search* option. You 
want to select all records relating to poultry, that are between 1 December 2013 and 31 
December 2013.

To do this, you need the following query:

("Tanggal" >= '2013-12-01' AND  "Tanggal" <= '2013-12-31') AND (("Spesies" = 'broiler') OR 
("Spesies" = 'chicken') OR ("Spesies" = 'duck') OR ("Spesies" = 'pigeon'))

This query is asking to return records:

Between the two dates: 
("Tanggal" >= '2013-12-01' AND  "Tanggal" <= '2013-12-31')

AND

With the following species:

(("Spesies" = 'broiler') OR ("Spesies" = 'chicken') OR ("Spesies" = 'duck') OR ("Spesies" = 'pigeon'))

If you test the query, it should return 30 records:

.. image:: ../_static/ISIKHNAS/028.png
   :align: center

Close the attribute table. Your selected records should be highlighted in yellow on your map.

Right-click on the :kbd:`movements_32750` and choose the *Save selection as* option. Save your new layer 
with an appropriate name such as :kbd:`movements_poultry_32750`. You can now remove the :kbd:`movements_32750` 
layer.

When you look closely, you will see that all the movements take place in Sulawesi. If you like, you can remove 
the layer :kbd:`Indonesia_32750`.

In the next section we will review styling again, and show density in our movement data.

|moderate| |FA| Style formatting
--------------------------------------------------------------------------------
Our movements data for is now showing on the map, but it doesn't really tell us too much about it. We can 
use styling to show more.

Right-click on your new :kbd:`movements_poultry_32750` and click on the *Style* tab.

As you have learnt previously, here you can style your layer to show attributes such as density. You can also:

* colour the movement lines according to the number of animals in each movement (density)
* increase the width of the movement lines to show the number of animals in each movement
* layer the movement lines so thinner lines are displayed on top of the wider lines

|moderate| |TY| Style formatting
--------------------------------------------------------------------------------
Review Section 16.4.1 *Styling to show density* and Section 16.5.2 *Style the villages to show the density 
of the recorded cases*.

Format the movement lines using colour to show the number of animals in each movement. The column you will use 
is *Jumlah Hew*.

Once you have your individual lines, you can double-click on each one and a new window will open. Here 
you can edit your line for things such as width, colour, transparency:

.. image:: ../_static/ISIKHNAS/029.png
   :align: center

Experiment with the width of each line until you are happy with your results.

After changing the width of each graduated line, you will then be able to order the lines so the widest lines 
appear underneath the thinnest ones.

Still in the *Layer properties* window, click on *Advanced*, and then *Symbol levels*:

.. image:: ../_static/ISIKHNAS/030.png
   :align: center

This opens up a new window, where you can order your symbols:

.. image:: ../_static/ISIKHNAS/031.png
   :align: center

When ordering symbols, the first symbol to be placed on the map is the one with a zero. In the image above, 
you can see that our widest line is a zero, and the narrowest line is a four. The result is this:

.. image:: ../_static/ISIKHNAS/032.png
   :align: center

This shows our lines formatted according to the number of livestock movements, using colour and line width.

|IC| 
--------------------------------------------------------------------------------

This chapter has been designed to show you how to use QGIS in a practical and useful way, using real data 
obtained from the iSIKHNAS database. It is only a small example of what you can do using the QGIS software. 
If you are interested, do not be afraid to explore the software. Use the internet to search for new ways to 
create particular maps, or investigate different ways of doing things.

