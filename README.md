
Convert B3 "BVBG.186.01 - Simplified Price Report - Equities" xml file to tab separated table. See table in the tsv dir.
The script extract selected info from the xml file.

The job is done by the funcion ´xml2table()´ that depends on ´from xml.dom import minidom´. 
The xml nodes are found by the tagname 'PricRpt' using ´xmldoc.getElementsByTagName('PricRpt')´
