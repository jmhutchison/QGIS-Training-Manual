|LS| Classification
===============================================================================

Labels are a good way to communicate information such as the names of
individual places, but they can't be used for everything. For example, let's
say that someone wants to know what types of land cover are in the Bandung districts area. 
Using labels, you'd get this:

.. image:: ../_static/classification/001.png
   :align: center

Obviously this is not ideal, so we need another solution. That's what this
lesson is about!

**The goal for this lesson:** To learn how to classify vector data effectively.

|basic| |FA| Classifying nominal data
-------------------------------------------------------------------------------


* Open :guilabel:`Layer Properties` for :guilabel:`bandung_districts`
* Go to the :guilabel:`Style` tab.
* Click on the dropdown that says :guilabel:`Single Symbol`:

.. image:: ../_static/classification/002.png
   :align: center

* Change it to :guilabel:`Categorized` and the interface will change:

.. image:: ../_static/classification/003.png
   :align: center

* Change the :guilabel:`Column` to :guilabel:`LANDCOVER` and the :guilabel:`Color
  ramp` to :guilabel:`random`:

.. image:: ../_static/classification/004.png
   :align: center

* Click the button labeled :guilabel:`Classify` and then click :guilabel:`OK`.

You'll see something like this:

.. image:: ../_static/classification/005.png
   :align: center

* Click the arrow (or plus sign) next to :guilabel:`bandung_districts` in the
  :guilabel:`Layer list`, you'll see the categories explained:

.. image:: ../_static/classification/006.png
   :align: center

So, this is useful! But it hurts your eyes to look at it, so let's see what we
can do about that.

* Open :guilabel:`Layer Properties` and go to the :guilabel:`Style` tab again.
* Change the symbol:

.. image:: ../_static/classification/007.png
   :align: center

