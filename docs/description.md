# Research Software Engineering

**Author:** Antonia A. Jost  
**Date:** 13 April 2024

## The Data Set

The chosen data set is accessible [here](https://www-genesis.destatis.de/genesis//online?operation=table&code=46331-0001&bypass=true&levelindex=1&levelid=1714400794387#abreadcrumb). Titled "Empfang und Versand von Gütern (Seegüterumschlag deutscher Häfen): Deutschland, Jahre, Güterabteilungen und -gruppen" in German, its English translation is "Receipt and dispatch of goods (sea cargo handling in German ports): Germany, years, cargo divisions and groups". My data set spans a ten-year time period, chosen to have enough data to conduct meaningful analyses without introducing excessive complexity or data overload. In the rows, all the different kinds of goods are listed, while the columns represent the years. There are two columns per each year, one for import and the other for export of goods. The cell values are integers and their unit is tonnes. There is barely any missing data.

## Motivation

The motivation to choose some data about marine freight transport originated from my experience living in Bremerhaven last summer, where 7.8 million m² of the city is dedicated to the harbour. Every time I walked along the dike, I was wondering what might be inside those massive vessels docking there. So when I noticed this data set on Destatis, it sparked my curiosity again to take a closer look at "what is inside".

## Further Investigation Possibilities

There are several interesting questions that one could ask about the mentioned data set, so here is a collection of some of those:

- How have import and export volumes changed over the ten-year period? Can we identify some broader economic trends or shifts in trade patterns?
- Which categories of goods are most frequently imported and exported? Can we highlight specific resource availabilities?
- How will this import/export continue in the future? Can we forecast some future trends in either cargo volume or which goods will be required most?
- Is there a correlation between the import and export volumes of certain goods? For example, does an increase in import of raw materials correlate with an increase in export of finished products?
- Can we identify factors (and if so which) that significantly impact the volume of goods handled?
- Can we see similar trends in the export of crops that need similar growing conditions and can we maybe link their export amount per year to certain climatic conditions during that time?
- Are technological, or in general processed, goods imported more rapidly/slower than agricultural products and how about the amounts each?
