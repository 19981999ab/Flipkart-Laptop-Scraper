.. Flikart_Laptop_Scraper documentation master file, created by
   sphinx-quickstart on Sun Jun  2 16:33:03 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Usage
==================================================


Since the project's aim was to store the data in a dictionary in a pickled form, all of the code is written in the spiders file and pipelines and items files are left untouched. 

User agents have also been used but this project only scrapes data until 18 pages and each page has 24 laptops so it can scrap at max 432 laptops.

To run this project use the following command ::.
    >>python fkart_laptops.py #no. of laptops to be pickled #directory

Example ::.
    >>python fkart_laptops.py 100 D:/

Before executing this command make sure to navigate to the folder fk_laptops/fk_laptops/spider.

This command will make a dict.pickle file in "D:/" directory

.. toctree::
   :maxdepth: 2