* Get rid of the outline the same way you did before, and click :guilabel:`OK`.
  (If you need to, go back to the lesson where we covered this to remember how
  it's done.)
* Click the :guilabel:`Delete all` button:

.. image:: ../_static/classification/008.png
   :align: center

This gets rid of the ugly classes so you can try again.

* Choose a new option from the :guilabel:`Color ramp`
* Click :guilabel:`Classify` again, and the new symbols will appear.
  
You'll notice they don't have outlines. This is because you just
removed the outlines.

* Change the color for :guilabel:`Water bodies` by double-clicking on the colored block
  representing its symbol:

.. image:: ../_static/classification/009.png
   :align: center

Use your own colors, so that the resulting map isn't as ugly as the old one. 
In the example, we'll use these colors, with our water bodies colored blue:

.. image:: ../_static/classification/011.png
   :align: center

This gives us a nice map:

.. image:: ../_static/classification/010.png
   :align: center

There is one category that is empty:

.. image:: ../_static/classification/012.png
   :align: center

* Select the empty category.
* Click the :guilabel:`Delete` button.

This only gets rid of the symbol, not the data, so don't worry about messing
up; you're not actually deleting anything that you can't recover.

Remember to save your map now so that you don't lose all your hard-earned
changes!

|basic| |TY| More classification
-------------------------------------------------------------------------------

If you're only following the basic-level content, use the knowledge you gained
above to classify the :guilabel:`urban` areas. Use darker colors to set them
apart from the farms.

|moderate| |FA| Ratio classification
-------------------------------------------------------------------------------

There are four types of classification: *nominal*, *ordinal*, *interval* and
*ratio*.

In nominal classification, the categories that objects are classified into are
name-based; they have no order. For example: town names, district codes, etc.

In ordinal classification, the categories are arranged in a certain order. For
example, world cities are given a rank depending on their importance for world
trade, travel, culture, etc.

In interval classification, the numbers are on a scale with positive, negative
and zero values. For example: height above/below sea level, temperature
above/below freezing (0 degrees Celsius), etc.

In ratio classification, the numbers are on a scale with only positive and zero
values. For example: temparature above absolute zero (0 degrees Kelvin),
distance from a point, the average amount of traffic on a given street per
month, etc.

In the example above, we used nominal classification to show different land cover 
areas. Now we will begin a new project, and look at ratio classification to classify 
villages by area.

* Save your rural symbology (if you want to keep it) by clicking on the
  :guilabel:`Save Style ...` button in the :guilabel:`Style` dialog.
* Close the :guilabel:`Style` dialog.
* Save and close your current project.

Now we will begin our new exercise.

* Open a new, blank project
* Open the layers :guilabel:`Sulawesi_dist_32750` and :guilabel:`VillagePolyBarSin_32750`.
* Change the colour styles if necessary.
  
We want to classify these villages by area, but there is a problem: they do not have
an area field! We will have to make one.

* Enter edit mode by clicking this button:

.. image:: ../_static/classification/013.png
   :align: center

* Add a new column with this button:

.. image:: ../_static/classification/014.png
   :align: center

* Set up the dialog that appears, like this:

.. image:: ../_static/classification/015.png
   :align: center

* Click :guilabel:`OK`.
  
The new field will be added (at the far right of the table; you may need to
scroll horizontally to see it). However, at the moment it is not populated, it
just has a lot of :kbd:`NULL` values.

To solve this problem, we'll need to calculate the areas.

* Open the field calculator:

.. image:: ../_static/classification/016.png
   :align: center

You'll get this dialog:

.. image:: ../_static/classification/018.png
   :align: center

* Change the values at the top of the dialog to look like this:

.. image:: ../_static/classification/017.png
   :align: center

* In the :guilabel:`Function List`, select :menuselection:`Geometry --> $area`:

.. image:: ../_static/classification/019.png
   :align: center

* Double-click on it so that it appears in the :guilabel:`Expression` field.
* Click :guilabel:`OK`.

Now your :kbd:`AREA` field is populated with values! Admire them, then close
the attribute table.

.. note::  These areas are in degrees area. Later, we will compute them in
   square meters.

* Open the :guilabel:`Layer properties` dialog's :guilabel:`Style` tab.
* Change the classification style from :guilabel:`Classified` to
  :guilabel:`Graduated`:

.. image:: ../_static/classification/020.png
   :align: center

* Change the :guilabel:`Column` to :guilabel:`AREA`:

.. image:: ../_static/classification/021.png
   :align: center

* Under :guilabel:`Color ramp`, choose the option :guilabel:`New color ramp...`
  to get this dialog:

.. image:: ../_static/classification/022.png
   :align: center

* Choose :guilabel:`Gradient` (if it's not selected already) and click
  :guilabel:`OK`. You'll see this:

.. image:: ../_static/classification/023.png
   :align: center

You'll be using this to denote area, with small areas as :guilabel:`Color 1`
and large areas as :guilabel:`Color 2`.

* Choose appropriate colors.
  
In the example, the result looks like this:

.. image:: ../_static/classification/024.png
   :align: center

* Click :guilabel:`OK`.
* Choose a suitable name for the new color ramp.
* Click :guilabel:`OK` after filling in the name.
  
Now you'll have something like this:

.. image:: ../_static/classification/025.png
   :align: center

Leave everything as-is.

* Click :guilabel:`Apply`:

.. image:: ../_static/classification/026.png
   :align: center


.. _backlink-classification-refine-1:

|moderate| |TY| Refine the classification
-------------------------------------------------------------------------------

* Get rid of the lines between the classes.
* Change the values of :guilabel:`Mode` and :guilabel:`Classes` until you get a
  classification that makes sense.

:ref:`Check your results <classification-refine-1>`

|hard| |FA| Rule-based classification
-------------------------------------------------------------------------------

It's often useful to combine multiple criteria for a classification, but
unfortunately normal classification only takes one attribute into account.
That's where rule-based classification comes in handy.

* Open the :guilabel:`Layer Properties` dialog for the :guilabel:`rural` layer.
* Switch to the :guilabel:`Style` tab.
* Switch the classification style to :guilabel:`Rule-based`. You'll get this:

.. image:: ../_static/classification/029.png
   :align: center

* Click the :guilabel:`Add` button.
* A new dialog that appears.
* Click the ellipsis :guilabel:`...` button next to the :guilabel:`Filter` text area.
* Using the query builder that appears, enter the criterion :kbd:`AREA >= 30000000` and choose a light color for it.
* Add the criterion :kbd:`AREA <= 30000000` and choose a dark color.
* Add the criterion :kbd:`DESA = 'Ajakkang'` and assign it the color black, with transparency at :kbd:`35%`.
* Use the :guilabel:`Rendering order` to render the layers correctly so Ajakkang is visible.

Your dialog should look like this:

.. image:: ../_static/classification/030.png
   :align: center

* Apply this symbology.

Your map will look like this:

.. image:: ../_static/classification/031.png
   :align: center

Now you have two area classes, with the village Ajakkang highlighted.

|IC|
-------------------------------------------------------------------------------

Symbology allows us to represent the attributes of a layer in an easy-to-read
way. It allows us as well as the map reader to understand the significance of
features, using any relevat attributes that we choose. Depending on the
problems you face, you'll apply different classification techniques to solve
them.

|WN|
-------------------------------------------------------------------------------

Now we have a nice-looking map, but how are we going to get it out of QGIS and
into a format we can print out, or make into an image or PDF? That's the topic
of the next lesson!
